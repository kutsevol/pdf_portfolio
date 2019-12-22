def convert_value_list_to_str(data):
    """
    Function to convert dict value from list to str.

    :param data: dict with values as list (e.g. {"key1": ["value1", "value2"]})
    :return: dict with values as str with comma separate
    (e.g. {"key1": "value1,value2"})
    """
    return {key: ",".join(value) for key, value in data.items()}
