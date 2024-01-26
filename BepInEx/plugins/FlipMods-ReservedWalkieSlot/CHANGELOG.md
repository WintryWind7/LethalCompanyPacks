# 1.6.1
+ Fix for issue where dead masked enemies would constantly try to re-equip walkies.
+ Fix for issue where masked enemies wouldn't properly destroy their holstered reserved walkie after being destroyed.
# 1.6.0
+ Masked enemies will now display your holstered reserved items if they are mimicking you.
# 1.5.5
+ Changes to support ReservedItemSlotCore 1.8.9
+ Fixed issue with not being able to type correctly in terminal with walkie equipped, and pressing the talk hotkey.
+ Fixed issue with building placement/rotation being canceled when speaking into walkie.
# 1.5.4
+ Added support for InputUtils, as a soft dependency. If this mod is enabled, you will be able to access any relevant hotkeys within the game's keybind menu.
+ Undid the edited tooltip for the walkie controls.
# 1.5.3
+ Fixed a specific issue causing an error about index out of range.
# 1.5.2
+ Stability improvements when running this mod, but host does not. (Temporarily disabling the use of the walkie's push to talk hotkey (when holstered) if host is not running this mod. Will re-implement this again soon)
+ Updated dependency for ReservedItemSlotCore 1.7.4
# 1.5.1
+ Walkie now renders on shoulder in some cases where you can view yourself in third person.
# 1.5.0
+ Various tweaks.
+ Updated for ReservedItemSlotCore 1.6.0
# 1.4.6
+ Updated dependency.
# 1.4.5
+ Should be able to activate the walkie again with LMB when currently held.
# 1.4.4
+ Fixed some cases where the walkie mesh's active state was incorrect.<br>
I will re-add the mesh to the local player when I get a good position for it.
# 1.4.3
+ Finally tracked down and fixed the bug preventing players from using their hotkeys to swap hotbars, or activate their reserved items with [F] or [X]
# 1.4.2
+ Updated load order to ensure the core mod loads first.
# 1.4.1
+ Fixed not properly handling PlayerActions in the OnDisable method if they were not yet initialized.
# 1.4.0
+ The walkie now straps nicely to your chest when not in your hand.
+ Involved in a code restructure/organization and updated to support ReservedItemSlotCore 1.4.0
+ Refer to the ReservedItemSlotCore 1.4.0 patch notes for more.
# 1.2.2
+ Updated to support a few tweaks in the ReservedItemSlotCore mod.
+ Fixed some desync issues, and tweaked some other settings.
# 1.2.1
+ The activate walkie keybind shouldn't "try" to run on non-owned players anymore.
+ Fixed bug causing players to get stuck on terminal.
# 1.2.0
+ Updated dependency to support the updated Core plugin.
# 1.1.0
+ You can now change hotkey for talking in the walkie in the config.
+ Various tweaks to support the updated core mod.
# 1.0.1
+ Fixed a bug in the item controls tooltip where some text was duplicating.
# 1.0.0
+ Initial release