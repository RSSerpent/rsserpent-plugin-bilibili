from rsserpent.model import Persona, Plugin

from . import api, html


author = Persona(
    name="queensferryme",
    link="https://github.com/queensferryme",
    email="queensferry.me@gmail.com",
)

plugin = Plugin(
    name="rsserpent-plugin-example",
    description="An example plugin for RSSerpent.",
    author=author,
    maintainers=[author],
    repository="https://github.com/RSSerpent/rsserpent-plugin-example",
    routers={api.path: api.provider, html.path: html.provider},
)
