import requests

ACCESS_TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"


class User:
    def __init__(self, id) -> None:
        self.id = id
    
    def __str__(self):
        user_url = "https://vk.com/id" + str(self.id)
        return user_url
    
        
    def get_friends(self):
        params = {
            "user_id": self.id,
            "access_token": ACCESS_TOKEN,
            "v": "5.21"
        }
        response = requests.get('https://api.vk.com/method/friends.get', params=params)
        res_json = response.json()
        friends_ids = res_json['response']['items']
        return friends_ids
    
    
    def __and__(self, other):
        m_f = list((set(user1.get_friends()) & set(user2.get_friends())))
        common_friends = [User(i) for i in m_f]
        return common_friends

        # или можно распечатать ссылки общих друзей
        # print('Ссылки на общих друзей:')
        # for i in common_friends:
        #     print(i)







user1 = User()
user2 = User()


common_friends = user1 & user2
print(common_friends)