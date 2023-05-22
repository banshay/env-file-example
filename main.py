from dotenv import load_dotenv
import os

load_dotenv()

NOT_SECRET_API_KEY = "Sadge"

API_KEY = os.getenv("API_KEY")


if __name__ == '__main__':
    print(API_KEY)
    print(NOT_SECRET_API_KEY)

