from typing import Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from PyQt5.QtWidgets import QVBoxLayout

from src.machine.controller import MACHINE
from src.config_manager import CONFIG as cfg
from src.dialog_handler import UI_LANGUAGE as uil
from src.logger_handler import LoggerHandler
from src.programs.addons import AddonInterface
from src.utils import time_print

ADDON_NAME = "Glass Detection"
_logger = LoggerHandler("ADDON: Glass Detection")


# The class needs to be called Addon and inherit from the AddonInterface
class Addon(AddonInterface):
    def setup(self):
        """Inits the addon, executed at program start."""
        cfg.add_config("ADDON_GLASS_DETECTION_ACTIVE", False)
        uil.add_config_description(
            "ADDON_GLASS_DETECTION_ACTIVE",
            {
                "en": "Activates the detection of glass before cocktail, needs hardware",
                "de": "Aktiviert die Erkennung von Glas vor dem Cocktail, benötigt Hardware",
            },
        )
        cfg.add_config("ADDON_GLASS_DETECTION_PIN", 0)
        uil.add_config_description(
            "ADDON_GLASS_DETECTION_PIN",
            {
                "en": "Pin number of the glass detection hardware",
                "de": "Pinnnummer der Hardware für die Glaserkennung",
            },
        )
        cfg.add_config("ADDON_GLASS_DETECTION_USE_HIGH", True)
        uil.add_config_description(
            "ADDON_GLASS_DETECTION_USE_HIGH",
            {
                "en": "Uses high signal if glass is present for glass detection, disable if low signal is used",
                "de": "Benutzt ein high Signal, wenn Glas erkannt wurde für die Glaserkennung, deaktiviere dies, wenn low Signal benutzt wird",  # noqa
            },
        )
        self.glass_detection_active = getattr(
            cfg, "ADDON_GLASS_DETECTION_ACTIVE", False
        )
        self.glass_detection_pin = getattr(cfg, "ADDON_GLASS_DETECTION_PIN", 0)
        self.glass_use_high = getattr(cfg, "ADDON_GLASS_DETECTION_USE_HIGH", True)
        self.pin_controller = MACHINE.pin_controller
        if self.glass_detection_active:
            time_print(
                f"ADDON: Initializing Glass Detection Pin: {self.glass_detection_pin}"
            )
            # Try to initialize the pin, if it fails, log the error and disable the addon
            # This is because otherwise the machine may not be able to prepare cocktails
            try:
                self.pin_controller.initialize_pin_list(
                    [self.glass_detection_pin],
                    is_input=True,
                    pull_down=self.glass_use_high,
                )
            except (RuntimeError, IOError) as e:
                _logger.log_event(
                    "ERROR",
                    "ADDON: Could not initialize glass detection pin. See error log for details.",
                )
                _logger.log_exception(e)
                self.glass_detection_active = False

    def cleanup(self):
        """Method for cleanup, executed a program end."""
        # the controller cleans up all pins, so we do not need to clean up this pin

    def before_cocktail(self, data: dict[str, Any]):
        """Executed right before the cocktail preparation.
        In case of a RuntimeError, the cocktail will not be prepared
        and the message will be shown to the user.
        """
        msg = {
            "en": "No glass was detected, please put a glass unter the outlet!",
            "de": "Kein Glas wurde erkannt, bitte stelle ein Glas unter den Ausguss!",
        }

        if not self._glass_is_present():
            message = msg.get(cfg.UI_LANGUAGE, msg["en"])
            raise RuntimeError(message)

    def after_cocktail(self, data: dict[str, Any]):
        """Executed right after the cocktail preparation"""

    def build_gui(
        self,
        container: QVBoxLayout,
        button_generator: Callable[[str, Callable[[], None]], None],
    ) -> bool:
        """Builds up the GUI to do additional things on command.
        Return:
        True, if you want to build an interface / GUI
        False, if you don't provide an interface / GUI
        """
        # Change to True, if you build your own GUI
        # Otherwise, an information will be shown, that the addon do not provide a GUI
        return False

    def _glass_is_present(self) -> bool:
        """Checks if a glass is present at the glass detection pin.
        Returns:
        True, if a glass is present
        False, if no glass is present
        """
        # always return true if turned off
        if not self.glass_detection_active:
            return True
        # output of a pin is True if high, False if low
        high_signal = self.pin_controller.read_pin(self.glass_detection_pin)
        if self.glass_use_high:
            return high_signal
        # so if the hardware uses low signal for detection, invert the value
        return not high_signal
