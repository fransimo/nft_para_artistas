#!/bin/bash

ff() {
  sq=$1
  st=$2
  end=$3
  ffmpeg -ss ${st} -to ${end} -i "$HOME/t/2022-04-05 13-01-39.mkv" /home/fran/synced/in_progress/2022_NFT-para-artistas/NFT_frames/${sq}_%05d.png
}

# -5seg +1seg

# ff 001 01:00 01:03
ff 003 01:43 01:44