from typing import Any, Callable
from PyQt5.QtWidgets import QVBoxLayout

# Auto created by CocktailBerry CLI
# Imports are automatically generated for all the examples from the docs
# You can delete the imports you don't need
# For more information see: https://cocktailberry.readthedocs.io/addons/

# Use the cfg to add your config / validation
from src.config_manager import CONFIG as cfg, shared
# Use the uil to add description and according translation
from src.dialog_handler import UI_LANGUAGE as uil
# The addon interface will provide intellisense for all possible methods
from src.programs.addons import AddonInterface

ADDON_NAME = "Start Glass Volume"


# The class needs to be called Addon and inherit from the AddonInterface
class Addon(AddonInterface):
    def setup(self):
        """Inits the addon, executed at program start. """
        options = [str(x) for x in range(100, 401, 25)]
        cfg.add_selection_config("ADDON_GLASS_VOLUME", options, "200")
        desc = {
            "en": "Glass volume set at application start.",
            "de": "Glasvolumen, welches bei Programmstart genutzt wird.",
        }
        uil.add_config_description("ADDON_GLASS_VOLUME", desc)
        shared.cocktail_volume = int(getattr(cfg, "ADDON_GLASS_VOLUME"))

    def cleanup(self):
        """Method for cleanup, executed a program end. """

    def before_cocktail(self, data: dict[str, Any]):
        """Executed right before the cocktail preparation.
        In case of a RuntimeError, the cocktail will not be prepared
        and the message will be shown to the user.
        """

    def after_cocktail(self, data: dict[str, Any]):
        """Executed right after the cocktail preparation"""

    def build_gui(
        self,
        container: QVBoxLayout,
        button_generator: Callable[[str, Callable[[], None]], None]
    ) -> bool:
        """Builds up the GUI to do additional things on command.
        Return:
        True, if you want to build an interface / GUI
        False, if you don't provide an interface / GUI
        """
        # Change to True, if you build your own GUI
        # Otherwise, an information will be shown, that the addon do not provide a GUI
        return False
