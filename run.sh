#!/usr/bin/env nix-shell
#! nix-shell -i fish --pure
#! nix-shell -I https://github.com/NixOS/nixpkgs/archive/4ecab3273592f27479a583fb6d975d4aba3486fe.tar.gz
#! nix-shell --packages fish cacert python311

argparse --name="run.sh" t/token= -- $argv

if not set -q _flag_token
        echo 'Usage: ./run.sh [ -t | --token ] BOT_TOKEN'
	exit
end

cd zebu-bot 
if test $status != 0
  echo "\nError: Please run this script from the directory which contains the zebu-bot repository."
  exit
end

source venv/bin/activate.fish
python3 src/main.py $_flag_token
