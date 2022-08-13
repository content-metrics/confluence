import json 
from instagramy import InstagramUser

class Connector: 

    def __init__(self, user_id):
        self.user_id = user_id
        self.page_statistics = None
        self.post_statistics = None
    

    def get_page_statistics(self): 
        """Extract the instagram page statistics."""
        print('get page statistics...')
        user = InstagramUser(self.user_id)
        data = {}
        if user.is_verified:
            print(f'The user is {user.fullname}.') 
            data["biography"] = user.biography
            data["fullname"] = user.fullname
            data["number_of_followers"] = user.number_of_followers
            data["number_of_followings"] = user.number_of_followings
            data["number_of_posts"] = user.number_of_posts
        else: 
            print('The user is unknown.')
        
        self.page_statistics = data
        return data

"""
    def get_posts_statistics(self):
        user = InstagramUser(self.user_id)
        number_of_posts = user.number_of_posts
        data = {}
        while number_of_posts > 0:
            post_number = "post " + str(number_of_posts)



        return number_of_posts 
        
"""


if __name__ == "__main__":
    user_id = 'boobamedia'
    instagram_connection = Connector(user_id)
    print(instagram_connection.get_page_statistics())