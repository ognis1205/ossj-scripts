import datetime
import sys
import fire
from traceback import format_exc
from kaggle import api


def main(output='output.txt'):
    with open(output, 'a') as output:
        search_cond = {
            'sort_by': 'updated',
            'page': 1,
        }
        ds = map(vars, api.dataset_list(**search_cond))
        ds = filter(
            lambda d: d['lastUpdated'] >= datetime.datetime(2023, 1, 1) and d['totalBytes'] > 0,
            ds
        )
        ds = list(ds)
        while len(ds) > 0:
            print('{} {}'.format(['\\', '|', '/', '-'][search_cond['page'] % 4], search_cond['page']), end='\r')
            print('\n'.join(map(lambda d: str(d['totalBytes']), ds)), file=output)
            search_cond = {
                'sort_by': 'updated',
                'page': search_cond['page'] + 1,
            }
            ds = map(vars, api.dataset_list(**search_cond))
            ds = filter(
                lambda d: d['lastUpdated'] >= datetime.datetime(2023, 1, 1) and d['totalBytes'] > 0,
                ds
            )
            ds = list(ds)


if __name__ == '__main__':
    try:
        fire.Fire(main)
    except:
        print(format_exc(), file=sys.stderr)
