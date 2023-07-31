from utils import dicts


def test_get_val():
    assert dicts.get_val({'1': 'один', '2': 'два', '3': 'три'}, '2', 'git') == 'два'
    assert dicts.get_val({'1': 'один', '2': 'два', '3': 'три'}, 'собака', 'git') == 'git'
    assert dicts.get_val({}, 'собака', 'git') == 'git'
    assert dicts.get_val({'1': 'один', '2': 'два', '3': 'три'}, '3') == 'три'
    assert dicts.get_val({'1': 'один', '2': 'два', '3': 'три'}, '5') == 'git'
