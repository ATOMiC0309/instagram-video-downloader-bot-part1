import requests
from pprint import pprint
from main import bot
import os


def instagram_downloader_func(insta_url, chat_id=None):
    try:
        url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/"

        querystring = {"url": insta_url}

        headers = {
            "x-rapidapi-key": "4b421b04d2mshcd3b9de88b7db44p135d78jsn6bb23f6d374b",
            "x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring).json()
        pprint(response)
        for res in response:
            title = res.get('title', "Sarlavha olinmadi!")
            type_content = res.get('type', "Xabar turi olinmadi!")
            content_url = res.get('url', "Url olinmadi!")
            with open(f"media/{chat_id}.mp4", 'wb') as file:
                file.write(requests.get(content_url).content)
            with open(f"media/{chat_id}.mp4", 'rb') as file:
                if type_content == 'video':
                    bot.send_video(chat_id, file, caption=f"Sarlavha: {title}\nTuri: {type_content}")
                else:
                    bot.send_photo(chat_id, file, caption=f"Sarlavha: {title}\nTuri: {type_content}")
    except:
        if os.path.exists(f"media/{chat_id}.mp4"):
            os.remove(f"media/{chat_id}.mp4")
        return False
    if os.path.exists(f"media/{chat_id}.mp4"):
        os.remove(f"media/{chat_id}.mp4")
    return True
