import sys
import select

from time import validate_format 

def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError

        if not select.select([sys.stdin, ], [], [], 0.0)[0]:
            raise IndexError

        current_time = sys.argv[1]
        validated_time = validate_format(current_time)

        if validated_time:
            crontab_list = parse_config(sys.stdin)
            return next_crontab_time(validated_current_time, crontab_list)

    except IndexError:
        if len(sys.argv) != 2:
            print('''
            ❗️ Error: Please input a single argument in current time format as HH:MM❗️
            
            Example command line 👇

            ​./app.py 16:10 < config

            ''')
        else:
            print('''
            ❗️ Error: Please provide standard input ❗️

            Your command line input should follow the following format to provide STDIN:
            ​./application.py HH:MM < config

            Example command line 👇

            ​./app.py 16:10 < config

            ''')