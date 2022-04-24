#!/bin/bash

ff() {
  sq=$1
  st=$2
  end=$3
  echo ffmpeg -ss ${st} -to ${end} -i "$HOME/t/2022-04-05 13-01-39.mkv" ${sq}_%05d.png
}

# +2seg

ff 001 01:00 01:03
ff 002 01:13 01:14