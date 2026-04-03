import csv
from datetime import datetime
from openpyxl import Workbook

def calculate_age(birth_date):
    today = datetime.today().date()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

try:
    with open(".\Employees\data.csv", encoding='utf-8') as f:
        reader = list(csv.reader(f))
except:
    print("Помилка відкриття CSV")
    exit()

wb = Workbook()
sheets = {
    "all": wb.active,
    "younger_18": wb.create_sheet(),
    "18-45": wb.create_sheet(),
    "45-70": wb.create_sheet(),
    "older_70": wb.create_sheet()
}

sheets["all"].title = "all"

for name, sheet in sheets.items():
    sheet.append(["№", "Прізвище", "Ім'я", "По батькові", "Дата народження", "Вік"])

counter = 1

for row in reader[1:]:
    birth_date = datetime.strptime(row[4], "%Y-%m-%d").date()
    age = calculate_age(birth_date)

    record = [counter, row[0], row[1], row[2], row[4], age]
    sheets["all"].append(record)

    if age < 18:
        sheets["younger_18"].append(record)
    elif age <= 45:
        sheets["18-45"].append(record)
    elif age <= 70:
        sheets["45-70"].append(record)
    else:
        sheets["older_70"].append(record)

    counter += 1

try:
    wb.save(".\Employees\employees.xlsx")
    print("Ok")
except:
    print("Не вдалося створити XLSX")