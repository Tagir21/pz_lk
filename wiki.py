import requests


def search_wikipedia(query):
    """Поиск статьи по запросу и возврат информации о ней."""
    url = "https://ru.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "utf8": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['query']['search']


def get_page_content(title):
    """Получение содержимого страницы по заголовку."""
    url = "https://ru.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": title,
        "prop": "text|sections",
        "format": "json",
        "utf8": 1
    }
    response = requests.get(url, params=params)
    return response.json()


def display_paragraphs(content):
    """Вывод параграфов из содержимого страницы."""
    print("\nПараграфы статьи:")
    for section in content['parse']['sections']:
        print(f"\n{section['line']}\n{content['parse']['text'][section['index']]}\n")


def main():
    while True:
        query = input("Введите запрос для поиска в Википедии: ")

        search_results = search_wikipedia(query)

        if not search_results:
            print("Статья не найдена.")
            continue

        print("\nРезультаты поиска:")
        for i, result in enumerate(search_results):
            print(f"{i + 1}. {result['title']}")

        choice = int(input("Выберите номер статьи для просмотра (или 0 для выхода): "))

        if choice == 0:
            break

        selected_title = search_results[choice - 1]['title']

        # Получаем содержимое выбранной статьи
        content = get_page_content(selected_title)

        if 'error' in content:
            print("Ошибка при получении содержимого статьи.")
            continue

        while True:
            # 3. Предлагаем пользователю три варианта действий
            print(f"\nСтатья: {selected_title}\n")
            print(content['parse']['text']['*'][:500])  # Показываем первые 500 символов статьи

            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")

            action_choice = input("Ваш выбор (1/2/3): ")

            if action_choice == "1":
                display_paragraphs(content)

            elif action_choice == "2":
                # Получаем связанные страницы
                linked_pages = content['parse']['sections']
                print("\nСвязанные страницы:")
                for i, section in enumerate(linked_pages):
                    print(f"{i + 1}. {section['line']}")

                linked_choice = int(input("Выберите номер связанной страницы (или 0 для возврата): "))
                if linked_choice == 0:
                    continue

                linked_title = linked_pages[linked_choice - 1]['line']
                content = get_page_content(linked_title)
                selected_title = linked_title

            elif action_choice == "3":
                print("Выход из программы.")
                return

            else:
                print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()