# 1.7.18
+ Additional tweaks to maybe fix the emotes canceling for players at times.
# 1.7.17
+ Fixed compat with certain terminal mods, such as Neofetch.
+ Fixed echoing in third person emote camera.
+ Made some small changes to maybe prevent issue with player's animations getting canceled when another player cancels their. Probably didn't fix it.
# 1.7.16
+ Fixed compat with MoreCompany.
+ Fixed bug where emote credits were being depleted for everyone when one player purchased an emote with ShareEverything disabled.
+ Fixed bug with emotes/emote credits not being loaded correctly for non-host clients.
# 1.7.15
+ Re-added hook method ModelReplacementAPI used to grab currently playing emotes. (I forgot it was referencing it)
# 1.7.14
+ Tweaked some code to help a bit more with compat with mods that might edit the player's animator controller.
# 1.7.13
+ Fixed issue with "start" emote clips not transition to the "loop" emote clip.
+ Fixed issue with certain emotes not knowing when they ended.
# 1.7.12
+ Added checks in case the player's animator controller is not an AnimatorOverrideController.
+ Fixed issue with not being able to scroll in the emote menu.
# 1.7.11
+ Restructure and reorganization of some code.
+ Fixed issue when the ShareEverything setting in the config is disabled and a player purchases an emote, the emote credits shouldn't be deducted from each player anymore.
+ Some UI tweaks.
+ Possible fix for the issue when players cancel an emote, other players emotes "break".
# 1.7.10
+ Fixed issue with dress girl showing up in the third person emote camera when she's not supposed to be visible.
+ Attempted fix for lag caused by code when MoreCompany is not enabled. (Thanks legoandmars!)
+ Rotating while emote can now be set to toggle in the config.
+ Audio is now based off of the third person emote camera while emoting.
# 1.7.9
+ Added more compat checks for More_Emotes. You should now be unable to emote while performing an emote from More_Emotes. (maybe even from other mods that add emotes)
+ The third person emote camera should now reset and swap back to the main camera if you die.
+ Attempted to fix some issues with translation mods causing issues when checking for certain values in the terminal. (hopefully fixed)
# 1.7.8
+ Re-added Masked Enemies emoting for non-host clients. Will continue testing and tweaking if needed.
# 1.7.7
+ Disabling Masked Enemy emotes for non-host client until I fix the bug with them.
# 1.7.6
+ Fixed issue with some input bindings.
# 1.7.5
+ Edited config descriptions related to keybinds.
# 1.7.4
+ Added support for InputUtils, as a soft dependency. If this mod is enabled, you will be able to access any relevant hotkeys within the game's keybind menu.
+ Some visual tweaks to the radial menu.
+ Created a bit of the framework for controller support. Will release soon!
# 1.7.3
+ Fixed issue with some of the new configs not syncing.
+ Removed Herobrine.
# 1.7.2
+ Fixed errors spamming when looking at a player who is not emoting.
# 1.7.1
+ Fixed some minor issues.
+ Added compatibility for BetterEmotes.
# 1.7.0
+ Added a config option to enable/disable sharing emotes. Read about this in the README!
+ Added something special with the Masked Enemies! Read about this in the README!
+ Fixed deformed character rigs after certain animations.
+ Fixed a bug with being able to perform emotes/open the emote menu when in special animations with enemies.
+ Fixed a bug where the default group credits wouldn't update when used to purchase emotes.
+ Fixed a bug when non-host clients purchased emotes, that the emote credit balance wouldn't update.
+ Players joining after a player DC'd while emoting <i>should</i> not have a broken animation rig anymore for other players.
+ Added a few more emotes!
+ Added config option to disable emoting for yourself. If disabled, this mod will not alter the default player's animator/animator controller, and may fix issues with compatibility with certain mods, such as VR mods.
# 1.6.4
+ Fixed "pose" emotes ending early.
# 1.6.3
+ Minor bug fixes.
# 1.6.2
+ Fixed accidental infinite loop.
# 1.6.1
+ Potential fix for emotes in the store sometimes not syncing with everyone.
# 1.6.0
+ Can now sync emotes with other players by looking at them and pressing E. (will update soon to match interact key)<br>
Syncing with another player's emote will perform the same emote, and match their time in the animation.
+ You can now rotate your character while emoting while holding the Alt key. (can be changed in config)
+ You can now zoom in and out while performing a custom emote by scrolling. Distance is clamped at 1.5 and 5.
+ Various fixes.
# 1.5.10
+ Fixed issue where clients lock up in a dark shadow screen. (not sure about every instance)
+ Fixed issues in some cases where clients don't sync emotes with host properly when the host has all emotes unlocked at start.<br>
(hopefully fixed the main issues from the previous patch)
# 1.5.9
+ Fixed non-host clients in some cases showing that they have every emote unlocked when they don't, but it won't let them use them. They should sync correctly again with the host.
+ Reverted some settings to fix some rendering bugs.
# 1.5.8
+ Fixed issue with some model replacement mods where you see your player's body at times. (hopefully didn't break anything)
# 1.5.7
+ Broke MoreCompany, but refixed now.
+ Tweaked/polished many existing emotes.
+ Added more emotes!
+ Added a Rock Paper Scissors emote to the complementary emotes.<br>
The RPS emote played is random. (I will need to tweak the hands a bit, though)
+ Fixed bug with emotes clients not playing the same emotes for specific emotes.
+ Emote store seed now resets correctly upon resetting ship.
+ Temporarily removed some emotes so I can fix the feet IK. (Will do later)
+ Added more emote loadout tabs. One for complementary, and one for each emote tier. I'll try to get feedback about these later.
# 1.5.6
+ Fixed issue with config not syncing.
+ Fixed issue with favorites not saving/loading at times.
# 1.5.5
+ Forgot to update README.
+ Some formatting tweaks to the terminal.
# 1.5.4
+ Player's shadow should no render correctly while in first person. Should still be compatible with MirrorDecor.
+ Added emote loadouts to the left of the radial menu. Currently, there are only "Favorites" and "All".<br>
Favorited emotes will persist across sessions/saves or game launches. However, they will not be available unless unlocked in your current session.
+ Added a config to re-allow purchasing emotes with group credits again. Emote credits will still be prioritized over group credits.
# 1.5.3
+ Fixed some new emotes not looping when supposed to.
# 1.5.1
+ Emotes can now only be purchased with emote credits.
+ 50% of all normal group credits earned will also be gained as emote credits. This amount can be changed in the configs.
+ Added 17 new emotes!
# 1.5.0
+ Fixed items in local player's hand when performing emotes.
+ Wrote code for CanOpenEmoteMenu(), but never called it. Fixed this.
+ Set toggle open menu to toggle by default. (can still be changed)
+ Changed default change emote page direction. I don't even know which should be default direction for scroll up/down...
+ Default sorting is by rarity, then by name.
+ Brightened the animation preview a bit.
+ Few other changes.
# 1.4.9
+ Applied compatibility patch for BiggerLobby (Thanks legoandmars!)
+ Publicized most of my classes to help with compatibility.
+ Various minor fixes.
# 1.4.8
+ Fixed local player mesh disappearing in third person emotes after dying.
+ Fixed seed not updating and/or syncing properly.
# 1.4.7
+ Fixed issue with scrolling 4 pages at a time in the emote wheel.
+ Fixed syncing buffer overflow issue.
# 1.4.6
+ Added the california girls dance meme from friday the 13th (I think)
# 1.4.5
+ Reduced the price of the tier 4 emotes to 300 (from 500)
+ Fixed compatibility with MoreCompany and MirrorDecor. Hopefully for good this time.
+ Animation preview now shows current skin, as well as any MoreCompany Cosmetics. (might work with custom models)
+ Changed the way the animation preview lighting works.
+ By default, the emote menu is not toggled anymore. Press to open, release to close. Releasing will play the currently hover emote. You can set this back to toggled in the config.
+ Can now change emote page by scrolling. You can reverse the scroll direction can be reversed in config.
+ Updated how syncing works between client/server. <i>Should</i> fix the issues with not syncing emotes and such with server.
# 1.4.4
+ Reverted MirrorDecor and MoreCompany compatibility patch for now.
# 1.4.3
+ Fixed wrong asset bundle path.
# 1.4.2
+ Fixed an issue when disabling the rarity, where the likelyhood of an emote was based on the tier, regardless of how many emotes were in that tier.<br>
This made the emotes from the upper tiers appear more frequently than the ones from the ower tiers.
# 1.4.1
+ Forgot to normalize the prices if the rarity system was disabled in the config.
+ Added config entry for setting the base price for emotes when the rarity system is disabled.
# 1.4.0
+ Added compatibility with MoreCompany and MirrorDecor!
+ Now unlocks all emotes at the start of the game if host does not have the mod.
+ Added an emote rarity system. Each emote will have its own tier, which affects how often emotes of that rarity will appear in each store's rotation slot.<br>
If you're not a fan of the rarity system, you could set all the weights for each tier to the same number in the config.
+ Emotes are now priced based on their rarity. They are not all 100 anymore.
+ Emote store now shows 6 emotes by default instead of 3.
+ Because of this tier system, emote coupons have been removed, and have been replaced with emote credits.
+ Emote names in the terminal have been color coded based on their tier. (green, blue, purple, and red) The colors can be changed in the accessibility section in the config.
+ Weapon wheel not displaying the correct emote has been fixed.
+ The seed bug <i>should</i> be fixed now. It preventing the seed from updating after new games.
# 1.3.9
+ Fixed bug where emotes weren't rotating until after the first round.
+ Fixed bug where free emote coupons weren't registering correctly.
# 1.3.8
+ Forgot to move Asset Bundles into their folder.
# 1.3.7
+ Fixed emotes not rotating daily.
+ Fixed local player arms sometimes appearing during emotes.
+ Potential fix for issue with terminal thinking players are trying to buy an emote when they're not.
+ Moved Asset Bundles in the Assets folder.
# 1.3.6
+ Fixed issue with asset bundles
# 1.3.5
+ Added pages to emote radial menu.
+ Fixed issue with not seeing others emoting with More_Emotes mod installed.
+ Added config to start with all emotes unlocked. (Server only setting, and will sync with clients)
+ Added basic complementary emotes to start with.
+ Tweaked existing emote animations.
+ Emote selection rotates daily!
+ Now over 100 emotes!
# 1.3.2
+ Now automatically removes old config entries.
+ Forgot to re-place the preview animation render subject underneath the map again.
# 1.3.1
+ Accidentally left out updated README.
# 1.3.0
+ Added an Emote Radial Menu!
+ Fixed the issue with start animations not transitioning properly to their loop animation. (as far as I can tell)
+ Potential fix for not loading the asset bundle when not using a mod loader.
+ Various other fixes. There are likely some that I missed.
# 1.2.5
+ MoreEmotes compatibility patch did not upload with my last update. Should be fixed now.
# 1.2.4
+ Added compatibility patch for MoreEmotes!
# 1.2.3
+ Minor compatibility fixes
# 1.2.2
+ Fixed bug preventing you from buying items in terminal.
# 1.2.1
+ Quick fix for assetbundle not loading.
# 1.2.0
+ Initial official release