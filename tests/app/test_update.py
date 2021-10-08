from starlette.testclient import TestClient

from rsserpent_plugin_bilibili import app


def test_route(client: TestClient) -> None:
    """Test `rsserpent_plugin_bilibili.route`."""
    response = client.get(app.update.path.format(platform="android"))
    assert response.status_code == 200
    assert "<title>哔哩哔哩更新情报 - 安卓版</title>" in response.text
