from datetime import datetime


def key_function(entry):
    date_string, time_string, _, _ = entry
    datetime_object = datetime.strptime(
        f'{date_string} {time_string}', '%Y-%m-%d %H:%M')
    return datetime_object


def extractErrorLogs(logs):
    # Write your code here
    res = []
    for log in logs:
        if log[2] == 'CRITICAL' or log[2] == 'ERROR':
            res.append(log)
    sorted_data = sorted(res, key=key_function)
    return sorted_data
