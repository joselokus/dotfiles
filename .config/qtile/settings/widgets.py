from libqtile import widget
from .theme import colors
#from spotify import Spotify
import psutil

#Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
   return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
   return widget.TextBox(
       **base(fg, bg),
       fontsize=fontsize,
       text=text,
       padding=3
   )


def powerline(fg="light", bg="dark"):
   return widget.TextBox(
       **base(fg, bg),
       text="", # Icon: nf-oct-triangle_left
       fontsize=37,
       padding=-2
   )

def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Caskaydia Cove Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
        widget.Prompt(),
    ]


primary_widgets = [
    *workspaces(),

   separator(),

   powerline('color4', 'dark'),

   icon(bg="color4", text=' '), # Icon: nf-fa-download

   widget.CheckUpdates(
       background=colors['color4'],
       colour_have_updates=colors['text'],
       colour_no_updates=colors['text'],
       no_update_string='0',
       display_format='{updates}',
       update_interval=1800,
       custom_command='checkupdates',
   ),

   powerline('color3', 'color4'),

   icon(bg="color3", text=' '),  # Icon: nf-fa-feed

   widget.Net(**base(bg='color3'), interface='wlan0'),

   powerline('color2', 'color3'),

   widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

   widget.CurrentLayout(**base(bg='color2'), padding=5),

   powerline('color1', 'color2'),

   icon(bg="color1", fontsize=17, text='  '), # Icon: nf-mdi-calendar_clock

   widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

   powerline('color4','color1'),

   icon(bg="color4", fontsize=17, text='  '), #Icon: nf-mdi-volume_medium

   widget.PulseVolume(**base(bg='color4')),

   powerline('color2', 'color4'),

   widget.Memory(measure_mem='G', format='{MemUsed: .2f}{mm}/{MemTotal: .2f}{mm}',  foreground='4b974a', background='88c0d0'),

   powerline('grey', 'color2'),

   widget.CPU(foreground='4b974a', background='ABB2BF', format='{load_percent}% {freq_current}Ghz'),
   powerline('dark', 'grey'),
   icon(bg='dark',fontsize=17, text='🌡️'),
   widget.ThermalSensor(background='ffd47e', foreground='212121',tag_sensor='Core 0', format='{tag} {temp:.1f}{unit}'),
   separator(),
   widget.ThermalSensor(background='f07178', foreground='212121',tag_sensor='Core 1', format='{tag} {temp:.1f}{unit}'),
   separator(),
   widget.ThermalSensor(background='fb9f7f', foreground='212121', tag_sensor='Core 2', format='{tag} {temp:.1f}{unit}'),
   separator(),

   widget.ThermalSensor(background='ffd47e', foreground='212121',tag_sensor='Core 3', format='{tag} {temp:.1f}{unit}'),

   widget.Systray(background=colors['dark'], padding=5),

]

primary_asus_widgets = [
    *workspaces(),

   separator(),

   powerline('color4', 'dark'),

   icon(bg="color4", text=' '), # Icon: nf-fa-download

   widget.CheckUpdates(
       background=colors['color4'],
       colour_have_updates=colors['text'],
       colour_no_updates=colors['text'],
       no_update_string='0',
       display_format='{updates}',
       update_interval=1800,
       custom_command='checkupdates',
   ),

   powerline('color3', 'color4'),

   icon(bg="color3", text=' '),  # Icon: nf-fa-feed

   widget.Net(**base(bg='color3'), interface='wlan0'),

   powerline('color2', 'color3'),

   widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

   widget.CurrentLayout(**base(bg='color2'), padding=5),

   powerline('color1', 'color2'),

   icon(bg="color1", fontsize=17, text='  '), # Icon: nf-mdi-calendar_clock

   widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

   powerline('color4','color1'),

   icon(bg="color4", fontsize=17, text='  '), #Icon: nf-mdi-volume_medium

   widget.PulseVolume(**base(bg='color4')),

   powerline('color2', 'color4'),

   widget.Memory(measure_mem='G', format='{MemUsed: .2f}{mm}/{MemTotal: .2f}{mm}',  foreground='4b974a', background='88c0d0'),

   powerline('grey', 'color2'),

   widget.CPU(foreground='4b974a', background='ABB2BF', format='{load_percent}% {freq_current}Ghz'),
   powerline('dark', 'grey'),
   icon(bg='dark',fontsize=17, text='🌡️'),
   widget.ThermalSensor(background='ffd47e', foreground='212121',tag_sensor='Core 0', format='{tag} {temp:.1f}{unit}'),
   separator(),
   widget.ThermalSensor(background='f07178', foreground='212121',tag_sensor='Core 1', format='{tag} {temp:.1f}{unit}'),
   separator(),
   widget.ThermalSensor(background='fb9f7f', foreground='212121', tag_sensor='Core 2', format='{tag} {temp:.1f}{unit}'),
   separator(),

   widget.ThermalSensor(background='ffd47e', foreground='212121',tag_sensor='Core 3', format='{tag} {temp:.1f}{unit}'),
   separator(),
   widget.Systray(background=colors['dark'], padding=5),

]
secondary_widgets = [
    *workspaces(),

   separator(),

   powerline('color1', 'dark'),

   widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

   widget.CurrentLayout(**base(bg='color1'), padding=5),

   powerline('color2', 'color1'),

   widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

   powerline('color4','color1'),

   icon(bg="color4", fontsize=17, text='  '), #Icon: nf-mdi-volume_medium

   widget.PulseVolume(**base(bg='color4')),

   powerline('color2', 'color4'),

   widget.Memory(measure_mem='G', format='{MemUsed: .2f}{mm}/{MemTotal: .2f}{mm} ',  foreground='4b974a', background='88c0d0'),

   powerline('color3','color2'),
   widget.CPU(foreground='4b974a', background='a3be8c', format='CPU {load_percent}% {freq_current}Ghz'),
   widget.Pomodoro(),
   widget.CPUGraph(type='box'),
   widget.MemoryGraph(),

   #widget.Clipboard(),
   #widget.CPUGraph(),
   #widget.MemoryGraph(),

]
ternary_widgets = [
    *workspaces(),

   separator(),
   #Spotify(background='#292d3e', play_icon=' ', pause_icon='󰏤 '),
   powerline("color1", "dark"),
   widget.CurrentLayoutIcon(**base(bg="color1"), scale=0.65),
   widget.CurrentLayout(**base(bg="color1"), padding=5),
   powerline("color2", "color1"),
   widget.Clock(**base(bg="color2"), format="%d/%m/%Y - %H:%M "),
   widget.CurrentScreen(),
   powerline("color4", "color1"),
   icon(bg="color4", fontsize=17, text="  "),  # Icon: nf-mdi-volume_medium
   widget.PulseVolume(**base(bg="color4")),
   powerline("dark", "color4"),
   widget.CPUGraph(type="box"),
   widget.MemoryGraph(),
]

widget_defaults = {
    'font': 'Caskaydia Cove Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
