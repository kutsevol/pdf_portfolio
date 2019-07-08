def convert_value_list_to_str(data):
    return {key: ",".join(value) for key, value in data.items()}
