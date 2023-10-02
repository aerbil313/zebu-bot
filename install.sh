#!/usr/bin/env nix-shell
#! nix-shell -i fish --pure
#! nix-shell -I https://github.com/NixOS/nixpkgs/archive/4ecab3273592f27479a583fb6d975d4aba3486fe.tar.gz
#! nix-shell --packages fish git cacert python3

git clone https://github.com/aerbil313/zebu-bot.git
cd zebu-bot
python3 -m venv .
source bin/activate.fish
pip install -r requirements.txt
exit
