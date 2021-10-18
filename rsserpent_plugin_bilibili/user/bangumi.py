from typing import Any, Dict

import arrow
from rsserpent.utils import HTTPClient, cached


path = "/bilibili/user/{uid}/bangumi"


@cached
async def provider(uid: int) -> Dict[str, Any]:
    """当前路由调用封装."""
    type_info = {"id": 1, "name": "bangumi", "name_zh": "追番"}
    return await provider_base(uid, type_info)


async def provider_base(uid: int, typea: Dict[str, Any]) -> Dict[str, Any]:
    """订阅用户追番/追剧列表."""
    user_info_api = f"https://api.bilibili.com/x/space/acc/info?mid={uid}&jsonp=jsonp"
    bangumi_list_api = (
        f"https://api.bilibili.com/x/space/bangumi/follow/list?type={typea['id']}"
        f"&follow_status=0&pn=1&ps=30&vmid={uid}"
    )

    async with HTTPClient() as client:
        user_info = (await client.get(user_info_api)).json()
        bangumi_list = (await client.get(bangumi_list_api)).json()

    username = user_info["data"]["name"]

    return {
        "title": f"{username} 的{typea['name_zh']}列表",
        "link": f"https://space.bilibili.com/{uid}/{typea['name']}",
        "description": user_info["data"]["sign"],
        "items": [
            {
                "title": f"{item['new_ep']['index_show']} - {item['title']}",
                "description": item["evaluate"],
                "link": f"https://www.bilibili.com/bangumi/play/ss{item['season_id']}",
                "pub_date": arrow.get(
                    item["new_ep"]["pub_time"]
                    if len(item["new_ep"]) > 1
                    else item["publish"]["pub_time"]
                ),
            }
            for item in bangumi_list["data"]["list"]
            if len(item["new_ep"])
        ],
    }
