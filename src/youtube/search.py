import urllib.request
import re
import os 

base_url = "https://www.youtube.com/"

def get_videos_ids_from_keywords(scope):
    context_url = f"results?search_query={scope}"
    regex_pattern = r"watch\?v=(\S{11})"
    url = os.path.join(base_url, context_url)
    html = urllib.request.urlopen(url)
    video_ids = re.findall(regex_pattern, html.read().decode())
    return video_ids


def get_channel_id_from_video_id(video_id):
    context_url = f"watch?v={video_id}"
    regex_pattern = r"<meta itemprop=\"channelId\" content=\"(.*?)\""
    url = os.path.join(base_url, context_url)
    html = urllib.request.urlopen(url)
    channel_id = re.findall(regex_pattern, html.read().decode())
    return channel_id[0]




def get_channels_ids_from_keywords(scope, video_limit=None):
    """
    args
    ----
    scope: str or list the query string 
    video_limit: integer or None is the max number of videos you want to retry

    return
    ------
    list
    """
    if isinstance(scope, list):
        youtube_default_sep = "+"
        scope = youtube_default_sep.join(scope)
    
    video_ids = get_videos_ids_from_keywords(scope=scope)
    video_ids = video_ids[:video_limit]
    channels_ids = []
    for video_id in video_ids:
        channel_id = get_channel_id_from_video_id(video_id=video_id)
        channels_ids.append(channel_id)
    return channels_ids
