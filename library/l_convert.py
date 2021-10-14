def do(lists):
    if len(lists) == 0:
        return list()
    else:
        result = list()
        for row in lists:
            part = {row[0]: row[1]}
            result.append(part)
        return result


def convert_dict(lists):
    if len(lists) == 0:
        return list()
    else:
        result = list()
        for row in lists:
            result.append(dict(row))
        return result
