import random

def check_guess(secret, guess):
    """Сравнивает догадку с загаданным числом и возвращает подсказку."""
    if guess < secret:
        return "Слишком мало"
    elif guess > secret:
        return "Слишком много"
    else:
        return "Поздравляю! Вы угадали!"

def main():
    secret = random.randint(1, 100)
    attempts = 0  # счётчик попыток
    print("Я загадал число от 1 до 100. Попробуйте угадать!")
    
    while True:
        try:
            guess = int(input("Ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите число.")
            continue
        
        attempts += 1  # увеличиваем счётчик
        result = check_guess(secret, guess)
        print(result)
        
        if result == "Поздравляю! Вы угадали!":
            print(f"Вы справились за {attempts} попыток!")  # итоговое сообщение
            break

if __name__ == "__main__":
    main()