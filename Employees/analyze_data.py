import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.csv"

CATEGORY_LABELS = {
    "younger_18": "До 18",
    "18-45": "18-45",
    "45-70": "45-70",
    "older_70": "Понад 70",
}


def calculate_age(birth_date):
    today = datetime.today().date()
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )


def empty_categories():
    return {key: 0 for key in CATEGORY_LABELS}


try:
    with DATA_FILE.open(encoding="utf-8") as file:
        reader = list(csv.reader(file))
except OSError:
    print("Помилка відкриття CSV")
    raise SystemExit(1)

all_categories = empty_categories()
male_categories = empty_categories()
female_categories = empty_categories()
male_total = 0
female_total = 0

for row in reader[1:]:
    gender = row[3].strip()
    birth_date = datetime.strptime(row[4], "%Y-%m-%d").date()
    age = calculate_age(birth_date)

    if age < 18:
        category = "younger_18"
    elif age <= 45:
        category = "18-45"
    elif age <= 70:
        category = "45-70"
    else:
        category = "older_70"

    all_categories[category] += 1

    if gender == "Ч":
        male_categories[category] += 1
        male_total += 1
    elif gender == "Ж":
        female_categories[category] += 1
        female_total += 1


print("Кількість співробітників за віковими категоріями:")
for key, label in CATEGORY_LABELS.items():
    print(f"{label}: {all_categories[key]}")

print("\nКількість співробітників кожної статі за віковими категоріями:")
for key, label in CATEGORY_LABELS.items():
    print(
        f"{label}: чоловіки - {male_categories[key]}, "
        f"жінки - {female_categories[key]}"
    )

print("\nЗагальна кількість співробітників за статтю:")
print(f"Чоловіки: {male_total}")
print(f"Жінки: {female_total}")

labels = list(CATEGORY_LABELS.values())
all_values = [all_categories[key] for key in CATEGORY_LABELS]
male_values = [male_categories[key] for key in CATEGORY_LABELS]
female_values = [female_categories[key] for key in CATEGORY_LABELS]
x_positions = range(len(labels))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(labels, all_values, color="steelblue")
plt.title("Кількість співробітників за віковими категоріями")
plt.xlabel("Вікова категорія")
plt.ylabel("Кількість співробітників")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
plt.bar(
    [position - bar_width / 2 for position in x_positions],
    male_values,
    width=bar_width,
    label="Чоловіки",
    color="cornflowerblue",
)
plt.bar(
    [position + bar_width / 2 for position in x_positions],
    female_values,
    width=bar_width,
    label="Жінки",
    color="lightcoral",
)
plt.xticks(list(x_positions), labels)
plt.title("Кількість чоловіків і жінок у кожній віковій категорії")
plt.xlabel("Вікова категорія")
plt.ylabel("Кількість співробітників")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
plt.bar(["Чоловіки", "Жінки"], [male_total, female_total], color=["cornflowerblue", "lightcoral"])
plt.title("Загальна кількість чоловіків і жінок")
plt.ylabel("Кількість співробітників")
plt.tight_layout()
plt.show()
