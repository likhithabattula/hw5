
def is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def ordinal_date(year: int, month: int, day: int) -> int:
    days_in_month = [0, 31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ordinal = sum(days_in_month[:month]) + day
    return ordinal