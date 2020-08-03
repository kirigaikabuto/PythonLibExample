def str_check(s):
    if len(s) < 6 or len(s) > 12:
        return False
    if s.isalnum():
        return True
    return False
