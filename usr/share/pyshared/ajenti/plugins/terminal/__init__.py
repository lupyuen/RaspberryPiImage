from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Terminal',
    icon='list-alt',
    dependencies=[
        PluginDependency('main'),
    ],
)


def init():
    import main
