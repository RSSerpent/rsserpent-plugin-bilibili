from rsserpent.models import Persona, Plugin

from . import user, app


plugin = Plugin(
    name="rsserpent-plugin-bilibili",
    author=Persona(
        name="creedowl",
        link="https://github.com/creedowl",
        email="creedowl@gmail.com",
    ),
    prefix="/bilibili",
    repository="https://github.com/creedowl/rsserpent-plugin-bilibili",
    routers={user.video.path: user.video.provider,
             app.update.path: app.update.provider},
)
