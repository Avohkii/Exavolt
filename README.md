# Exavolt - The Metal Arms Mod Loader

## Where to get Binaries
Download from [Releases](https://github.com/dj0wns/Exavolt/releases)

## Basic Usage
1. Fill the `mods/` directory with zipfile mods (available in the metal arms modding discord: [https://discord.gg/3Dztwe6Wcy](https://discord.gg/3Dztwe6Wcy))
2. Drag a Vanilla Metal Arms NTSC Gamecube iso file onto the `exavolt.exe`
3. Enable Extended memory in Dolphin Settings and slide the slider to the maximum value
4. Open the mod.iso in Dolphin and enjoy your mods!

## Setting up Repository
` git clone https://github.com/dj0wns/Exavolt`  
` cd Exavolt`  
` Git submodule update --init --recursive`  

## Command Line Options
```
usage: exavolt.py [-h] [input_iso] [output_iso] [mod_folder]

Add mods to Metal Arms ISO file

positional arguments:
  input_iso   A valid vanilla Metal Arms Iso File
  output_iso  Name of the new output iso which will be produced
  mod_folder  Folder containing all mods which the user will have the option
              of adding

options:
  -h, --help  show this help message and exit
```

### Default Command Line Arguments
`input_iso: "metalarms.iso"`  
`output_iso: "mod.iso"`  
`mod_folder: "mods/"`  

## Compiling a release
`python -m PyInstaller -F exavolt.py --add-data files\*;files --add-data lib\pyiiasmh\lib\win32\*;lib\win32 --add-data asm\*;asm --add-data lib\pyiiasmh\__includes.s;. --icon="icon.ico"`

## Thanks

Huge thanks to Vissova for the logo
