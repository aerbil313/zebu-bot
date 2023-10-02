## How to install
First install Nix if you haven't done so already:
```
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```
For more information on installing and uninstalling Nix, you can optionally check <https://zero-to-nix.com/start/install>.

Clone the repository:
```
nix-shell --pure --packages git cacert --run "git clone https://github.com/aerbil313/zebu-bot.git"
```
Inspect the script `install.sh` now if you want. Run the installer:
```
zebu-bot/install.sh
```
Note: It may take a very long time to install the first time you do it.

## How to run
Execute the runner:
```
zebu-bot/run.sh
```
