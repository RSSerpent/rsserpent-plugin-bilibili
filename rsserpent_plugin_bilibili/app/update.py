from typing import Any, Dict

import arrow
from rsserpent.utils import HTTPClient, cached


platform_trans = {
    "android": "安卓版",
    "iphone": "iPhone 版",
    "ipad": "iPad HD 版",
    "win": "UWP 版",
    "android_tv_yst": "TV 版",
}
path = "/bilibili/app/update/{platform}"


@cached
async def provider(platform: str) -> Dict[str, Any]:
    """订阅 Bilibili 客户端更新信息."""
    api_url = f"https://app.bilibili.com/x/v2/version?mobi_app={platform}"

    async with HTTPClient() as client:
        update_info = (await client.get(api_url)).json()

    return {
        "title": f"哔哩哔哩更新情报 - {platform_trans[platform]}",
        "link": "https://app.bilibili.com",
        "description": f"哔哩哔哩更新情报 - {platform_trans[platform]}",
        "items": [
            {
                "title": item["version"],
                "description": item["desc"],
                "link": "https://app.bilibili.com",
                "pub_date": arrow.get(item["ptime"]),
            }
            for item in update_info["data"]
        ],
    }
