from datetime import datetime, timedelta
import gzip
import os
import pytz
import shutil

import requests

from app.config.db_config import connect_to_database
from app.utils.db_helper import load_data_to_database


HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    ),
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': '*/*',
}

BLOCKCHAIR_URL = (
    'https://gz.blockchair.com/bitcoin/transactions/'
    'blockchair_bitcoin_transactions_{current_date}.tsv.gz'
)
OUTPUT_DIRECTORY = 'Data'


def generate_url_data():
    current_date = (
        datetime.now().date() - timedelta(days=2)
    ).strftime("%Y%m%d")
    return BLOCKCHAIR_URL.format(current_date=current_date)


def download_data():
    url = generate_url_data()
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    load_file_path = os.path.join(OUTPUT_DIRECTORY, os.path.basename(url))
    if os.path.exists(load_file_path):
        print(f"Архив уже загружен: {os.path.basename(load_file_path)}")
        return load_file_path
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(load_file_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        print(f"Архив загружен: {os.path.basename(url)}")
        return load_file_path
    else:
        print(f"Загрузка не удалась. Код ответа: {response.status_code}")
        return None


def extract_data(load_path):
    if load_path is None:
        print("Архив не существует. Невозможно разархивировать.")
        return None
    extract_file_path = os.path.splitext(load_path)[0]
    if os.path.exists(extract_file_path):
        print(f"Файл уже разархивирован: {os.path.basename(extract_file_path)}")
        return None
    with gzip.open(load_path, 'rb') as f_in:
        with open(extract_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Архив успешно разархивирован: {os.path.basename(load_path)}")
    return extract_file_path



if __name__ == "__main__":
    archive_file = download_data()
    extract_file = extract_data(archive_file)
    if extract_file:
        driver = connect_to_database()
        load_data_to_database(driver, extract_file)
