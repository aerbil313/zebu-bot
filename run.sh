#!/usr/bin/env nix-shell
#! nix-shell -i fish --pure
#! nix-shell -I https://github.com/NixOS/nixpkgs/archive/4ecab3273592f27479a583fb6d975d4aba3486fe.tar.gz
#! nix-shell --packages fish cacert python3

cd zebu-bot
source bin/activate.fish
python3 zebu-bot/src/main.py
