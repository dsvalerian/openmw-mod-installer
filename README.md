# openmw-mod-installer
A portable desktop application for quickly and easily installing Morrowind mods for OpenMW.

## Description
OpenMW is an open-source engine implementation for Bethesda's open-world RPG game The Elder Scrolls III: Morrowind. 
Like other Bethesda games, Morrowind has a very active modding community with nearly two decades of mod history.
When playing Morrowind using OpenMW, the process for installing mods is different than for the release version of the game.
This portable application was written to make that process easier.

## General Modding Process for OpenMW
OpenMW players generally have an `openmw.cfg` file in a Users subdirectory. To install mods, they must have the mod packaged in a data folder, then go to the `openmw.cfg` and manually add a line for each mod folder, structured like `data="<mod_folder_path>"`.

This application automates that process.

## Usage
- Place the `.exe` file in the same directory as your mod data folders. It should look something like this:
  -- mods_folder/
    -- mod1_folder/
    -- mod2_folder/
    -- mod3_folder/
    -- openmw-mod-installer `.exe`
    
- Click and run the .`exe`
- Follow the on-screen instructions.
- Afterwards, make sure to launch the `OpenMW` launcher and check any data files that are included with your mods.

The application will prompt the user to give a path to the directory containing their `openmw.cfg` file. Most players can leave this blank and let the application use the default path.
Note: This is NOT the `openmw.cfg` file located in their `OpenMW` application directory. It is the config file located in their user directory, along with their saves.
