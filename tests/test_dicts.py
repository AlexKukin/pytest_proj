from utils import dicts


def test_dicts():
    test_dict = {"key1": "value1", "key2": "value2"}

    assert dicts.get_val(test_dict, "key1") == "value1"
    assert dicts.get_val(test_dict, "key2") == "value2"
    assert dicts.get_val(test_dict, "key2", "my_def_value") == "value2"

    assert dicts.get_val(test_dict, "wrong_key") == "git"
    assert dicts.get_val(test_dict, "wrong_key", "my_def_value") == "my_def_value"

    assert dicts.get_val({}, "key1") == "git"
    assert dicts.get_val({}, "key1", "my_def_value") == "my_def_value"

    assert dicts.get_val(test_dict, "wrong_key", None) is None
