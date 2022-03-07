
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date, time


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Start programm "MAIN "')
    print(date.today())
    calculate_salary()
    get_employees()


