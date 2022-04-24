
f_figlet() {
  echo $1
  figlet -f $1 "NFT  para  Artistas  por  Fran  Simo'"
}

export -f f_figlet

find /opt/homebrew/opt/figlet/share/figlet/fonts/C64-fonts -name \*.flf -exec bash -c 'f_figlet "{}"' \;