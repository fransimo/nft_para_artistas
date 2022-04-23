# Así se han creado los NFTs del taller

## Textos

```
figlet -c -w 132 -f smmono9 < intro.txt
```

## Conversión de la película

```
vlc --vout=caca Tiempos_Modernos.mkv
```

## Superposición de la Matrix (Ghost in the shell)

```
docker run -ti geertjohan/gomatrix -k
```
## Mezcla

La mezcla de las dos fuentes de imagen se hizo en OBS.

## Extracción de los frames

```
ffmpeg -ss 01:07 -to 01:10 -i 2022-04-05\ 13-01-39.mkv %05d.png
```