from time import validate_hour_min, calculate_difference


def parse_input(file):
    crontab = []
    for line in file:
        crontab.append(line.strip('\n').split(' '))

    return crontab


def next_crontab_time(current_time, crontab):
        for line in crontab:
            crontab_hour = line[1]
            crontab_minute = line[0]
            crontab_command = line[2]
            crontab_validated_time = crontab_validator(
                [crontab_minute, crontab_hour])
            if crontab_validated_time:
                result = calculate_difference(
                    crontab_validated_time, current_time)
                print(f'{result} - {crontab_command}')


def crontab_validator(crontab):
    try:
        # * validate crontab time

        for time_value in crontab:
            if not time_value == '*' and not time_value.isdigit():
                raise ValueError

        crontab_hour = crontab[1]
        crontab_minute = crontab[0]

        # * validate crontab time in digits
        if crontab_hour.isdigit() and crontab_minute.isdigit():
            validate_hour_min(int(crontab_hour), int(crontab_minute))

        elif crontab_hour.isdigit():
            validate_hour_min(int(crontab_hour), 0)

        elif crontab_minute.isdigit():
            validate_hour_min(0, int(crontab_minute))

        else:
            pass

        return {'hour': crontab_hour, 'minute': crontab_minute}

    except:
        print('❗️ Incorrect time format in config file ❗️')