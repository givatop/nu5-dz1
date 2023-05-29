import os
import time
import random

from file_manager import get_files, get_folders


TEST_FILE = f"test.test{random.randint(100500, 200500)}"
TEST_FOLDER = f"test_folder{random.randint(100500, 200500)}"


def test_get_files():
    """ Тест функции get_files с помощью создания файл/папки и её поиска
    в списке, который возвращает функция"""

    with open(TEST_FILE, 'w'): pass
    os.mkdir(TEST_FOLDER)

    time.sleep(1)

    files = get_files(os.getcwd())

    try:
        assert TEST_FILE in files
        assert TEST_FOLDER not in files
    finally:
        os.remove(TEST_FILE)
        os.rmdir(TEST_FOLDER)


def test_get_folders():
    """ Тест функции get_files с помощью создания файл/папки и её поиска
    в списке, который возвращает функция"""

    with open(TEST_FILE, 'w'): pass
    os.mkdir(TEST_FOLDER)

    time.sleep(1)

    folders = get_folders(os.getcwd())

    try:
        assert TEST_FILE not in folders
        assert TEST_FOLDER in folders
    finally:
        os.remove(TEST_FILE)
        os.rmdir(TEST_FOLDER)

