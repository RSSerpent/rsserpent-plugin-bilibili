from typing import Any, Dict
from rsserpent.utils import cached

from .bangumi import provider_base

path = "/bilibili/user/{uid}/cinema"


@cached
async def provider(uid: int) -> Dict[str, Any]:
    """当前路由调用封装."""
    type_info = {"id": 2, "name": "cinema", "name_zh": "追剧"}
    return await provider_base(uid, type_info)
