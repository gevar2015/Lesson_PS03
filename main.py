from bs4 import BeautifulSoup
import requests
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Функция перевода слов и описаний
def translate_to_russian(text):
    translator = Translator()
    translation = translator.translate(text, dest='ru')
    return translation.text

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        if word_dict is None:
            print("Не удалось получить слово. Попробуйте снова.")
            continue

        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и описание на русский
        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(word_definition)

        # Начинаем игру
        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ")
        if user.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()
