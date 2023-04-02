from googleapiclient.discovery import build
import pandas as pd
from IPython.display import JSON

api_key = 'AIzaSyDUwAjfu38TehA479BXj_S-q2MpF-YUDqk'

channel_ids = ['UCoOae5nYA7VqaXzerajD0lg',
               ] # WE CAN ADD ALL CHANNEL IDS HERE

api_service_name = "youtube"
api_version = "v3"

youtube = build(
    api_service_name, api_version, developerKey=api_key)

request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id=','.join(channel_ids)  # TO CONCATENATE ALL CHANNEL IDS WITH A COMMA
)
response = request.execute()

JSON(response)



def get_channel_stats(youtube, channel_ids):
    all_data = []
    
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    response = request.execute()

    # loop through items
    for item in response['items']:
        data = {'channelName': item['snippet']['title'],
                'subscribers': item['statistics']['subscriberCount'],
                'views': item['statistics']['viewCount'],
                'totalVideos': item['statistics']['videoCount'],
                'playlistId': item['contentDetails']['relatedPlaylists']['uploads']
        }
        
        all_data.append(data)
        
    return(pd.DataFrame(all_data))

channel_stats = get_channel_stats(youtube, channel_ids)