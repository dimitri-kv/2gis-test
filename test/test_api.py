import pytest


@pytest.mark.parametrize("q, result", [
    ('Новосибирск', 'Новосибирск'),
    ('рск', 'рск')
])
def test_search_positive(request_to_api_get_params, q, result):
    payload = {'q': q}
    result = request_to_api_get_params(payload).json()
    print(result)
    for res in result["items"]:
        assert q in res["name"]


@pytest.mark.parametrize("q", [
    '',
    'q',
    '1',
    1,

    0,
    '-1'
])
def test_search_negative_low(request_to_api_get_params, q):
    payload = {'q': q}
    result = request_to_api_get_params(payload).json()
    print(result)
    assert result["error"]["message"] == "Параметр 'q' должен быть не менее 3 символов"


@pytest.mark.parametrize("q", [
    '000',
    '%2F',
    '%2F%2F%2F'
])
def test_search_negative_not_found(request_to_api_get_params, q):
    payload = {'q': q}
    result = request_to_api_get_params(payload).json()
    print(result)
    assert result["items"] == []


def test_search_negative_big(request_to_api_get_params):
    payload = {'q': 'vepq;conjcfweohnqohn[rqfohn[rqfohn[u2fo[o[q[uo12gu4c21[rty49cvbbpowcfpibqnmn12xdm21pdrybo7dt78'}
    result = request_to_api_get_params(payload).json()
    print(result)
    assert result["error"]["message"] == "Параметр 'q' должен быть не более 30 символов"


@pytest.mark.parametrize("country_code", [
    'ru',
    'kg',
    'kz',
    'cz',
    'ua'
])
def test_country_code_positive(request_to_api_get_params, country_code):
    payload = {'country_code': country_code}
    result = request_to_api_get_params(payload).json()
    print(result)
    for res in result["items"]:
        assert res["country"]["code"] == country_code


@pytest.mark.parametrize("country_code", [
    'asdflb',
    0,
    -1
])
def test_country_code_negative(request_to_api_get_params, country_code):
    payload = {'country_code': country_code}
    print(payload)
    result = request_to_api_get_params(payload).json()
    print(result)
    assert result["error"]["message"] == "Параметр 'country_code' может быть одним из следующих значений: ru, kg, kz, cz"


@pytest.mark.parametrize("page_size", [
    5,
    10,
    15
])
def test_result_grouping_page_and_count(request_to_api_get_params, page_size):
    """test for page_size + page number params"""
    payload = {'page': 1, 'page_size': page_size}
    res = request_to_api_get_params(payload).json()
    items = res["items"]
    print(items)
    for i in range(2, 8):
        payload = {'page': i, 'page_size': page_size}
        result = request_to_api_get_params(payload).json()
        if len(result["items"]) > 0:
            print(result["items"])
            print(result["items"][0])
            print(items[-1])
            assert result["items"][0] != items[-1]
        items.append(result["items"])
    print(items)


@pytest.mark.parametrize("country_code", [
    'ru',
    'kg',
    'kz',
    'cz',
    'ua'
])
@pytest.mark.parametrize("q, result", [
    ('Новосибирск', 'Новосибирск'),
    ('рск', 'рск')
])
def test_search_with_country_code(request_to_api_get_params, q, country_code, result):
    payload = {'q': q, 'country_code': country_code}
    result = request_to_api_get_params(payload).json()
    print(result)
    for res in result["items"]:
        assert q in res["name"]