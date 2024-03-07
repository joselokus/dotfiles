import subprocess
import socket
from libqtile.config import Screen
from libqtile import bar, widget

from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets, ternary_widgets, primary_asus_widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.96)



hostname=socket.gethostname()

if  hostname == 'asus-getlife':
    additional_widgets = [secondary_widgets, ternary_widgets]
    connected_monitors = 3
    screens = [Screen(
       top=status_bar(primary_asus_widgets)
    )]
else:
    additional_widgets = [secondary_widgets]
    connected_monitors = 2
    screens = [Screen(
       top=status_bar(primary_widgets)
    )]

for monitorIndex in range(0, connected_monitors - 1):
    screens.append(Screen(
        top=status_bar(additional_widgets[monitorIndex]),
        ))