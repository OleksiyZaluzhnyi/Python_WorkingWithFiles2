import csv
import random
from faker import Faker
from datetime import datetime

fake = Faker('uk_UA')

male_patronymics = ["Іванович", "Петрович", "Сергійович", "Олегович", "Андрійович",
                    "Миколайович", "Васильович", "Юрійович", "Романович", "Дмитрович",
                    "Олександрович", "Степанович", "Григорович", "Богданович",
                    "Тарасович", "Леонідович", "Євгенович", "Ігорович", "Максимович", "Вікторович"]

female_patronymics = ["Іванівна", "Петрівна", "Сергіївна", "Олегівна", "Андріївна",
                      "Миколаївна", "Василівна", "Юріївна", "Романівна", "Дмитрівна",
                      "Олександрівна", "Степанівна", "Григорівна", "Богданівна",
                      "Тарасівна", "Леонідівна", "Євгенівна", "Ігорівна", "Максимівна", "Вікторівна"]

def generate_birth_date():
    start = datetime(1946, 1, 1)
    end = datetime(2011, 12, 31)
    return fake.date_between(start, end)

with open(".\Employees\data.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Прізвище", "Ім'я", "По батькові", "Стать", "Дата народження",
                     "Посада", "Місто", "Адреса", "Телефон", "Email"])

    for i in range(500):
        gender = "Ж" if random.random() < 0.4 else "Ч"

        if gender == "Ж":
            last = fake.last_name_female()
            first = fake.first_name_female()
            patronymic = random.choice(female_patronymics)
        else:
            last = fake.last_name_male()
            first = fake.first_name_male()
            patronymic = random.choice(male_patronymics)

        writer.writerow([
            last,
            first,
            patronymic,
            gender,
            generate_birth_date(),
            fake.job(),
            fake.city(),
            fake.address(),
            fake.phone_number(),
            fake.email()
        ])

print("CSV created")