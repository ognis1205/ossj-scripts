import datetime
import sys
import fire
from traceback import format_exc
from kaggle import api


def progress(page):
    print('{} {}'.format(['\\', '|', '/', '-'][page % 4], page), end='\r')


def by_update_date_and_size(after, inf):
    return lambda d: d['lastUpdated'] >= after and d['totalBytes'] > inf


def write(datasets, output):
    print(
        '\n'.join(map(lambda d: str(d['totalBytes']), datasets)),
        file=output
    )


def main(output='output.txt'):
    query = {
        'sort_by': 'updated',
        'page': 1,
    }

    by_condition = by_update_date_and_size(
        datetime.datetime(2023, 1, 1),
        0,
    )

    with open(output, 'a') as output:
        ds = map(vars, api.dataset_list(**query))
        ds = filter(by_condition, ds)
        ds = list(ds)
        while len(ds) > 0:
            progress(query['page'])
            write(ds, output)
            query['page'] += 1
            ds = map(vars, api.dataset_list(**query))
            ds = filter(by_condition, ds)
            ds = list(ds)


if __name__ == '__main__':
    try:
        fire.Fire(main)
    except:
        print(format_exc(), file=sys.stderr)
