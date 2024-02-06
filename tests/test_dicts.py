import pytest
from utils import dicts


@pytest.mark.parametrize('collection, key, default, expected', [
    ({"key1": "value1", "key2": "value2"}, "key1", "git", "value1"),
    ({"key1": "value1", "key2": "value2"}, "key2", "git", "value2"),
    ({"key1": "value1", "key2": "value2"}, "key2", "git", "value2"),
    ({"key1": "value1", "key2": "value2"}, "wrong_key", "git", "git"),
    ({"key1": "value1", "key2": "value2"}, "wrong_key", "my_def_value", "my_def_value"),
    ({}, "key1", "git", "git"),
    ({}, "key1", "my_def_value", "my_def_value"),
    ({"key1": "value1", "key2": "value2"}, "wrong_key", None, None)
])
def test_dict(collection, key, default, expected):
    assert dicts.get_val(collection, key, default) == expected

