
# maya_fspy

Simple UI to import fSpy files into Autodesk Maya

## What is this?

This is the non-official importer for fSpy JSON data into Autodesk Maya. [fSpy](https://github.com/stuffmatic/fSpy) is an open source, cross-platform app for still image camera matching. See [fspy.io](https://fspy.io/) for more info.

If you have found this tool helpful in any way, please consider donating to the original creators on the [fspy.io](https://fspy.io/) website.

This is by no means a perfect import and some tweaks might be required, but it's sure as hell better than placing an image plane and camera by hand.

The below images show fSpy project (top) and a matching Maya camera created by the importer (bottom).

![Image of fspy](https://github.com/JustinPedersen/maya_fspy/blob/master/images/fspy.png)
![Image of maya](https://github.com/JustinPedersen/maya_fspy/blob/master/images/maya_01.png)
![Image of maya](https://github.com/JustinPedersen/maya_fspy/blob/master/images/maya_02.png)

## Compatibility

| Maya Version | Python Version | Qt Binding | Status |
|--------------|----------------|------------|--------|
| Maya 2025+   | Python 3.11+   | PySide6    | ✅ Supported |
| Maya 2022-2024 | Python 3.9/3.10 | PySide2  | ✅ Supported |
| Maya 2018-2021 | Python 2.7   | PySide2    | ✅ Supported |

**Note:** The plugin uses native Maya commands (maya.cmds) and does not require PyMEL.

## Installing and Running

### Installation Paths

Install the plugin to your Maya scripts directory based on your operating system:

#### Windows
```
C:\Users\<username>\Documents\maya\<version>\scripts\maya_fspy
```

#### macOS
```
/Users/<username>/Library/Preferences/Autodesk/maya/<version>/scripts/maya_fspy
```

#### Linux
```
/home/<username>/maya/<version>/scripts/maya_fspy
```

### Installation Methods

#### Option 1: Download Release (Recommended)
1. Download the latest zip file from [Releases](https://github.com/JustinPedersen/maya_fspy/releases)
2. Unzip it into your Maya scripts folder at the path above
3. Make sure the final structure is: `scripts/maya_fspy/src/maya_fspy/...`

#### Option 2: Git Clone
```bash
cd /path/to/maya/<version>/scripts
git clone https://github.com/JustinPedersen/maya_fspy.git
```

### Running the Plugin

Paste the following code into the Maya Script Editor in a Python tab and run:

```python
import maya_fspy.ui as mfspy_ui
mfspy_ui.maya_fspy_ui()
```

**Tip:** Create a shelf button for easier access! Just drag the Python code from the Script Editor to your shelf.

## Use

### FSPY Application

| Setting | Value |
|---------|-------|
| **Vanishing Point Axis 1** | -Z |
| **Vanishing Point Axis 2** | -X |
| **Reference Distance** | Along the y-axis |

1. Load your image in fSpy and configure the perspective lines
2. **Important:** Configure the settings as shown in the table above
3. Export camera parameters as JSON: `File > Export > Camera parameters as JSON`
4. Make sure the exported file has the `.json` extension (not `.fspy`)

![fSpy settings](https://github.com/JustinPedersen/maya_fspy/blob/master/images/fspy.png)

### Maya

![ui](https://github.com/JustinPedersen/maya_fspy/blob/master/images/ui.png)

1. Click the **JSON** button and navigate to the JSON file exported from fSpy
2. Click the **Image** button and navigate to the same image used within fSpy
3. Click **Import!**
4. A group with a new camera and image plane will be created

**Note:** You may need to reposition/scale this group depending on your needs. The camera's transforms are locked by default to prevent accidental changes, but they can be safely unlocked and tweaked if needed.

## Troubleshooting

### Common Issues

**Q: The importer doesn't work or throws an error**
- Make sure you exported a `.json` file from fSpy, not a `.fspy` project file
- Verify your Maya version is 2018 or newer
- Check that the fSpy settings match the required configuration (see table above)

**Q: The camera perspective doesn't match my image**
- Double-check the vanishing point axes in fSpy are set to `-Z` and `-X`
- Verify the reference distance is set to "Along the y-axis"
- Make sure you're using the same image in both fSpy and Maya

**Q: ImportError when running the plugin**
- Ensure the folder structure is correct: `maya/scripts/maya_fspy/src/maya_fspy/`
- Try restarting Maya after installation
- Check that you're using a compatible Maya version (2018+)

**Q: The created camera group is too large/small**
- The imported group can be freely scaled and positioned as needed
- This is normal and depends on your scene's scale and the reference distance set in fSpy

## Changelog

### Version 2.0.0
- Added Maya 2025+ support with PySide6
- Replaced PyMEL with native maya.cmds for better compatibility
- Added Python 2/3 compatibility improvements
- Improved error handling and null checks
- Updated documentation with compatibility matrix

### Version 1.3.0
- Added PySide6/PySide2 compatibility layer
- Python 3 improvements

### Version 1.2.0
- Initial public release
- Support for Maya 2018-2024

## Credits

**Created by:** Justin Pedersen

**Special Thanks:**
- The [fSpy team](https://github.com/stuffmatic/fSpy) for creating this amazing camera matching application
- Jascha Wohlkinger for assistance with Maya matrix transformations

If you find this tool helpful, please consider supporting the original fSpy developers at [fspy.io](https://fspy.io/)

