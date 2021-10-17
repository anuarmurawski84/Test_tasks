import pytest


class Browser:
    def set_int(self, int_value):
        print(int_value)


class Browser1(Browser):
    def __init__(self):
        self.name = 'explovet'


class Browser2(Browser):
    def __init__(self):
        self.name = 'firefox'


class Browser3(Browser):
    def __init__(self):
        self.name = 'chrome'


browsers_dict = {
    'browser1': Browser1,
    'browser2': Browser2,
    'browser3': Browser3
}


tests_values = {
    'ok':  # ожидаемое сообщение
    [1, 2, 3],  # значения, при которых получаем сообщение “ok”
    'not ok':  # ожидаемое сообщение
    ['bad1', 'bad2', 'bad3']  # значения, при которых получаем сообщение “not ok”
}

def create_test_data_from_test_values():
    for k in tests_values.keys():
        for v in tests_values[k]:
            yield k, v

def get_ids(val):
    return f'browser: "{val[0]}"'

def get_ids_2(val):
    return f'exp_msg: "{val[0]}", value: "{val[1]}"'

@pytest.mark.parametrize(
    argnames="browser_params",
    argvalues=browsers_dict.items(),
    ids=get_ids
)
@pytest.mark.parametrize(
    argnames="values",
    argvalues=create_test_data_from_test_values(),
    ids=get_ids_2
)
def test_1(browser_params, values):
    browsers_name = browser_params[0]
    browsers_instance = browser_params[1]

    exp_msg = values[0]
    value = values[1]

    print(f'exp_msg: "{exp_msg}", value: "{value}" - browser: "{browsers_name}"')

