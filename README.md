# osu! Launcher
This repository contains an open-source osu! launcher written in Python. The osu! launcher provides a convenient way to launch the osu! game, osu!lazer, and connect to private servers with a simple and user-friendly interface.

# Features
 - Launches the original osu! game.
 - Launches osu!lazer, the next-generation osu! client.
 - Connects to private servers with a custom server IP using the -devserver method.
 - Saves the server IP for future use.
 - Settings button for easy access to server configuration.

# Usage
1. Click the "Launch osu! button to start the original osu! game."
2. Click the "Launch osu!lazer" button to launch the next-generation osu! client.
3. Use the settings button to specify a custom private server IP.
4. Click the "Launch Private Server" button to connect to the private server with the specified IP.
5. When adding a new server ip, the server_ip.txt file will be created in your current directory, inside the file will be the server ip and you can edit it directly through there if you want to.

# App Preview
![](https://cdn.discordapp.com/attachments/538398613987131422/1125995082240237698/image.png)

# Installation
You can download the executable (only for windows) in the [Releases](https://github.com/artorias305/osu-launcher/releases/) page.

# Build from your device
1. Clone the repository: `git clone https://github.com/artorias305/osu-launcher.git`
2. Install the required dependecies: `pip install -r requirements.txt` or manually `pip install flet pillow` (only library being used).
3. Run the launcher: `python main.py`

# Contributions
Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to submit a pull request. Please make sure to follow the project's coding style and guidelines.

# License
This project is licensed unser the [**MIT LICENSE**](https://opensource.org/license/mit/)
