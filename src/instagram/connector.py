import json 
from instagramy import InstagramUser
from collections import defaultdict
import datetime

class Connector: 

    def __init__(self, user_id):
        self.user_id = user_id
        self.page_statistics = None
        self.posts_statistics = None
    

    def get_page_statistics(self): 
        """Extract the instagram page statistics."""
        print('get page statistics...')
        user = InstagramUser(self.user_id, from_cache=True)
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


    def get_posts_statistics(self, limit=10):
        user = InstagramUser(self.user_id, from_cache=True)
        number_of_posts = user.number_of_posts
        posts = user.posts
        data = defaultdict(list)
        for j in range(limit):
            post_id = user.posts[j][6]
            data[post_id] = []
            data[post_id].append(user.posts[j][0])  # likes
            data[post_id].append(user.posts[j][1])  # comments 
            data[post_id].append(user.posts[j][3])  # is_video
            data[post_id].append(user.posts[j][10]) # post_time

        self.posts_statistics = data 
        return data        



if __name__ == "__main__":
    user_id = 'justinbieber'
    instagram_connection = Connector(user_id)
    print(instagram_connection.get_page_statistics())
    print("**" * 10)
    print(instagram_connection.get_posts_statistics())