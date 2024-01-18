-   **1.5.0**

    -   Added support for AudioSource names as filters to where sounds can play. No more same sound from different sources!
    -	Fixed a bug where AudioSources using the standard Play() would not randomize properly. 
    -	Added a config option to turn informational debugging on by default on launch.
    -	Some minor tweaks to logging again. Mostly the same this time too. Cleaned up some useless messages, fixed typos, etc.
    -	Added few new mod API methods and updated existing ones. You can now use some of the methods with different parameters than before.

-   **1.4.0**

    -   Added support for Ogg Vorbis and Mpeg MP3 files. Now any of the 3 file types should work. Wav, ogg or mp3.
    -	Reworked playOnAwake patching. Hopefully now ALL playOnAwake AudioSources and sounds should work without any problems. 
    -	Added a config option to let the mod patch any playOnAwake AudioSources that get created later during a game, as before it only ran when a new Unity scene was loaded. The option is for the delay between each runtime patch.
    -	Added config option to sync host's Unity built in randomization seed with all clients. Random sounds should be the same for everyone with this on.
    -	Some minor tweaks to logging. Mostly cleaned up some useless messages, fixed typos and added a new keybind for informational logs, F5 + LeftControl.
    -	Added few new mod API methods and updated existing ones. You can now add sounds with multiple random variants from code without having the chance specified in the file name and small tweaks like that.

-   **1.3.2**

    -   Small bug fixes.
    -	Made networking optional. It was never meant to be forced on. It can now be toggled from the config file.

-   **1.3.1**

    -   Changed the random clip seperator from "_" to "-".


-   **1.3.0**

    -   Internal restructure of multiple parts of the mod. Shouldn't change previous behaviour.
    -	Added support for random replacement clips. One vanilla sound can now have new multiple random clips with set chances that play randomly when the vanilla sound would.
    -	Fixed multiple small bugs. AudioSources with playOnAwake set to true should now play more than once when the scene is not reloaded between playback.
    -	Experimental networking for Unity AudioClips. Send AudioClips over the network to all connected players, also optionally sync all of the networked clips of the host to all clients.
    -	Minor tweaks for game v45

-   **1.2.2**

    -   Added support for mod managers. This changes the folder structure and loading of custom sounds a bit and all mods will need to be updated to work with mod managers. Old mods will continue to work with the newest release when manually installed. Mods only need to update to support mod managers, otherwise no sounds will load when using a mod manager.

-   **1.2.1**

    -   Minor edits to mod page.

-   **1.2.0**

    -   Added ability to load sound files from plugins folder, more in depth logging option and support for most AudioSources with playOnAwake flag set to true.

-   **1.1.1**

    -   Minor edits to mod page.

-   **1.1.0**

    -   Added a way to replace any in game audio clip by a custom one. Mod released on thunderstore.

-   **1.0.0**

    -   Mod released on github.
