def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
   if len(password) < min_length:
       return False
   has_upper = False
   has_lower = False
   has_digit = False
   for char in password:
       if char.isupper():
           has_upper = True
       if char.islower():
           has_lower = True
       if char.isdigit():
           has_digit = True
   if require_upper and not has_upper:
       return False
   if require_lower and not has_lower:
       return False
   if require_digit and not has_digit:
       return False
   return True