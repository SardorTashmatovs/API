# Поиск в интернете:
# Создайте программу, которая позволяет пользователю вводить запрос, а затем отображает результаты поиска из
#  поисковой системы, используя API.

import requests

def google_search():
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'x': x,
    }
    for index, item in enumerate(['items']):
                print(f"{index + 1}. {item['title']}")
                print(f"   {item['link']}")
                print()
    else:
            print("No result")

if __name__ == "__main__":
    sear = input("Введите")
    api_key = "Ваш API"  
    x = "Ww"  

    google_search()