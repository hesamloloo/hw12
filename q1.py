import requests
import logging

# تنظیم logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# آدرس پایه API
BASE_URL = "https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api"

def get_movies():
    """ارسال درخواست GET برای بازیابی لیست فیلم‌ها"""
    try:
        logging.info("Sending GET request to retrieve movie list.")
        response = requests.get(f"{BASE_URL}/movies")
        response.raise_for_status()  # بررسی وضعیت پاسخ
        movies = response.json()
        logging.info("Successfully retrieved movie list.")

        print("\nList of Movies:")
        for movie in movies:
            # بررسی وجود کلیدهای title و year در داده‌های دریافتی
            title = movie.get('title', 'Unknown Title')
            year = movie.get('year', 'Unknown Year')
            print(f"- {title} ({year})")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error while retrieving movies: {e}")
        print("Failed to retrieve movie list.")

def add_movie(predefined_inputs=None):
    """دریافت اطلاعات فیلم از کاربر و ارسال درخواست POST برای افزودن فیلم جدید"""
    try:
        # دریافت جزئیات فیلم از ورودی از پیش تعریف شده یا شبیه‌سازی شده
        if predefined_inputs:
            title, year, genre = predefined_inputs
        else:
            title = input("Enter movie title: ")
            year = input("Enter movie year: ")
            genre = input("Enter movie genre: ")

        new_movie = {
            "title": title,
            "year": year,
            "genre": genre
        }

        logging.info("Sending POST request to add a new movie.")
        response = requests.post(f"{BASE_URL}/movies", json=new_movie)
        response.raise_for_status()  # بررسی وضعیت پاسخ

        if response.status_code == 201:
            logging.info("Movie successfully added.")
            print("Movie successfully added to the system!")
        else:
            logging.warning("Unexpected status code received.")
            print("Failed to add the movie. Please try again.")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error while adding a new movie: {e}")
        print("Failed to add the movie.")

def main():
    while True:
        print("\nOptions:")
        print("1. Retrieve list of movies")
        print("2. Add a new movie")
        print("3. Exit")

        choice = input("Please choose an option (1/2/3): ")

        if choice == "1":
            get_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    predefined_inputs = None  # برای استفاده از مقادیر ورودی واقعی کاربر، این را تغییر ندهید
    main()

