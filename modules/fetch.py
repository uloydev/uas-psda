import requests


class Fetch:
    
    @staticmethod
    def all_data():
        result = requests.get('https://api.kawalcorona.com/indonesia/provinsi')
        return result.json()


