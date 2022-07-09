# Steamy Sunshine

 - Generates a apps_windows.json file for Sunshine(Moonlight for the rest of
   us) Stream.
 - The generated file contains individual Application entries for every
   currently installed Steam game.
 - This is useful for example with Anbernic style devices running JELOS,
   Batocera, AmberElec, etc.
 - In the case of JELOS, it is especially useful as that system provides an
   automatic Emulation Station game import of all advertised Moonlight games, at
   which point you can run screenscraper to grab some nice images / preview
   videos that will be presented in Emulation Station.
 
## Configuration
 
 - Install Sunshine Stream on some fancy pants gaming omputer
 - Update `WINDOWS_STEAMAPPS_DIR` if your `steamapps` directory differs from the
   existing value.
 - Update `APPS_WINDOWS_JSON_FILEPATH` to point to a valid `apps_windows.json`
   filepath that the locally installed Sunshine instance looks at.
 - Update `EXCLUDE_APPIDS` to exclude perticular Steam App Ids if you wish to not
   have entries generated for them.
 - Run `python steamy-sunshine.py`
 - Restart the `sunshinesvc` Windows Service
