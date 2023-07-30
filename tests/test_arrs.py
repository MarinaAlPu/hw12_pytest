from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 2, "test") == "test"
    assert arrs.get([1, 2, 'abc', 'мир вашему дому', [1, 7], 3], 3) == 'мир вашему дому'
    assert arrs.get(['f', 'b', 5], -1, "test") == "test"
    assert arrs.get([1, 2.56, 'мама'], 93, "test") == "test"
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], -953, "test") == "test"
    assert arrs.get([1, ['g', 5], 13, 3], 1, "test") == ['g', 5]
    assert arrs.get([{'key': 'value'}, 2, 3], 0, "test") == {'key': 'value'}
    assert arrs.get([1, 2, 3], 1) == 2
    assert arrs.get([1, 2, 3], -21) == None
    assert arrs.get([], 13) == None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 'abc', 'мир вашему дому', [1, 7], 3], -4, -1) == ['abc', 'мир вашему дому', [1, 7]]
    assert arrs.my_slice([1, 2.541265, 'а', 'б', 'вгдеё', 3], 0) == [1, 2.541265, 'а', 'б', 'вгдеё', 3]
    assert arrs.my_slice(['f', 'w', 'b'], -2, 4) == ['w', 'b']
    assert arrs.my_slice([1, 2, 3], 0, 0) == []
    assert arrs.my_slice([1, 2, 'fgh', 6, 10.56, 13, 'a'], 0, 5) == [1, 2, 'fgh', 6, 10.56]
    assert arrs.my_slice([1, 'мрвыалэ', 'аааа', 4, 'лес', 7], 0, -3) == [1, 'мрвыалэ', 'аааа']
    assert arrs.my_slice([1, 7, (2, 13, 19732.6525654), 3], 2, -1) == [(2, 13, 19732.6525654)]
    assert arrs.my_slice(['а', 'б', 'вгдеё'], -2, -1) == ['б']
    assert arrs.my_slice([1, 2, 'abc', 'мир вашему дому', [1, 7], 3], -2, -2) == []
    assert arrs.my_slice([1, 2, 'abc', 'мир вашему дому', [1, 7], 3], 3, 3) == []
    assert arrs.my_slice([], 0, 0) == []
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice(['а', 'б', 'вгдеё']) == ['а', 'б', 'вгдеё']
    assert arrs.my_slice([1, 2, 3], -4, 2) == [1, 2]
