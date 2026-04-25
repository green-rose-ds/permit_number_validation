def permit_number_format(permit_number: str):
    if not permit_number:
        return False
    if len(permit_number) != 8:
        return False
    if not (permit_number[0:1].isalpha() and
        permit_number[2:6].isdigit() and
        permit_number[6:7].isalpha()):
        return False
    return True 