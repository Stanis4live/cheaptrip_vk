import vk_api


def repost(token, owner_id, item_id, message=None):
    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    obj = f'wall{owner_id}_{item_id}'
    vk.wall.repost(object=obj, message=message)
    # vk.wall.repost(object=owner_id+'_'+item_id, message=message)
    # vk.wall.repost(object='wall-56877160_78', message=message)


# Пример использования:
owner_id = '-56877160'  # Идентификатор владельца записи
item_id = '77'  # Идентификатор записи
repost(owner_id=owner_id, item_id=item_id, message='Репост!', token='vk1.a.GejAv1tQrm4gotI8uRxENm13sEobFKmXHrelkefVpEr-31wzVVqv5bI80I5quXwOFPZLpo2EqMPyviFI4Es4W8hcRzOmLHBwbvdBXLrxOMw7ji36KtNNAzfAb4Catq3EXaxjqNcXmJGIyIV_rBUeCNt15_jcSvaY0F2uADg76sJvOd7y9K_ka_HEAtLmkf4yGrgpYbWmE3anU3xt6gZ1Mg')

