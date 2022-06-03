import sys
from minmax import minmax
from list import list_notes

help_message = 'You should use this app in 2 ways:\n' \
               'python currency.py minmax RUB 01.06.2022 02.06.2022\n' \
               'python currency.py list RUB 15.05.2022 02.06.2022 --limit=3'

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'minmax':
        minmax(sys.argv[2:])
    elif mode == 'list':
        list_notes(sys.argv[2:])
    else:
        print(help_message)
