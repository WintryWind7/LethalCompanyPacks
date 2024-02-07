# 1.6.3
+ Fixed warnings when InputUtils is not enabled.
# 1.6.2
+ Fix for issue where dead masked enemies would constantly try to re-equip flashlights.
+ Fix for issue where masked enemies wouldn't properly destroy their holstered reserved flashlight after being destroyed.
# 1.6.1
+ Forgot to update README and dll version.
# 1.6.0
+ Masked enemies will now display your holstered reserved items if they are mimicking you.
# 1.5.10
+ Fixed the laser pointer red cube mesh issue. Again.
# 1.5.9
+ Changes to support ReservedItemSlotCore 1.8.9.
# 1.5.8
+ Added support for InputUtils, as a soft dependency. If this mod is enabled, you will be able to access any relevant hotkeys within the game's keybind menu.
+ Tweaks to fix an issue with flashlight turning on randomly when doing something kinda specific?
# 1.5.7
+ Actually fixed laser pointer this time.
# 1.5.6
+ Fixed laser pointer having a red square around it.
# 1.5.5
+ Fixed a specific issue causing an error about index out of range.
# 1.5.4
+ Stability improvements when running this mod, but host does not. (Temporarily disabling the use of the toggle flashlight hotkey if host is not running this mod. Will re-implement this again soon)
+ Updated dependency for ReservedItemSlotCore 1.7.4
# 1.5.3
+ Fixed issue with the base flashlight not hiding the "strap" part of the mesh while on your shoulder.
# 1.5.2
+ Flashlight now renders on shoulder in some cases where you can view yourself in third person.
# 1.5.1
+ Removed some noisy logs.
# 1.5.0
+ Fixed the main issue of null object references when turning on/off flashlights at times, and/or dropping them.
+ Allows the laser pointer to populate the reserved flashlight slot.
+ Updated for ReservedItemSlotCore 1.6.0
# 1.4.6
+ Flashlight in currently held slot (not reserved slot) should now activate correctly when pressing LMB.
# 1.4.5
+ Minor fixes.
# 1.4.4
+ Previously broke turning on the flashlight with left click. This has been fixed.
+ Fixed some cases where the flashlight mesh's active state was incorrect.
# 1.4.3
+ Finally tracked down and fixed the bug preventing players from using their hotkeys to swap hotbars, or activate their reserved items with [F] or [X]
# 1.4.2
+ Updated load order to ensure the core mod loads first.
# 1.4.1
+ Fixed not properly handling PlayerActions in the OnDisable method if they were not yet initialized.
# 1.4.0
+ Involved in a code restructure/organization and updated to support ReservedItemSlotCore 1.4.0
+ Refer to the ReservedItemSlotCore 1.4.0 patch notes for more.
# 1.3.2
+ Accidentally hid flashlight mesh when other players equipped it, cause you not to see the flashlight on their shoulder.
# 1.3.1
+ Because of weird lighting issues, your local player will continue using their helmet light while not holding a flashlight.<br>
Other players will still appear to have a flashlight on their shoulder.
# 1.3.0
+ The flashlight now mounts to your shoulder when not in your hand.
# 1.2.2
+ Updated to support a few tweaks in the ReservedItemSlotCore mod.
+ Fixed some desync issues, and tweaked some other settings.
# 1.2.1
+ The activate flashlight keybind shouldn't "try" to run on non-owned players anymore.
+ Fixed bug causing players to get stuck on terminal.
# 1.2.0
+ Updated dependency to support the updated Core plugin.
# 1.1.0
+ You can now change the flashlight hotkey in the config.
+ Various tweaks to support the updated core mod.
# 1.0.1
+ Fixed a bug in the item controls tooltip where some text was duplicating.
# 1.0.0
+ Initial release