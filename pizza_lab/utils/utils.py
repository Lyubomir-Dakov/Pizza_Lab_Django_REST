def str_to_bool(value):
    if value.lower() == 'true':
        return True
    elif value.lower() in 'false':
        return False
    else:
        raise ValueError(f"Cannot convert {value} to boolean.")