import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, files_list: list):
        """Метод загружает файлы по списку files_list на яндекс диск"""
        for file in files_list:
            url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            params = {"path": "/" + file}
            headers = {"Authorization": token}
            response = requests.get(url, params=params, headers=headers).json()
            upload_url = response["href"]
            with open(file, "rb") as f:
                resp = requests.put(upload_url, files={"file": f})
                print(resp.status_code)     # проверочный принт


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    files_list = ["car1.jpeg", "car2.jpeg"]
    token = open("token.txt").read()
    uploader = YaUploader(token)
    result = uploader.upload(files_list)
