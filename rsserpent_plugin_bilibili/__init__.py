from rsserpent.model import Persona, Plugin

from . import video


author = Persona(
    name="creedowl",
    link="https://github.com/creedowl",
    email="creedowl@gmail.com",
)

plugin = Plugin(
    name="rsserpent-plugin-bilibili",
    description="Bilibili subscriber.",
    author=author,
    maintainers=[author],
    prefix="/bilibili",
    repository="https://github.com/creedowl/rsserpent-plugin-bilibili",
    routers={video.path: video.provider},
)
