import requests
import json
import os
import sys
import progressbar as pb
import urllib.request
from datetime import datetime

class VK:
    def __init__(self, access_token, user_id, screen_name, version='5.131'):
        self.token = access_token
        if user_id == '' and screen_name != '':
            self.id = screen_name
        else:
            self.id = user_id 
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):            

        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        self.id = response.json()['response'][0]['id']
        return response.json()
    
    def download_from_vk(self, ya, photo_count):

        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': 'profile', 'extended': 1, 'count': 1000}
        response = requests.get(url, params={**self.params, **params})
        
        if photo_count >= response.json()['response']['count']:
            photo_count = response.json()['response']['count']

        bar = pb.ProgressBar(max_value = photo_count)
        list = []
        list_count = []
        num = 0
        
        for rep in response.json()['response']['items']:            
            if num < photo_count:
                result = {}
                if rep["likes"]["count"] in list_count:
                    temp_date = datetime.utcfromtimestamp(rep["date"]).strftime('%Y%m%d')
                    result['file_name'] = f'{rep["likes"]["count"]}-{temp_date}.jpg'
                else:
                    result['file_name'] = f'{rep["likes"]["count"]}.jpg'
                    list_count.append(rep["likes"]["count"])
                
                result['size'] = 'z'
                list.append(result)
                num += 1
                ya.upload_file_to_disk(result['file_name'], rep["sizes"][-1]["url"])
                bar.update(num)
            else:            
                json_data = json.dumps(list)
                ya.save_json(list)
                return json_data