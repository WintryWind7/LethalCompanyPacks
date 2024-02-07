## 2.3.1
- Fix file structure in Thunderstore for SCP 914 recipes (no changes to mod file)
- Changes to documentation/install instructions

## 2.3.0
- Added json-based custom conversions for SCP 914

## 2.2.1
- Fix inverted logic for doors (and manually account for Thumper/Mimic door speeds)
- Fixed issue with doors opening normally networking incorrectly

## 2.2.0
- Reprogrammed doors, should be less prone to navigation issues
- Fixed 914 global audio (hopefully for real this time)
- Fixed spraypaint not working

## 2.1.0
- Fix SCP 914 locking up if an item conversion is supposed to destroy an item
- Added per-moon rarity overrides
- Uncapped rarity value
- Added Secret Labs as a default config option
- Updated config descriptions

## 2.0.2
- Fix softlock on map generation when vanilla items are removed/replaced

## 2.0.1
- Fixed SCP 914 SFX radius being far too big

## 2.0.0
- Added SCP 914
- Fixed some minor mesh issues in SCP 914 room
- Minor adjustments to doors (may help with enemies getting stuck)

## 1.5.0
- v49 compatibility
- Ported to LethalLevelLoader (with some generation tweaks and additional config options, multiple fire exit moons e.g. March are now supported)
- Added much more lighting to the start room
- Fix some navmesh issues in 914 room
- Additional navmesh tweaks to reduce occurences of scrap spawning in walls/in ceilings

## 1.4.1
- Fix collisions missing in SCP 914 room

## 1.4.0
- Added SCP 914 room (Not functional... yet)
- Adjusted dungeon generation to make smaller dungeons (plus additional tweaks to try and make generation more consistent)
- Added new config option to allow customization of the dungeon size (use with caution)

## 1.3.2
- Tweaked moon config to be more flexible and support modded moons better
- More detailed logging of processes and additional error notify messages
- Lethal Expansion incompatibility note

## 1.3.1
- Fix door desync problem
- Fix scrap possibly spawning OOB
- Fix moon config not working with latest LethalLib versions
- Slightly decreased average size of generated dungeon (NOTE: Balanced around Titan; free moons may be relatively small)

## 1.3.0
- Fixed special scrap not spawning, improved scrap spawns in general
- Dungeon flow tweaks to further improve path generation
- Increased chances for special cap rooms to spawn (173, 372, etc)
- Added Bepinex/HookGenPatcher dependencies to make dependencies clearer for manual downloaders

## 1.2.0
- Added new rooms (173 Chamber, 3-way connector)
- Added open doorways for room connectors
- Improved room meshes to help prevent enemies/scrap spawning OOB and improve navigation
- Increased lighting brightness across all rooms
- Modified dungeon generation to increase odds of more winding paths
- Removed fire escapes from catwalks in 4-way room

## 1.1.1
- Fix readonly issue with some room meshes
- Improved lighting

## 1.1.0
- Fix missing room layer information, causing enemies/hazards to ignore walls/fail to recognise floors
- Added flat stair colliders

## 1.0.1
- Fix default config

## 1.0.0
- Initial release