import math
import sys
import fire
from tqdm import tqdm
from traceback import format_exc


UNITS = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')

DIGITS = ('1', '10', '100', '100')

def convert(size):
   if size == 0:
       return '0B'
   i = int(math.floor(math.log(size, 1024)))
   p = math.pow(1024, i)
   s = int(math.floor(math.log(round(size / p), 10)))
   return "{}{}".format(DIGITS[s], UNITS[i])


def write(line, output):
    print(line, file=output)


def main(input='input.txt', output='output.txt'):
    with open(input, 'r') as input, open(output, 'a') as output:
        for l in tqdm(input.readlines()):
            write(convert(int(l)), output)


if __name__ == '__main__':
    try:
        fire.Fire(main)
    except:
        print(format_exc(), file=sys.stderr)
