import datetime
import os


def get_comand(init_extraction):
    time_format = '%H:%M:%S'
    rewinds = 5
    capture = 2
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
get_frames('00:01:18')
get_frames('00:01:48')
get_frames('00:01:59')
get_frames('00:02:23')
get_frames('00:02:41')
get_frames('00:03:05')
get_frames('00:05:12')
get_frames('00:09:29')
get_frames('00:12:38')
get_frames('00:18:36')
get_frames('00:19:04')
get_frames('00:19:09')
get_frames('00:19:29')
get_frames('00:20:04')
get_frames('00:20:19')
get_frames('00:20:51')
get_frames('00:21:06')
get_frames('00:21:34')
get_frames('00:21:38')
get_frames('00:22:34')
get_frames('00:23:17')
get_frames('00:25:13')
get_frames('00:27:30')
get_frames('00:27:51')
get_frames('00:28:07')
get_frames('00:28:13')
get_frames('00:29:28')
get_frames('00:29:58')
get_frames('00:36:13')
get_frames('00:37:09')
get_frames('00:38:38')
get_frames('00:40:07')
get_frames('00:40:09')
get_frames('00:48:46')
get_frames('00:55:50')
get_frames('01:00:30')
get_frames('01:06:10')
get_frames('01:11:23')
get_frames('01:16:49')
get_frames('01:22:24')
get_frames('01:22:30')
get_frames('01:22:51')

