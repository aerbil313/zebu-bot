#!/usr/bin/env nix-shell
#! nix-shell -i fish --pure
#! nix-shell -I https://github.com/NixOS/nixpkgs/archive/4ecab3273592f27479a583fb6d975d4aba3486fe.tar.gz
#! nix-shell --packages fish cacert python311

cd zebu-bot
python3 -m venv python-venv
source venv/bin/activate.fish
pip install -r src/requirements.txt
exit
