# The monsters have learned how to mimic the voices of your friends.

## Information
Enemies will now learn the voices of your friends and be able to repeat them.

## Discord server: https://discord.gg/8VXmnSfENj

## Credits
[![](https://cdn.discordapp.com/attachments/753742297153273867/1195825026105098380/image.png?ex=65b565d7&is=65a2f0d7&hm=68399b82b2ff4ee98216bc83759acd5a8f07c0ecfe0a7be12070a29a1a77f3b6&)](https://www.youtube.com/RugbugRedfern)

Programming by Rugbug Redfern

https://www.youtube.com/RugbugRedfern

Playtesting by Dubscr

https://www.youtube.com/dubscr

## Configuration
All players who want to hear voices need the mod installed. This is a client-side mod. Make sure your mic is enabled in-game.

It can be configured through the config file in r2modman or manually in the .cfg file to enable/disable voices for specific creatures and adjust the frequency of voice lines. The host's config will be automatically synced to other players in the lobby.

## FAQ

### Does this mod use AI?
No! There is no AI involved at all in this mod.

### Does it fill up my hard drive with audio clips?
No, files are deleted automatically a few seconds after they are recorded and moved to memory. Data stored in memory is monitored to be kept below a reasonable usage. All data is wiped from memory when the game is closed.

### Does this mod steal recordings of my or my friends' voices?
No. All voice data is handled locally on your computer and is never sent to anyone. Additionally, it is wiped when you close the game.

### How does it work?
It records audio and plays it back at random times from enemies that you choose. Often times it results in some pretty creepy coincidences!

### Can I play alone?
No, you need friends.

### My game is stuttering, why?
Some players may experience stutters every few seconds. To fix this:
- Move Lethal Company's install location to an SSD.
If that doesn't work, you can try the [Skinwalkers Experimental](https://thunderstore.io/c/lethal-company/p/RugbugRedfern/SkinwalkersExperimental/) version which fixes stutters but may cause issues for some players.

## Changelog

### 4.0.1
- Updated README to reflect v2
- The v3 version is still playable on the new branch: [Skinwalkers Experimental](https://thunderstore.io/c/lethal-company/p/RugbugRedfern/SkinwalkersExperimental/)

### 4.0.0
- Reverted to v2 due to stability issues with the v3 release.

### 3.0.1
- Reduced max audio clips back to 200

### 3.0.0
- Fixed the issue that some players would experience where every few seconds their game would stutter.
- The game no longer writes any files to disk. Everything is now processed in memory. Yay!
- Increased max audio clips from 200 to 500

Thanks to Nick for being a good idea bouncer

### 2.0.6
- Improved clarity of some log messages
- Fixed an issue that may have been caused by other mods adding enemies

### 2.0.5
- Updated for Lethal Company v48
- Added an option to the config to disable voices from modded enemies.

### 2.0.4
- Updated for Lethal Company v47
- Attempted to reduce the stutter that can affect some players by reducing Dissonance log output (1A3)
- Fixed an issue where the Ghost Girl could play voice lines for players she was not haunting (1A3)

### 2.0.3
- Updated 2.0.2 patch notes with something I forgot to note

### 2.0.2
- Fixed a memory leak
- The developer of Lethal Progression fixed the conflict between the mods
- Fixed an issue where spectators would not hear monster voices. This doesn't mean spectators hear the same voices as who they are spectating, but the same client-side voices that everyone hears normally.

### 2.0.1
- Recompiled for BepInEx 5.4.2100 for Thunderstore compatibility

### 2.0.0
- Enemies no longer play voice lines when dead
- Removed some unnecessary logs
- Added Masked and Nutcracker to the config

### 1.0.8
- Updated for Lethal Company v45
- Actually fixed the bug where audio would randomly play outside (for alive players)
- Removed the 404 error
- Removed the LC_API dependency

### 1.0.7
- Fixed an issue where audio would randomly play outside

### 1.0.6
- Fixed a bug introduced in 1.0.5 where audio wouldn't play

### 1.0.5
- Updated website URL to go to the Discord server
- Attempted a fix for some occasional audio issues outside

### 1.0.4
- Added a config which can be configured in r2modman or manually in the .cfg file. This allows you to enable/disable voices for specific creatures and adjust the frequency of voice lines.
- Fixed an issue where some creatures would be quieter than others
- Fixed an issue where when playing the game for a long period of time audio clips wouldn't be removed

### 1.0.3
- Fixed an issue where BepInEx would destroy the GameObject, making the mod not work.

### 1.0.2
- Fixed the error.

### 1.0.1
- Attempted to fix an error that prevented the mod from starting.

### 1.0.0
- Initial Release