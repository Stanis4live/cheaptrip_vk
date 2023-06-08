import requests

from project.Api.api_vk_data import ApiData


class VkApiMethods:

    def __init__(self, api_url, token,
                 api_version, user_id=None, domain=None):
        self.api_url = api_url
        self.token = token
        self.api_version = api_version
        self.user_id = user_id
        self.domain = domain

    # здесь и нужен домен, смысл не понятен
    def post_on_own_wall(self, text, owner_id=None, pic_id=None):
        resp_post = requests.post(self.api_url + ApiData.POST_ON_WALL,
                                  params={
                                      "access_token": self.token,
                                      "v": self.api_version,
                                      "domain": self.domain,
                                      "message": text,
                                      "attachments": f'photo{owner_id}_{pic_id}'
                                     }
                                  ).json()
        return resp_post["response"]["post_id"]

    # тоже постит на своей странице
    def post_on_wall(self, text, owner_id, user_id, publish_date=None, pic_id=None):
        resp_post = requests.post(self.api_url + ApiData.POST_ON_WALL,
                                  params={
                                      "access_token": self.token,
                                      "owner_id": owner_id,
                                      "message": text,
                                      "publish_date": publish_date,
                                      "attachments": f'photo{user_id}_{pic_id}',
                                      "v": self.api_version,
                                     }
                                  ).json()
        print(resp_post)
        # return resp_post["response"]["post_id"]

    def get_upload_url(self):
        resp_url = requests.post(self.api_url + ApiData.PIC_UPLOAD_ON_SERVER,
                                 params={
                                     "access_token": self.token,
                                     "v": self.api_version,
                                 }
                                 ).json()
        return resp_url["response"]["upload_url"]


    @staticmethod
    def send_pic_to_url(upload_url, image_path):
        file = {"file1": open(f"{image_path}", "rb")}
        response_photo = requests.post(upload_url, files=file).json()
        return (response_photo["photo"],
                response_photo["server"],
                response_photo["hash"])

    def save_photo_before_post(self, photo, server, photo_hash):
        save_photo = requests.post(self.api_url + ApiData.PIC_SAVE_BEFORE_POST,
                                   params={
                                       "access_token": self.token,
                                       "v": self.api_version,
                                       "user_id": self.user_id,
                                       "photo": photo,
                                       "server": server,
                                       "hash": photo_hash
                                     }
                                   ).json()
        return (save_photo["response"][0]["owner_id"],
                save_photo["response"][0]["id"],
                save_photo["response"][0]["sizes"][5]["url"])
