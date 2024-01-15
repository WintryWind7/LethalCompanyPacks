# 3rd Person

Installation
-

- Download and place 3rdPerson.dll in the BepInEx Plugins folder (Lethal Company\BepInEx\plugins)
- Launch the game and 3rdPerson will start working, default keybind is C and can be changed (BepInEx\config\verity.3rdperson.cfg)
- You can enabled MoreCompany support by editing the Config (BepInEx\config\verity.3rdperson.cfg)

TODO
-

- Raycast and visually display what you're looking at.
- Collision detection to prevent camera clipping.

Changelog
-

### Version 1.0.1
- You can now pause the game and use the terminal while in 3rd person.

### Version 1.0.2
- Fixed all HUD problems, everything should now work as if you were in first person.
- PlayerModel quality has been fixed.

### Version 1.0.3
- You no longer need to set HideManagerGameObject to true in the BepInEx Config

### Version 1.0.4
- Now supports QuackAndCheese's Mirror Decor. (Thanks to QuackAndCheese) (https://thunderstore.io/c/lethal-company/p/quackandcheese/MirrorDecor/)
- Also now supports MoreCompany's Cosmetics. (Thanks to QuackAndCheese) (https://thunderstore.io/c/lethal-company/p/notnotnotswipez/MoreCompany/)

### Version 1.0.5
- Third Person will not activate while in terminal.
- Third Person camera will no longer work if you're dead.

### Version 1.0.6
- Third Person will not activate while in chat.
- You can now customize camera position/offset in the config file.

### Version 1.0.7
- UI is no longer in world space, so it won't clip through objects now! (some visual issues, will be fixed soon.)

### Version 1.0.8
- Camera no longer breaks when dying.
- Added Orbiting to the 3rd Person camera, can be activated by holding down middle mouse button (can be chanegd in config).
- Added a check for if the Centipede is on your head, if so it will toggle first person and not let you re-activate it until its off.

### Version 1.0.9
- Fixed Centipede checks

### Version 1.1.0
- Updated cullingmask to current game version 45 gameplay camera.