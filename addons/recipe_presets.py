# pylint: disable=attribute-defined-outside-init
from typing import Any, Callable
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QGridLayout, QPushButton, QAbstractItemView, QListWidget, QLabel, QComboBox, QVBoxLayout
from PyQt5.QtGui import QFont, QCursor

# Auto created by CocktailBerry CLI version 1.20.3
# Imports are automatically generated for all the examples from the docs
# You can delete the imports you don't need
# For more information see: https://cocktailberry.readthedocs.io/addons/

# Use the LoggerHandler class for your logger
from src.logger_handler import LoggerHandler
# Use the dpc to display dialogues or prompts to the user
from src.display_controller import DP_CONTROLLER as dpc
# You can access the default database with help of the dbc
from src.database_commander import DB_COMMANDER as dbc
# The addon interface will provide intellisense for all possible methods
from src.programs.addons import AddonInterface
from src.ui_elements.clickablelineedit import ClickableLineEdit
from src.ui.setup_keyboard_widget import KeyboardWidget
from src.utils import restart_program

ADDON_NAME = "Recipe Presets"
_logger = LoggerHandler("ADDON: Recipe Presets")


# The class needs to be called Addon and inherit from the AddonInterface
class Addon(AddonInterface):
    def setup(self):
        """Inits the addon, executed at program start. """
        # creates two new table if it does not exists
        # the tables are called preset and preset_data
        # preset contains the preset name and the id
        # preset_data contains the preset id, and the recipe id
        dbc.handler.query_database(
            "CREATE TABLE IF NOT EXISTS preset (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);"
        )
        dbc.handler.query_database(
            "CREATE TABLE IF NOT EXISTS preset_data (preset_id INTEGER, recipe_id INTEGER);"
        )

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
        # everything for the layout
        self.grid_layout = QGridLayout()
        self.button_update = QPushButton("Update")
        self.button_update.setMinimumSize(QSize(335, 60))
        self.button_update.setMaximumSize(QSize(2000, 70))
        self.button_update.setFont(self._generate_font(18))
        self.grid_layout.addWidget(self.button_update, 4, 0, 1, 2)
        self.button_apply = QPushButton("Apply")
        self.button_apply.setMinimumSize(QSize(335, 60))
        self.button_apply.setMaximumSize(QSize(2000, 70))
        self.button_apply.setFont(self._generate_font(18))
        self.grid_layout.addWidget(self.button_apply, 4, 2, 1, 1)
        self.button_add = QPushButton("<-")
        self.button_add.setMinimumSize(QSize(100, 140))
        self.button_add.setMaximumSize(QSize(200, 600))
        self.button_add.setFont(self._generate_font(48))
        self.grid_layout.addWidget(self.button_add, 2, 1, 1, 1)
        self.button_remove = QPushButton("->")
        self.button_remove.setMinimumSize(QSize(100, 140))
        self.button_remove.setMaximumSize(QSize(200, 600))
        self.button_remove.setFont(self._generate_font(48))
        self.grid_layout.addWidget(self.button_remove, 3, 1, 1, 1)
        self.label_not_used = QLabel("Not Used")
        self.label_not_used.setMinimumSize(QSize(330, 0))
        self.label_not_used.setMaximumSize(QSize(800, 40))
        self.label_not_used.setFont(self._generate_font(20))
        self.label_not_used.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        self.grid_layout.addWidget(self.label_not_used, 1, 2, 1, 1)
        self.list_not_used = QListWidget()
        self.list_not_used.setMaximumSize(QSize(1000, 1000))
        self.list_not_used.setFont(self._generate_font(20, False))
        self.list_not_used.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # type: ignore
        self.list_not_used.setSelectionMode(QAbstractItemView.MultiSelection)  # type: ignore
        self.list_not_used.setSelectionBehavior(QAbstractItemView.SelectItems)  # type: ignore
        self.grid_layout.addWidget(self.list_not_used, 2, 2, 2, 1)
        self.label_used = QLabel("Used")
        self.label_used.setMinimumSize(QSize(330, 0))
        self.label_used.setMaximumSize(QSize(800, 40))
        self.label_used.setFont(self._generate_font(20))
        self.label_used.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        self.grid_layout.addWidget(self.label_used, 1, 0, 1, 1)
        self.selection_preset = QComboBox()
        self.selection_preset.setMinimumSize(QSize(105, 50))
        self.selection_preset.setMaximumSize(QSize(2000, 100))
        self.selection_preset.setFont(self._generate_font(14))
        self.selection_preset.setCursor(QCursor(QtCore.Qt.ArrowCursor))  # type: ignore
        self.selection_preset.setMaxVisibleItems(11)
        self.grid_layout.addWidget(self.selection_preset, 0, 0, 1, 1)
        self.list_used = QListWidget()
        self.list_used.setMaximumSize(QSize(1000, 1000))
        self.list_used.setFont(self._generate_font(20, False))
        self.list_used.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # type: ignore
        self.list_used.setSelectionMode(QAbstractItemView.MultiSelection)  # type: ignore
        self.list_used.setSelectionBehavior(QAbstractItemView.SelectItems)  # type: ignore
        self.grid_layout.addWidget(self.list_used, 2, 0, 2, 1)
        self.name_input = ClickableLineEdit()
        self.name_input.setFont(self._generate_font(20))
        self.name_input.setMinimumSize(QSize(105, 50))
        self.grid_layout.addWidget(self.name_input, 0, 1, 1, 2)
        container.addLayout(self.grid_layout)
        # other ui logic
        self.button_update.setProperty("cssClass", "btn-inverted")
        self.label_not_used.setProperty("cssClass", "secondary bold")
        self.label_used.setProperty("cssClass", "secondary bold")
        self.list_not_used.setSortingEnabled(True)
        self.list_used.setSortingEnabled(True)
        # populate the ui logic
        self.name_input.clicked.connect(lambda: KeyboardWidget(self, self.name_input, 30))  # type: ignore
        self.populate_dropdown()
        self.fill_list()
        self.button_update.clicked.connect(self.update_preset)
        self.button_add.clicked.connect(lambda: self.switch_elements(self.list_used, self.list_not_used))
        self.button_remove.clicked.connect(lambda: self.switch_elements(self.list_not_used, self.list_used))
        self.button_apply.clicked.connect(self.apply_preset)
        self.selection_preset.currentIndexChanged.connect(self.preset_selected)
        return True

    def update_preset(self):
        """Gets the data from the PyQt Elements and updates the database preset entry"""
        # we use the id as the combobox name, so we dont need to get the id from the database
        # gets the selected id
        preset_id = self.selection_preset.currentText()
        # if the id is "new" we need to create a new entry
        new_name = self.name_input.text()
        if preset_id == "new":
            dbc.handler.query_database("INSERT INTO preset (name) VALUES (?)", (new_name,))
            # now get the id of the new entry
            preset_id = dbc.handler.query_database("SELECT id FROM preset WHERE name = ?", (new_name,))[0][0]
            self.selection_preset.addItem(str(preset_id))
        # else update the name
        else:
            dbc.handler.query_database("UPDATE preset SET name = ? WHERE id = ?", (new_name, preset_id))
        # delete all old entries
        dbc.handler.query_database("DELETE FROM preset_data WHERE preset_id = ?", (preset_id,))
        # get all the text from the list widget
        used = [self.list_used.item(i).text() for i in range(self.list_used.count())]

        for recipe in used:
            cocktail = dbc.get_cocktail(recipe)
            if cocktail is None:
                continue
            dbc.handler.query_database(
                "INSERT INTO preset_data (preset_id, recipe_id) VALUES (?, ?)",
                (int(preset_id), cocktail.id)
            )
        dpc.standard_box(f"The preset #{preset_id}({new_name}) was updated successfully")
        # sets to the new preset, important if a new one was created
        dpc.set_combobox_item(self.selection_preset, str(preset_id))

    def populate_dropdown(self):
        """Populates the dropdown with all the presets"""
        dpc.fill_single_combobox(
            self.selection_preset,
            ["new"] + [str(i[0]) for i in dbc.handler.query_database("SELECT id FROM preset")],
            True, False, False
        )

    def fill_list(self):
        """Initially fills all the cocktails into the used list, nothing in not used"""
        cocktails = dbc.get_all_cocktails()
        self.list_used.clear()
        self.list_not_used.clear()
        self.name_input.setText("")
        dpc.fill_list_widget(self.list_used, [x.name for x in cocktails])
        self.list_used.sortItems()
        self.button_update.setText("Create Preset")

    def switch_elements(self, to_add: QListWidget, to_remove: QListWidget):
        """Trigger on button click to switch elements from one list to another"""
        if not to_remove.selectedItems():
            return

        ingredient_names = [x.text() for x in to_remove.selectedItems()]
        to_add.addItems(ingredient_names)

        for ingredient in ingredient_names:
            dpc.delete_list_widget_item(to_remove, ingredient)
        dpc.unselect_list_widget_items(to_remove)
        to_add.sortItems()

    def preset_selected(self):
        """Trigger when a preset is selected, fills the list widgets with the data from the preset"""
        selected_preset = self.selection_preset.currentText()
        # if its the new preset, we need to clear the list and return
        if selected_preset == "new":
            self.fill_list()
            return
        self.button_update.setText("Update Preset")
        # we need to get the recipe name from the database
        query = """
            SELECT r.Name
            FROM preset_data as pd
            INNER JOIN Recipes as r
            ON pd.recipe_id = r.ID
            WHERE pd.preset_id = ?
            """
        preset_data = [x[0] for x in dbc.handler.query_database(query, (int(selected_preset),))]
        # build sets of data used and not used
        all_recipes = {x.name for x in dbc.get_all_cocktails()}
        not_used = list(all_recipes - set(preset_data))
        self.list_used.clear()
        self.list_not_used.clear()
        dpc.fill_list_widget(self.list_used, preset_data)
        dpc.fill_list_widget(self.list_not_used, not_used)
        preset_name = dbc.handler.query_database("SELECT name FROM preset WHERE id = ?", (int(selected_preset),))[0][0]
        self.name_input.setText(preset_name)

    def apply_preset(self):
        """Apply the preset to the database"""
        preset_id = self.selection_preset.currentText()
        if preset_id == "new":
            return
        # set all recipes to active
        dbc.set_all_recipes_enabled()
        # select all recipe ids from the current preset id
        # set all recipes to inactive where the id is not in the list
        query = """
            UPDATE Recipes
            SET Enabled = 0
            WHERE ID NOT IN
            (SELECT recipe_id FROM preset_data WHERE preset_id = ?)
        """
        dbc.handler.query_database(query, (int(preset_id),))
        _logger.info(f"Preset #{preset_id} was applied")
        if dpc.user_okay(
            f"Preset #{preset_id} was applied. Restart the program? This is recommended, so changes can take effect."
        ):
            restart_program()

    def _generate_font(self, size: int, bold: bool = True):
        font = QFont()
        font.setPointSize(size)
        if bold:
            font.setBold(True)
            font.setWeight(75)
        return font
