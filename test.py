import random

number = random.randint(1, 10)
print("Я загадал число от 1 до 10. Попробуй угадать!")

guess = int(input("Твой вариант: "))

if guess == number:
    print("🎉 Правильно! Ты угадал!")
else:
    print(f"❌ Неверно. Я загадал {number}.")
