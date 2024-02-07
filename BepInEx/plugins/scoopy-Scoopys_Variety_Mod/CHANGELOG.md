# 1.1.0
- Added lights in the death-jump room to make it less treacherous without a torch
- Added some lights to the piping to make it easier to navigate
- Reduced brightness of lights in the sewer slightly
- Fixed vent placement to line up with the walls better
- Fixed enemies being able to walk through walls surrounding doorways

# 1.0.1
- Fixed an issue that would cause planets and the ship to flood after visiting the sewer interior
- Fixed turrets being able to shoot through doorways

# 1.0.0
- Added a new interior: Sewer
- Added 2 new tiles to the dungeon interior
	- One of these acts as a generator equivalent, with a loot item equivalent to the apparatus. Picking this item up does not turn off the lights however.
- Increased lighting in dungeon interior, and lighting is now randomly generated
- Dungeon Props now spawn randomly, to add variety to room layouts
- Fixed doors pushing the player when opened
- Fixed spray paint not working on dungeon interior walls
- Fixed various graphical issues / tile misalignment issues
- Fire exits can no longer spawn inside the entry room of the dungeon
- Removed some troublesome vents which caused enemies to get stuck behind props on spawning
- Various other bug fixes/small improvements

# 0.6.5 
- Minor lighting changes to improve visibility and increase overall brightness in the Dungeon interior
- Removed some vents which were placed behind objects, causing enemies to get stuck

# 0.6.4
- Updated depenency to LethalLevelLoader 1.05
	- This should make string matching moon names using 'list' in the config more forgiving, and fix a bug with march

# 0.6.3
- Updated depenencies to LethalLevelLoader 1.04 and LethalLib 0.11.0
	- This should fix issues with March

# 0.6.2
- Fixed config not accepting 'list' as a valid value

# 0.6.1
- Fixed issue with MinCastleSizeMultiplier config value.

# 0.6.0
- Updated to be compatible with Lethal Company v47 and v48
- Added LethalLevelLoader as a dependency
	- This fixes moons with multiple fire exits not working - March is now compatible with this mod
	- This enables compatibility with moon mods which also use LethalLevelLoader - though there may be issues in the early stages
	- This also enables a higher degree of customisability via the config
- Reduced shadow draw distance to significantly improve performance
	- This should fix the performance issues encountered on larger maps/lower end systems and reduce lag spikes
	- If you continue to encounter significant performance issues please report it on the discord
- Added 1 new tile
- Updated config settings
	- CastleDungeonMoons: New value 'list' can be provided to allow more customisable moon configuration using CastleDungeonMoonsList config value.
	- CastleDungeonMoonsList: New config value which allows users to provide a comma seperated list of moon names and rarities. e.g. rend30, dine300, egypt100 which would register the dungeon on 'rend', 'dine' and 'egypt' at rarities 30, 300 and 100 respectively.
	- MaxCastleSizeMultiplier: New config value which allows users to specify the max size multiplier for the dungeon, capping map generation multipliers to this value.
	- MinCastleSizeMultiplier: This allows users to specify the min size multiplier for the dungeon, raising map generation multipliers to this value.
- Fixed turrets shooting through the central pillar in the spiral staircase tile
- Reduced reflectivity of dungeon surfaces
- Enabled generation on March when 'vanilla' is selected
- Various other bugfixes

# 0.5.1
- Changed fire exit spawning to be more similar to the base game
	- No longer spawns in a 1x1 room, now on random door blockers
- Changed guitar to be one-handed
	- While the desync issue may still occur, this should at least allow players who become desynced to still interact with the world
- Some lighting changes to hopefully improve performance

# 0.5.0
- Added a new room tile
- Changed door sounds for opening/closing/unlocking wood doors
- Changed dungeon interior moon config
	- You can now specify lists of individual moons instead of just pre-defined settings
	- You can specify modded moons aswell, though these are still unstable and may result in issues
	- If you have made any config changes you will likely need to update your config to match the new settings
- Fixed an issue where turrets could see/shoot through doorways and some objects
- Moved some torches to reduce lighting bleed-through
- Increased scrap value of fire axe and weezer guitar

# 0.4.0
- Added a new room tile
- Fixed enemies being unable to navigate up the spiral staircase
- Added a central pillar to the spiral staircase room
- Fixed enemies being able to walk through some map objects
- Adjusted map objects in some rooms

# 0.3.0
- Renamed to "Scoopy's Variety Mod" to avoid confusion with similarly named mods
- Fixed weezer guitar bugging out players games and being undroppable
	- Encountered no issues in my testing, please report if this issue persists
- Fixed enemies not being able to enter the spiral staircase room
	- Spiral staircase itself is still not functional
- Added config options to control scrap item rarities
- Adjusted lighting to improve FPS drops caused by hitting shadow cap

## 0.2.1
- Fixed dungeon spawning on March when not intended
	- This will disable dungeon spawning on modded moons for the short term - more permanent fix coming soon
- Added some props to the dining room tiles
- Moved the annoying table infront of one of the dining room door spawns 
- You can now specify specific planets other than titan in the config in a similar manner to titan ("vow", "rend", etc.)

## 0.2.0
- Added fire axe as a scrap and useable weapon
	- Only found as a scrap spawn, can't be bought
	- Deals significantly more damage than the shovel, or can be sold for a good price
- Significantly changed the generation parameters of the dungeon interior
	- Start room should no longer generate only a single path, and rather provide between 3-4 paths each time
	- Dungeon size has been reduced significantly, to improve navigation and bring it closer in-line to vanilla interiors
	- Overall dungeon generation should be more "branch-y" and less "depth-y"
- Changed dungeon lighting to improve visibility
	- Increased brightness and radius of torches 
	- Added and moved some torches in tiles
- Changed dungeon footstep sounds to better suit the material
- Significantly reduced likelihood of dungeon being too vertical and causing player to teleport to entrance
	- May still occur very rarely on titan
- Fixed enemies being unable to path up and down normal staircases
	- Only tested extensively with masked enemies - some enemies may still not work
- Fixed enemies not opening doors and walking through walls
	- Some enemies are still broken and unable to open doors, but none should walk through walls anymore
- Fixed an issue where players could clip through the front door and fall out of the map
- Changed cell-doors to fix server-wide syncing
- Fixed locked cell doors not being able to be unlocked with a key
- Minor changes to some dungeon tiles 

## 0.1.0
- Initial release
- Added dungeon interior.
- Added weezer guitar as two-handed scrap item.