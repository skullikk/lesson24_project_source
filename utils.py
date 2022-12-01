def filter_query(value, data):
    return list(filter(lambda x: value in x, data))


def map_query(value, data):
    col_number = int(value)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(value, data):
    result = []
    for str_ in data:
        if str_ not in result:
            result.append(str_)
    return result


def sort_query(value, data):
    reverse = False if value == 'asc' else True
    return list(sorted(data, reverse=reverse))


def limit_query(value, data):
    limit = int(value)
    return data[:limit]


dict_of_utils = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query
}
