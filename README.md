<img src="https://raw.githubusercontent.com/AndreWohnsland/CocktailBerry/master/docs/pictures/CocktailBerry.svg" alt="CocktailBerry"/>

![GitHub release (latest by date)](https://img.shields.io/github/v/release/AndreWohnsland/CocktailBerry)
![GitHub Release Date](https://img.shields.io/github/release-date/AndreWohnsland/CocktailBerry)
![Python Version](https://img.shields.io/badge/python-%3E%3D%203.9-blue)
![GitHub](https://img.shields.io/github/license/AndreWohnsland/CocktailBerry)
![GitHub issues](https://img.shields.io/github/issues-raw/AndreWohnsland/CocktailBerry)
[![Documentation Status](https://readthedocs.org/projects/cocktailberry/badge/?version=latest)](https://cocktailberry.readthedocs.io)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AndreWohnsland_CocktailBerry&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=AndreWohnsland_CocktailBerry)
![GitHub Repo stars](https://img.shields.io/github/stars/AndreWohnsland/CocktailBerry?style=social)

[![Buy Me a Coffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow)](https://www.buymeacoffee.com/AndreWohnsland)

# CocktailBerry-Addons

Repository for all official [CocktailBerry addons](https://cocktailberry.readthedocs.io/).
For a detailed user guide, have a look into the official [documentation](https://cocktailberry.readthedocs.io/addons/).
This is the official providing point for the app addon ressources, automatically listed and managed over the GUI.
If you are interested in creating an addon for CocktailBerry, have a look into the user guide, fork this repo, and commit a PR.

## Addon Overview

Here is a list of currently available addons.

### 🥛 Start Glass Volume

A simple addon, which adds the option to define the default glass volume, set at machine start.
This setting will replace the default 200 ml with the selected value.
Just install it over the GUI and enjoy the additional setting.

### 📝 Recipe Presets

Use this addon to get access to an additional GUI for the management of different active presets of your cocktail recipes.
You can create and edit presets, as well as activate them.
Within a preset, you can define the recipes, which should be available for the maker.
The preset will then set your selection to enabled and all other recipes to disabled.
Note that this does not change the default CocktailBerry behavior, but only alter the list used for available recipe calculation.
Quickly switch between different presets and enjoy the flexibility of CocktailBerry.
You can access the GUI as soon as you installed the addon over the addon GUI.

## Development

To get started go to the documentation for the [CocktailBerry addons](https://cocktailberry.readthedocs.io/addons/).
You will most likely develop your addon according to this guideline within your local CocktailBerry.
If you are satisfied, fork this project, create a branch and place your addon into this repo `addons` folder.
If your addon needs extensive documentation, you can also create an own folder within the addons folder with the python file, as well as a readme file.
Otherwise, the documentation or description can be put into this readme file under the overview section.
To get your addon discovered and installable by CocktailBerry, place the according information into the `addon_data.json` file.
Each addon is a element in the list, containing name, description and the (raw) file url.
You can stick to the existing entries, as an example.
Please make the name entry similar to the `ADDON_NAME` defined in your addon file.
If you prefer using your own repository for the addon, you will only need to enter the data into `addon_data.json`, but refer the url to your project location.

After that, you can create a pull request and let your addon get verified.
Verified addons are beneficial for the user because the will be shown over the GUI and can be installed with one click over it.
Please remember, if you addon needs additional packages not included within CocktailBerry, either provide installation instruction or implement this logic into the addon setup.