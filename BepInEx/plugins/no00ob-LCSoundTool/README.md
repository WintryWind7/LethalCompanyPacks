# LC Sound Tool
This mod is by default **FULLY CLIENT SIDE**, but if you enable the networking feature in the config it requires everyone to have it installed and for everyone to have the networking feature on.

Simplistic Lethal Company sound tool/API and debugger. Patches all native Unity AudioSource components allowing you to dynamically replace any sound in the game at the final stages of playback with one or multiple random options with specified chances by simply supplying new audio clip(s) and the original clip's name to this mod. Let's you easily load your own custom .wav, .ogg or .mp3 sound files for use with your own mods. Experimental networking for sending and syncing audio clips across all of the connected players and syncing the Unity randomization seed for consistant random clips. Lastly, optionally allows logging all AudioSources playback, including PlayOneShot, PlayClipAtPoint etc. and the names of each audio clip playing into the BepInEx console and log when you press the F5 key. More in depth logging can be toggled with LeftAlt + F5 and more informational logs with LeftControl + F5.

## ATTENTION
This mod won't work without a mod of your own that does the replacing. This mod is just purely a tool/API for replacing, loading and networking sound files. To be able to replace sound without creating a mod of your own you can try the following seperate mod utilizing this tool: https://thunderstore.io/c/lethal-company/p/Clementinise/CustomSounds/

## Features

- Press F5 to log all audio playback to BepInEx console.
- Load your own custom .wav, .ogg or .mp3 audio files for use within your mod.
- Replace any audio clip with another one or multiple random ones with specified chances for playback.
- (Optional) Send audio clips over the network and sync the hosts clips with all clients.
- (Optional) Sync the Unity randomization seed with all players.

## Installation

Install like any other BepInEx mod, either manually or with mod manager of your choice. I recommend r2modman.

When installing manually, install the mod to the following directory: `\GAME_LOCATION\Lethal Company\BepInEx\plugins`

## Usage/Examples

Check the [mod wiki](https://thunderstore.io/c/lethal-company/p/no00ob/LCSoundTool/wiki/828-audio-logging/) for detailed instructions on how to use this mod as mod developer or user.

And for more in-depth developer example see the following github repo: https://github.com/no00ob/LCSoundToolTest

## FAQ

#### Why are none of the logs showing up?

Make sure you have at least the following BepInEx.cfg settings:
- [Chainloader] HideManagerGameObject = true
- [Logging.Console] Enabled = true
- [Logging.Console] LogLevels = Fatal, Error, Info, Debug, Warning
- Possibly [Logging.Disk] WriteUnityLog = false

If nothing else works you can try my BepInEx.cfg from here: https://pastebin.com/LdsPhH5U

If they're still not showing up just shoot me a msg in Discord (@no00ob) and we can try to figure it out.

#### Why does this one sound not show up in log and I cannot replace it?

This should not be happening. If you are sure you found a sound that does not work, please take note of the name and where it plays and send it over to me in Discord as either a DM or on the Lethal Company Modding Server in the LC Sound Tool forum as a post.

#### Why is the networking not working?

Make sure you turn the feature on in the mod config. When networking is turned on everyone needs LCSoundTool installed to join a lobby or else you will get an error.

#### Can you use this tool to record sounds or interact with the voice chat?

No, not at the moment. I might look into this later. If you want enemies to use player voices check out SkinWalkers mod.

#### What is the performance impact of this tool compared to just manual replacement?

I have not done any major testing. In theory this should add very tiny slight delay and overhead to any audio playback, but no major delays or issues have been encountered. The programming in this game is so messy sometimes that finding certain audio clips was painful enough where I just decided that a tool like this might come in handy.

#### Can you add this or that?

Depends totally on what you're asking. If you want a new feature that has something to do with this mods original scope and improves it in a meaningful way, feel free to shoot me a message on Discord as a DM or on the Lethal Company Modding Server in the LC Sound Tool forum as a post or in Github as an issue and I'll take a look. Otherwise no.

#### Does this mod work with other Unity games?

Any version prior to 1.2.0 should and versions past that will not work. I tried the pre 1.2.0 version with my Unity 2022.3.x game and it did work for it too. The mods replacing the audio do not however, as different games use different sounds obviously.

#### Can I contribute somehow?

Yes. If you find any bugs or errors let me know and feel free to send pull requests my way if you feel like you can provide better programming, bug fixes or more features.

## Config

The config can be found from: `\GAME_LOCATION\Lethal Company\BepInEx\config\LCSoundTool.cfg`

or if you're using mod managers you can find the config from here: [Example](https://i.imgur.com/OZAgeNL.png)

```
## Settings file was created by plugin LC Sound Tool v1.4.0
## Plugin GUID: LCSoundTool

[Experimental]

## Whether or not to use the networking built into this plugin. If set to true everyone in the lobby needs LCSoundTool installed and networking enabled to join.
# Setting type: Boolean
# Default value: false
EnableNetworking = true

## Whether or not to sync the default Unity randomization seed with all clients. For this feature, networking has to be set to true. Will send the UnityEngine.Random.seed from the host to all clients automatically upon loading a networked scene.
# Setting type: Boolean
# Default value: false
SyncUnityRandomSeed = true

## How long to wait between checks for new playOnAwake AudioSources. Runs the same patching that is done when each scene is loaded with this delay between each run. DO NOT set too low or high. Anything below 10 or above 600 can cause issues. This time is in seconds. Set to 0 to disable rerunning the patch, but be warned that this might break runtime initialized playOnAwake AudioSources.
# Setting type: Single
# Default value: 90
NewPlayOnAwakePatchRepeatDelay = 90
```

## Known Issues

- Currently should be none :)