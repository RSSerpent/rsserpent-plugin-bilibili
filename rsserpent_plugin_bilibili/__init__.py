from rsserpent.models import Persona, Plugin

from . import route


plugin = Plugin(
    name="rsserpent-plugin-bilibili",
    author=Persona(
        name="creedowl",
        link="https://github.com/creedowl",
        email="creedowl@gmail.com",
    ),
    prefix="/bilibili",
    repository="https://github.com/creedowl/rsserpent-plugin-bilibili",
    routers={route.path: route.provider},
)
