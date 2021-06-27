from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient
from rsserpent.model.rss import Feed

from rsserpent_plugin_bilibili import plugin


app = FastAPI()
client = TestClient(app)


for path, provider in plugin.routers.items():

    @app.get(path)
    def router(data: dict = Depends(provider)) -> Feed:  # type: ignore
        """Define an example router."""
        return Feed(**data)


def test() -> None:
    """Test if each router works properly (returns 200)."""
    for path in plugin.routers:
        assert client.get(path).status_code == 200
