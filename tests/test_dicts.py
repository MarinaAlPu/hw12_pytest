from utils import dicts


def test_get_val(collections_for_test):
    assert dicts.get_val(collections_for_test[0], '2', 'git') == 'два'
    assert dicts.get_val(collections_for_test[1], 'собака', 'git') == 'git'
    assert dicts.get_val(collections_for_test[2], 'собака', 'git') == 'git'
    assert dicts.get_val(collections_for_test[3], '3') == 'три'
    assert dicts.get_val(collections_for_test[4], '5') == 'git'
    assert dicts.get_val(collections_for_test[5], '5') == 'git'
    assert dicts.get_val(collections_for_test[6], '5') == 'git'
