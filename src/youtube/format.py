import pandas as pd
from config import config

def channel_stats_from_json_to_df(json_file):
    import json
    with open(json_file) as f:
        data =  json.load(f)
    records = []
    for channel_id, channel_info in data.items():
        channel_views = channel_info['channel_statistics']["viewCount"]
        channel_suscribers = channel_info['channel_statistics']["subscriberCount"]
        channel_videos = channel_info['channel_statistics']["videoCount"]

        videos = channel_info["video_data"]
        for video_id, video_info in videos.items():
            video_hash = video_id
            publish_at = video_info["publishedAt"]
            video_title = video_info["title"]
            video_description = video_info["description"]
            channel_title = video_info["channelTitle"]
            video_tags = video_info.get("tags")
            video_lang = video_info.get("defaultAudioLanguage")
            video_views = video_info["viewCount"]
            video_likes = video_info.get("likeCount", None)
            video_comments = video_info["commentCount"]
            video_duration = video_info["duration"]

            properties_values = (
                    channel_id,
                    channel_views,
                    channel_suscribers,
                    channel_videos,
                    video_hash,
                    publish_at,
                    video_title,
                    video_description,
                    channel_title,
                    video_tags,
                    video_lang,
                    video_views,
                    video_likes,
                    video_comments,
                    video_duration
                )
            properties = config.get('properties')
            new_row = dict(zip(properties, properties_values))
            records.append(new_row)

    temp_df = pd.DataFrame.from_records(records)
    return temp_df