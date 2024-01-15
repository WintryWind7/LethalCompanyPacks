# LethalCompanyShipMaid
A mod where the ship and the storage closet is cleaned up when you press the associated keybinding within the ship.

# Usage
- Press 'M' to cleanup the ship and closet
- Press 'N' to cleanup the storage closet only
- Press 'J' to set an objects placement location (if position overrides enabled)
- Make sure that any players that you play with also have the mod installed for them to see the organized loot change positions.

# Features
## Basics
- Keypresses will organize each item type in groups by the name of the item
	- Ship cleanup default keybinding is 'M'
		- Items now are organized by [Value] by default. The futher from the door, the higher the value. Can also be [Stack] ed (See config settings)
		- Items are grouped in two locations, front of ship and back of ship (See config settings)
	- Closet cleanup default keybinding is 'N'
		- Items in the closet will be staggered slightly to the right of the 'first' item
	- Set object location default keybinding is 'J'
		- If UseOneHandedPlacementOverrides / UseTwoHandedPlacementOverrides / UseItemTypePlacementOverrides is enabled, pressing this keybind will log the location of the given item for future organization requests

## Config File Parameters
- Keybinds
	- CleanupShipKey
		- Keypress used to cleanup the ship and closet

	- CleanupClosetKey
		- Keypress used to cleanup the closet only

	- SetObjectTypePositionKey
		- Keypress used to set an object's organization location

- Ship Cleanup Configurations
	- ItemGrouping
		- Whether to group the items in tight clusters or to spread them out by value
		- Options
			- [Value]
				- Spread items up the ship by the value
			- [Stack]
				- Keep items stacked on top of one another to reduce clutter
			- Thanks to [jcsnider](https://github.com/jcsnider) for the suggestion

	- TwoHandedItemLocation
		- Where to place the two handed items, and inherrently where to place the single handed objects.
		- Options
			- [Front]
				- Two handed items to the front of the ship 
				- One handed items to the back of the ship
			- [Back]
				- Two handed items to the back of the ship 
				- One handed items to the front of the ship
		- Thanks to [jcsnider](https://github.com/jcsnider) and [Artemis-afk](https://github.com/Artemis-afk) for the suggestion

	- OrganizationTechniques
		- Options
			- [Loose]
				- Spread items accross the ship from left to right
			- [Tight]
				- Pack the items to the side of the ship with the suit rack.

- Item Type Overrides
	- ClosetLocationOverride
		- A List of objects to force into the closet on ship cleanup
			- Enter a list of item names in comma separated form to force these items to be placed in the closet instead of on the floor.
		- Thanks to [jcsnider](https://github.com/jcsnider) for the suggestion

	- SortingDisabledList
		- Items on this list will be ignored during the sorting process
			- Enter a list of item names in comma separated form to ignore these items during organization.
		- Thanks to [nontheoretical](https://github.com/nontheoretical) for the suggestion

- Position Overrides
	- UseItemTypePlacementOverrides
		- When [Enabled] and you have pressed 'J' with an item type in a given location, all future cleanup commands will place this item type in its given location 
		- During bootup all scrap objects that are not on the storage shelve list will be candidates for definiting these location prior to you setting the item locations using 'J'

	- UseTwoHandedPlacementOverrides
		- When [Enabled] and you have pressed 'J' with a one handed item in a given location, all future cleanup commands will place all one handed items in its the given location 
		- During bootup all two handed objects that are not on the storage shelve list will be candidates for definiting this location prior to you setting the item locations using 'J'

	- UseOneHandedPlacementOverrides
		- When [Enabled] and you have pressed 'J' with a two handed item in a given location, all future cleanup commands will place all two handed items in its the given location 
		- During bootup all one handed objects that are not on the storage shelve list will be candidates for definiting this location prior to you setting the item locations using 'J'

# Changes
- V3.2.3
	- Patched issue with one handed object location settings being incorrectly stored
- V3.2.2
	- Update readme for additional information and fixed old descriptions 
- V3.2.1
	- A minor patch fix for possible conflicting configuration issues
- V3.2.0
	- Added custom placement options (set locations with 'J' or whatever key you bind)
		- Place all two handed objects in the same location using UseTwoHandedPlacementOverrides=[Enabled]
		- Place all one handed objects in the same location using UseOneHandedPlacementOverrides=[Enabled]
		- Place all items of a given type in the same location using UseItemTypePlacementOverrides=[Enabled]	
- V3.1.1
	- Fixed an issue where loot was landing either on the storage closet or in the suit rack area 
- V3.1.0
	- Improved the handling of the bounds of the ship and storage closet to prevent items from clipping out of the ship.  
	- Thanks to [nontheoretical](https://github.com/nontheoretical) for finding the issue.
- V3.0.1
	- Fixes
		- Fixed a bug where modified scrap levels would teleport outside of ship when sorted by value
	- Features
		- Added a blacklist to sorting (Thanks to [nontheoretical](https://github.com/nontheoretical) for the suggestion)		 
- V3.0.0
	- Introduced a configuration system that will allow the customization and tailoring of the mod to your liking
	- Began working on ship storage closet functionality now that the ship functionality is ironing out.
	- Added Oranization configuration for stacking / spacing
	- Added closet override for defaulting storage location to closet for a customized list of items

- V2.1.1
  - Adjusted loot placement to avoid suit rack
- V2.1.0 
  - Updated the networking for better tying to client side functions
- V2.0.0
  - Made the system network compatible (definitely buggy)
- V1.1.0
  - The main control of the mod is now through keybinds.
  - Pressing 'm' will organize ship objects
  - Pressing 'n' will organize the ship's closet

# Installation
1. Install BepInEx
2. Run game once with BepInEx installed to generate folders/files
3. Drop the DLL inside of the BepInEx/plugins folder
4. No further steps needed

# Feedback
- Feel free to leave feedback or requests at [my github](https://github.com/bozzobrain/LethalCompanyShipMaid).

# Buy me a beer
[Buy me a beer](https://www.buymeacoffee.com/bozzobrain)
