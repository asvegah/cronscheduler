import sys
import select

from timecalc import validate_format
from cronparser import parse_input, next_crontab_time 

def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError

        if not select.select([sys.stdin, ], [], [], 0.0)[0]:
            raise IndexError

        current_time = sys.argv[1]
        validated_time = validate_format(current_time)

        if validated_time:
            crontab = parse_input(sys.stdin)
            return next_crontab_time(validated_time, crontab)

    except IndexError:
        if len(sys.argv) != 2:
            print('''
            ❗️ Error: Please input a single argument in current time format as HH:MM❗️
            
            Example command line 👇

            ​./scheduler.py 16:10 < config

            ''')
        else:
            print('''
            ❗️ Error: Please provide standard input ❗️

            Your command line input should follow the following format to provide STDIN:
            ​./application.py HH:MM < config

            Example command line 👇

            ​./scheduler.py 16:10 < config

            ''')

if __name__ == '__main__':
    main()