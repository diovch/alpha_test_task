import sys
from minmax import console_minmax
from list import console_list_notes

help_message = 'You should use this app in 2 ways:\n' \
               'python currency.py minmax RUB 10.05.2022 02.06.2022\n' \
               'python currency.py list RUB 15.05.2022 02.06.2022 --limit=3'

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'minmax':
        console_minmax(sys.argv[2:])
    elif mode == 'list':
        console_list_notes(sys.argv[2:])
    else:
        print(help_message)
