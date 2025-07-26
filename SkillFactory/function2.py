def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
    if len(password) < min_length:
        return False

    if require_upper and not any(char.isupper() for char in password):
        return False

    if require_lower and not any(char.islower() for char in password):
        return False

    if require_digit and not any(char.isdigit() for char in password):
        return False

    return True