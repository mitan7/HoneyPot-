# READ THIS!!!
This is a Honey Pot for finding an attackers IP and webhook. You **MUST** go into the .py to change some of the code:

# Changing to YOUR webhook (NEEDED!!!)
Go into the code and change `DEFENDER_WEBHOOK = "https://discord.com/api/webhooks/YOUR_WEBHOOK_HERE" # PUT WEBHOOK HERE` and change the https discord link to yours. 

# (optional) Changing the "Protected By *X*" to your own name
In line `68` (`sub_label = tk.Label(header, text="Protected by Mitan7", font=("Segoe UI", 12, "italic"), bg="#0B3D91", fg="white")`) you can change `Protected by Mitan7` to your name.

# Make into .exe 
Use Pyinistaller (`pip install pyinstaller`) to install Pyinstaller. Then do (windows) `cd path\to\youe\script` and `pyinstaller --onefile --noconsole HoneyPot.py` (you should change the name to like "`InfoStealerBuilder.py`") and in `dist` it should be there (`NAME_OF_FILE.exe`)
