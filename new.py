from datetime import datetime

def calculate_age(birthdate_str):


    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        return None, None # Handle invalid date format

    current_date = datetime.now()

    years = current_date.year - birthdate.year
    if (current_date.month < birthdate.month) or \
       (current_date.month == birthdate.month and current_date.day < birthdate.day):
        years -= 1

    months = (current_date.month - birthdate.month) % 12
    if current_date.month < birthdate.month:
        months = 12 + months
    
    return years, months

# Example Usage:
birthdate_string = "1990-05-15"
years, months = calculate_age(birthdate_string)

if years is not None and months is not None:
    print(f"Age: {years} years, {months} months")
else:
    print("Invalid date format")