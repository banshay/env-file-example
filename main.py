# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dotenv import load_dotenv
import os

load_dotenv()

NOT_SECRET_API_KEY = "Sadge"

API_KEY = os.getenv("API_KEY")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(API_KEY)
    print(NOT_SECRET_API_KEY)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
