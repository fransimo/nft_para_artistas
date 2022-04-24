import datetime
import os


def get_comand(init_extraction):
    time_format = '%H:%M:%S'
    rewinds = 5
    capture = 1
    movie_location = "/home/fran/t/2022-04-05 13-01-39.mkv"
    frame_destination = "/home/fran/synced/in_progress/2022_NFT-para-artistas/NFT_frames/"

    sq = frame_destination + init_extraction.replace(":", "_")
    t_init = datetime.datetime.strptime(init_extraction, time_format)
    t_init_sq = t_init - datetime.timedelta(seconds=rewinds)
    t_end_sq = t_init_sq + datetime.timedelta(seconds=capture)
    t_init_sq_st = t_init_sq.strftime(time_format)
    t_end_sq_st = t_end_sq.strftime(time_format)
    return f'ffmpeg -ss {t_init_sq_st} -to {t_end_sq_st} -i "{movie_location}" {sq}_%05d.png'


def get_frames(init_extraction):
    cmd = get_comand(init_extraction)
    print(cmd)
    os.system(cmd)


get_frames('00:01:00')
get_frames('00:01:13')