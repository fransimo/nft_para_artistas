import datetime
import os
import io
import random
from PIL import Image, ImageDraw, ImageSequence, ImageFont


def add_text_layer_gif(source_image, dest_image, text):
    font = ImageFont.truetype("CONSOLA.TTF", 45)
    im = Image.open(source_image)

    frames = []
    for frame in ImageSequence.Iterator(im):
        # Draw the text on the frame
        d = ImageDraw.Draw(frame)
        d.multiline_text((12, 22), text, font=font, fill=(0, 0, 0))
        d.multiline_text((10, 20), text, font=font, fill=(255, 255, 255))
        # d.text((10,440), "Not your keys, not your coins!", font=font)
        del d
        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)

        frames.append(frame)

    frames[0].save(dest_image, save_all=True, append_images=frames[1:])


def get_config():
    movie_location = "/home/fran/t/2022-04-05 13-01-39.mkv"
    frame_destination = "/home/fran/synced/in_progress/2022_NFT-para-artistas/NFT_frames"
    return movie_location, frame_destination

def get_frame_sequence_string(init_extraction, rewinds, capture):
    time_format = '%H:%M:%S'
    t_init = datetime.datetime.strptime(init_extraction, time_format)
    t_init_sq = t_init - datetime.timedelta(seconds=rewinds)
    t_end_sq = t_init_sq + datetime.timedelta(seconds=capture)
    t_init_sq_st = t_init_sq.strftime(time_format)
    t_end_sq_st = t_end_sq.strftime(time_format)
    return t_init_sq_st, t_end_sq_st


def get_command(type, init_extraction, rewinds, capture):
    t_init_sq_st, t_end_sq_st = get_frame_sequence_string(init_extraction, rewinds, capture)
    movie_location, frame_destination = get_config()
    sq = init_extraction.replace(":", "_")

    if type == 'PNG':
        dest=f'{frame_destination}/PNGs/{sq}_%05d.png'
        cmd = f'ffmpeg -y -ss {t_init_sq_st} -to {t_end_sq_st} -i "{movie_location}" {dest}'
    elif type == 'GIF':
        dest = f'{frame_destination}/GIFs/{sq}.gif'
        cmd = f'ffmpeg -y -ss {t_init_sq_st} -to {t_end_sq_st} -i "{movie_location}" -f gif  /tmp/tmp.gif'

    return cmd, dest

def get_frames(type, init_extraction, rewinds, capture):
    cmd, dest = get_command(type, init_extraction, rewinds, capture)
    os.system(cmd)
    return cmd, dest


def generate_nft(init_extraction, rewinds=3.5, capture=2):
    texts = ["En los blockchain \ncapaces de contener NFTs \ntodas las operaciones \nson visibles.",
             "Not your keys,\n    not your coins!",
             "Nunca muestres tu 'seed'\n\nQuien la tenga,\n    ¡tiene tu dinero!",
             "Tu 'wallet'\n\n no tiene el dinero,\n tiene las claves para...\n\n\n        ¡firmar!",
             "EL NFT es\n\nun registro de propiedad\n\nde un OBJETO\nen un BLOCKCHAIN,\n\nno de los derechos\nde autor o reproducción.",
             ]

    cmd, dest = get_frames('GIF', init_extraction, rewinds, capture)
    end = len(texts) - 1
    text = texts[random.randint(0, end)]
    add_text_layer_gif('/tmp/tmp.gif', dest, text)


# get_frames('00:01:00')
generate_nft('00:01:13')
# exit(0)
generate_nft('00:01:18', rewinds=5, capture=2)
generate_nft('00:01:48', rewinds=4, capture=2)
# get_frames('00:01:59')
# get_frames('00:02:23')
generate_nft('00:02:41', rewinds=3, capture=2)
generate_nft('00:03:05')
generate_nft('00:05:12', rewinds=4, capture=2)
# get_frames('00:09:29', rewinds=3, capture=1)
generate_nft('00:12:38', rewinds=3, capture=1)
# get_frames('00:18:36', rewinds=3, capture=3)
generate_nft('00:19:04', rewinds=3, capture=5)
# get_frames('00:19:09')
# get_frames('00:19:29', rewinds=3.5, capture=5)
# get_frames('00:20:04', rewinds=3.5, capture=5)
# get_frames('00:20:19')
generate_nft('00:20:51')
# get_frames('00:21:06')
# get_frames('00:21:34')
generate_nft('00:21:38', rewinds=2, capture=3)
generate_nft('00:22:34', rewinds=3.5, capture=4)
# get_frames('00:23:17', rewinds=3.5, capture=4)
# get_frames('00:25:13')
# get_frames('00:27:30', rewinds=3.5, capture=3)
generate_nft('00:27:51', rewinds=2, capture=4)
generate_nft('00:28:07')
generate_nft('00:28:13', rewinds=2, capture=5)
# get_frames('00:29:28')
generate_nft('00:29:58', rewinds=2, capture=2)
# get_frames('00:36:13')
# get_frames('00:37:09')
generate_nft('00:38:38')
generate_nft('00:40:07', rewinds=1, capture=10)
generate_nft('00:48:46', rewinds=5, capture=3)
generate_nft('00:55:50', rewinds=3.5, capture=1)
generate_nft('01:00:33', rewinds=0, capture=2)
generate_nft('01:06:10', rewinds=1, capture=5)
# get_frames('01:11:23')
generate_nft('01:16:49')
generate_nft('01:22:24', rewinds=2, capture=3)
generate_nft('01:22:30', rewinds=2, capture=3)
generate_nft('01:22:40', rewinds=4, capture=10)
generate_nft('01:23:00', rewinds=1, capture=5)

