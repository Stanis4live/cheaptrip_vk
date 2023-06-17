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
    vk.messages.send(peer_id=user_id, random_id=0, message=message, attachment=attachment)


dir_path = os.path.dirname(os.path.realpath(__file__))
send_massage(user_id=5958128, message='MASSAGE', attachment='cat.jpg', att_path=dir_path, token='vk1.a.GejAv1tQrm4gotI8uRxENm13sEobFKmXHrelkefVpEr-31wzVVqv5bI80I5quXwOFPZLpo2EqMPyviFI4Es4W8hcRzOmLHBwbvdBXLrxOMw7ji36KtNNAzfAb4Catq3EXaxjqNcXmJGIyIV_rBUeCNt15_jcSvaY0F2uADg76sJvOd7y9K_ka_HEAtLmkf4yGrgpYbWmE3anU3xt6gZ1Mg')
# send_massage(user_id=5958128, message='MASSAGE', attachment='cat.jpg', att_path=dir_path, token='vk1.a.5a4y1ziI7O2igeIaKvHSTAjR3FJTv3-dzkYYgdaCK7s1J6sK4FmmZhDpM_lcc8tQ9zGZWbJcoUGKfWlmJ-POxXCtrEnxtIV6PKDPdiaPRucmcdh57BsHqnGTuAQQh4Us_r_V5H4Zz7MOoYPbnd1_i9xgX2BwPMkuN8j-UcUWz7CaDcoE7znYUhvzkUu7ovooJN5xk1Lk2oWKqM8Br3cB7Q')