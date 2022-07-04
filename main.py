

import requests

from pprint import pprint



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type' : 'application/json',
            'Authorization' : 'OAuth {}'.format(self.token)
        }
    def upload(self, file_path):
        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(URL, headers=headers, params=params)
        pprint(response.json())
        return response.json()


    def upload_file_to_disk(self, file_path, filename):
        response_href = self.upload(file_path)
        href = response_href.get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':

    token = 'AQAAAAAO-mTuAADLW71PcQPokU32uhIYKYcMw10'

    filename = 'romanchik.txt'
    file_path = 'romanchik.txt'
    ya = YaUploader(token)
    ya.upload_file_to_disk(file_path=file_path,filename=filename)