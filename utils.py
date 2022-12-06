import re
from typing import Any, Callable


def filter_query(param: str, data: list[str]) -> list[str]:
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: list[str]) -> list[str]:
    col_number = int(param)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(data: list[str], *args: Any, **kwargs: Any) -> list[str]:
    result = []
    for str_ in data:
        if str_ not in result:
            result.append(str_)
    return result


def sort_query(param: str, data: list[str]) -> list[str]:
    reverse = False if param == 'asc' else True
    return list(sorted(data, reverse=reverse))


def limit_query(param: str, data: list[str]) -> list[str]:
    limit = int(param)
    return data[:limit]


def regex_query(param: str, data: list[str]) -> list[str]:
    v: str = re.sub(r'\s', '+', param)
    pattern: re.Pattern = re.compile(v)
    return list(filter(lambda x: re.search(pattern, x), data))


dict_of_utils: dict[str, Callable[..., list[str]]] = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex_query
}
