from typing import Any, Dict

import arrow
from rsserpent.utils import HTTPClient, cached


path = "/bilibili/user/{uid}/video"


@cached
async def provider(uid: int) -> Dict[str, Any]:
    """订阅 up 上传的最新视频."""
    user_info_api = f"https://api.bilibili.com/x/space/acc/info?mid={uid}&jsonp=jsonp"
    video_list_api = (
        f"https://api.bilibili.com/x/space/arc/search?mid={uid}&ps=30"
        "&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp"
    )

    async with HTTPClient() as client:
        user_info = (await client.get(user_info_api)).json()
        video_list = (await client.get(video_list_api)).json()

    username = user_info["data"]["name"]

    return {
        "title": f"{username}的最新投稿视频",
        "link": f"https://space.bilibili.com/{uid}/video",
        "description": user_info["data"]["sign"],
        "items": [
            {
                "title": item["title"],
                "description": item["description"],
                "link": f"https://www.bilibili.com/video/{item['bvid']}",
                "pubDate": arrow.get(item["created"]),
                "author": username,
            }
            for item in video_list["data"]["list"]["vlist"]
        ],
    }
