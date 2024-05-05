﻿# Capture Patcher Tool

Do you find yourself in a situation where you have a rig with multiple universes but only a Capture Solo license? While you can design your project in the Solo edition, you're restricted to patching just one universe of fixtures.

You might consider using Capture Demo, but there's a catch. With the Demo, you're limited to 90 minutes of previz before it ends, and within this time frame, you must patch all the fixtures.

Introducing my tool: easily edit the CSV fixture data file exported from Solo and import it into Capture Demo, saving valuable time.

## How It Works:

1. Draw your project as usual in Capture Solo (without adding the patch).
2. Export the Fixture Data file into CSV format from the export menu.
   - Optionally, export the project for a different version of Capture to use the Demo without removing your license.
3. Open the terminal in the folder where the file is located and use the script to add patch information.
4. Open the project in Capture Demo and effortlessly import the new Fixture Data file with all the patches.

Enjoy the convenience! Patch all your fixtures in a flash without wasting any time. And when the 90 minutes are up, simply close, reopen, and reimport the file.

## Modes Explanation

First of all let's analyze a CSV file exported from Capture. These are the field where this script works on:
1. Fixture: this is the name of the fixture in the Capture library. **Do not change that** The script use this field to group fixture, so let you choose a fixture type and sequentially patch all fixture inside that "family"
2. Circuit: this is the place you can enter an electric circuit. We'll use this field to write down (manually or with Capture sequential tool) the dmx addresses of the fixture. Capture Solo/Duet/Quartet let's you patch only a fixed amount of universes based on your licence, this way **you can bypass this limit** and write whatever address you want inside the circuit field. 
3. Patch: this is the real dmx address used by Capture. The script makes the hard work for you, dynamically populating this field according the desidered mode 
4. Note: this is a multi purpose field, you can enter anything here. You can The script 
