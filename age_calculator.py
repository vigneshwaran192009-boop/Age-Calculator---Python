from datetime import date, datetime
import calendar


def add_months(original_date, number_of_months):
    """Add calendar months, using the last day if the target month is shorter."""
    month_index = original_date.month - 1 + number_of_months
    year = original_date.year + month_index // 12
    month = month_index % 12 + 1
    last_day = calendar.monthrange(year, month)[1]
    day = min(original_date.day, last_day)
    return date(year, month, day)


def get_age(birth_date, today=None):
    """Return exact age as (years, months, days)."""
    if today is None:
        today = date.today()

    if birth_date > today:
        raise ValueError("Date of birth cannot be in the future.")

    years = today.year - birth_date.year
    try:
        anniversary = birth_date.replace(year=today.year)
    except ValueError:
        # Treat February 29 as February 28 in non-leap years.
        anniversary = date(today.year, 2, 28)

    if today < anniversary:
        years -= 1

    last_birthday = add_months(birth_date, years * 12)

    months = (today.year - last_birthday.year) * 12
    months += today.month - last_birthday.month

    month_date = add_months(last_birthday, months)
    if month_date > today:
        months -= 1
        month_date = add_months(last_birthday, months)

    days = (today - month_date).days
    return years, months, days


def main():
    print("=" * 36)
    print("          AGE CALCULATOR")
    print("=" * 36)
    print("Enter your date of birth (DD-MM-YYYY).")

    dob_text = input("Date of birth: ").strip()

    try:
        birth_date = datetime.strptime(dob_text, "%d-%m-%Y").date()
        years, months, days = get_age(birth_date)

        print("\nYour exact age is:")
        print(f"{years} years, {months} months, and {days} days.")
    except ValueError as error:
        print(f"Invalid input: {error}")
        print("Please enter a valid date in DD-MM-YYYY format.")


if __name__ == "__main__":
    main()
