from starlette.testclient import TestClient

from rsserpent_plugin_bilibili import user


def test_route(client: TestClient) -> None:
    """Test `rsserpent_plugin_bilibili.route`."""
    response = client.get(user.video.path.format(uid=546195))
    assert response.status_code == 200
    assert "<author>老番茄</author>" in response.text
