import urllib.request
import re
import os 

base_url = "https://www.youtube.com/"

def get_videos_ids_from_keywords(scope):
    context_url = f"results?search_query={scope}"
    url = os.path.join(base_url, context_url)
    html = urllib.request.urlopen(url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return video_ids


def get_channel_id_from_video_id(video_id):
    context_url = f"watch?v={video_id}"
    url = os.path.join(base_url, context_url)
    html = urllib.request.urlopen(url)
    channel_id = re.findall(r"<meta itemprop=\"channelId\" content=\"(.*?)\"", html.read().decode())
    return channel_id[0]




def get_channels_ids_from_keywords(scope, video_limit=None):
    if isinstance(scope, list):
        youtube_default_sep = "+"
        scope = youtube_default_sep.join(scope)
    # video_limit is the max video you want to retry
    video_ids = get_videos_ids_from_keywords(scope=scope)
    video_ids = video_ids[:video_limit]
    channels_ids = []
    for video_id in video_ids:
        channel_id = get_channel_id_from_video_id(video_id=video_id)
        channels_ids.append(channel_id)
    return channels_ids



