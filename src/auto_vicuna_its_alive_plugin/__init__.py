"""This is an example plugin for Auto-Vicuna."""
from typing import Any, Optional

from auto_vicuna_plugin_template import AutoVicunaPluginTemplate


class AutoVicunaItsAlivePlugin(AutoVicunaPluginTemplate):
    """
    This is an example plugin for Auto-Vicuna.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-Vicuna-Its-Alive"
        self._version = "0.1.0"
        self._description = "This is an example plugin for Auto-Vicuna."

    def on_response(self, response: str, *args, **kwargs) -> Optional[Any]:
        """This method is called when a response is received from the model."""
        if len(response):
            print("OMG OMG It's Alive!")
        else:
            print("Is it alive?")
