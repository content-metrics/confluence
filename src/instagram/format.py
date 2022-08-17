import pandas as pd 
from connector import Connector
import json

CONFIG_FILE = 'config/properties.json'

def page_stats_from_dict_to_df(user_id, limit=10): 
    with open(CONFIG_FILE) as f:
        properties = json.load(f)
    user_connect = Connector(user_id)
    print(user_connect.get_page_statistics())
    post_data = user_connect.get_posts_statistics(limit)
    df = pd.DataFrame.from_dict(post_data, orient='index',
                                columns=properties['post'][1:])
    return df

