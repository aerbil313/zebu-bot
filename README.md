## How to install
First follow [this guide](https://docs.pycord.dev/en/stable/discord.html#discord-intro) to create a bot user. You can skip the 6th step of "Inviting Your Bot", because we only need the permissions in the 5th step. You can use the `spiral.jpg` photo in the repository for your application.

You can run this bot [everywhere](https://github.com/determinateSystems/nix-installer#the-determinate-nix-installer) nix runs, including Windows (via WSL), Linux and MacOS. First install Nix if you haven't done so already:
```
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```
For more information on installing and uninstalling Nix, you can check <https://zero-to-nix.com/start/install>.

Clone the repository:
```
nix-shell --pure --packages git cacert --run "git clone https://github.com/aerbil313/zebu-bot.git"
```
If you want to, you can inspect the script `install.sh` now. Run the installer:
```
zebu-bot/install.sh
```
Note: It may take a very long time to install the first time you do it.

## How to run
Execute the runner with the token you copied earlier while following the guide:
```
zebu-bot/run.sh --token BOT_TOKEN
```
