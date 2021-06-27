# Bilibili up 主视频订阅.
from datetime import datetime

import requests


path = "/bilibili/user/video/{uid}"


def provider(uid: int) -> dict:
    """订阅 up 上传的最新视频."""
    user_info_url = (
        "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp".format(uid)
    )
    video_list_url = (
        "https://api.bilibili.com/x/space/arc/search?mid={}&ps=30&tid=0"
        "&pn=1&keyword=&order=pubdate&jsonp=jsonp ".format(uid)
    )

    user_info = requests.get(user_info_url).json()
    video_list = requests.get(video_list_url).json()

    username = user_info["data"]["name"]

    return {  # noqa: ECE001
        "title": username + " 的最新投稿视频",
        "link": "https://space.bilibili.com/{}/video".format(uid),
        "description": user_info["data"]["sign"],
        "items": list(
            map(
                lambda item: {
                    "title": item["title"],
                    "description": item["description"],
                    "link": "https://www.bilibili.com/video/" + item["bvid"],
                    "pubDate": datetime.fromtimestamp(item["created"]),
                    "author": username,
                },
                video_list["data"]["list"]["vlist"],
            )
        ),
    }
