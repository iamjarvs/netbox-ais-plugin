from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:aisPlugin:asnpools_list",
        link_text="ASN Pools",
    ),
    
    PluginMenuItem(
        link="plugins:aisPlugin:vnipools_list",
        link_text="VNI Pools",
    ),

    PluginMenuItem(
        link="plugins:aisPlugin:ippools_list",
        link_text="IP Pools",
    ),
)
