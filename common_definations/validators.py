from django.core.exceptions import ValidationError


def mobile_number_validator(mob_Number: str) -> bool:
    mob_no = f'{mob_Number}'
    not_valid_starter = ["0", 1, 2, 3, 4]
    if(len(mob_no) != 10 or any(map(mob_no.startswith, map(str, not_valid_starter)))):
        raise ValidationError(f"'{mob_no}' is not a valid number!")


def name_validator(name):
    if(not name or not f'{name}'.isalpha()):
        raise ValidationError(f'{name} is not proper name!')
