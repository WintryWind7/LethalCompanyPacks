To add custom recipes to SCP 914, a json file is used. See default.json for an example for how to add your own conversions (it is recommended you don't modify this file and instead make your own).
Each item conversion entry has 6 parts; the name of the item to convert, and a list for each conversion setting corresponding to the name of the item (or items for a chance) to convert to.
If the output string is "@", the item will not be changed (only the charge of battery items and scrap value of scrap items will be changed)
If the output string is "*", the item will be destroyed.
See the following example:
{"ItemName":"paper", "RoughResults":["*"], "CoarseResults":["*"], "OneToOneResults":["@", "pen"], "FineResults":["book", "book", "folder"], "VeryFineResults":["origami"]}
When a paper item is put in SCP 914, the results will be (assuming all these items exist):
	Rough/Coarse	: The paper is destroyed.
	1:1				: The paper has a 50/50 chance of either coming out unchanged or becoming a pen.
	Fine			: The paper has a 67% chance of becoming a book, or a 33% chance of becoming a folder.
	Very Fine		: The paper will become origami.
Names are automatically converted to lowercase when read, matching is based on the item data name (the same text that appears when you scan an item).

*For users*:
1. Create a new file named whatever you want with the extension .json
2. Add square braces that will encompass the whole file
3. In the square braces, add entries like the above. Every entry except the last requires a comma
4. Place your new file in the same folder as default.json (the folder this readme is found in)

*For mod developers*:
Follow basically the same steps as above for your custom items, but you'll need to make a folder called "badhamknibbs-scp914-recipes" in the plugins folder of your mod when uploading (Thunderstore/mod managers will put it in its own folder, manual installers will need to move it to a subfolder themselves)
SCPCBDunGen will search all folders in the plugins directory, searching for a sub-folder named "badhamknibbs-scp914-recipes" and will attempt to load all .json files in that directory. It will NOT detect a folder called "badhamknibbs-scp914-recipes" in the plugin folder.