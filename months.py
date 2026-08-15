# Program to display all month names

import calendar 

def print_month_names():
    """Prints all month names from January to December."""
    print("List of all months:")
    for month_num in range(0, 13):  
        print(f"{month_num}: {calendar.month_name[month_num]}")

if __name__ == "__main__":
    try:
        print_month_names()
    except Exception as e:
        print(f"An error occurred: {e}")
