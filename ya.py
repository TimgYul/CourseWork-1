import requests
import json
from pprint import pprint

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        } 
    
    def create_folder(self):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': 'photos_vk', 'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)
        

    def upload_file_to_disk(self, filename, url):
        self.create_folder()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": f'photos_vk/{filename}', "url": url, "overwrite": "true"}
        #response = requests.get(upload_url, headers=headers, params=params)
        #href = response.json().get('href')

        response = requests.post(upload_url, params=params, headers=headers ) # data=open(filename, 'rb'))

    def save_json_local(self,json_data):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

    def save_json(self, data_js):
        self.save_json_local(data_js)
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()

        params = {"path": f'photos_vk/data.json', "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href')

        response = requests.put(href, data=open('data.json', 'rb'))

 