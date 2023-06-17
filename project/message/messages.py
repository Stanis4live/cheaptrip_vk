import os
import vk_api


def upload_photo(att_path, photo, session):
    file_path = os.path.join(att_path + '/' + photo)
    upload = vk_api.VkUpload(session)
    photo = upload.photo_messages(file_path)
    photo_data = photo[0]
    owner_id = photo_data['owner_id']
    photo_id = photo_data['id']
    access_key = photo_data['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment


def send_massage(token, user_id, message=None, attachment=None, att_path=None):
    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    if attachment is not None:
        attachment = upload_photo(att_path=att_path, photo=attachment, session=session)
    vk.messages.send(user_id=user_id, random_id=0, message=message, attachment=attachment)


