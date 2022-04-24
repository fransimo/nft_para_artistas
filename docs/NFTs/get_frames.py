import datetime
import os


def get_comand(init_extraction, rewinds, capture):
    time_format = '%H:%M:%S'

    movie_location = "/home/fran/t/2022-04-05 13-01-39.mkv"
    frame_destination = "/home/fran/synced/in_progress/2022_NFT-para-artistas/NFT_frames/"

    sq = frame_destination + init_extraction.replace(":", "_")
    t_init = datetime.datetime.strptime(init_extraction, time_format)
    t_init_sq = t_init - datetime.timedelta(seconds=rewinds)
    t_end_sq = t_init_sq + datetime.timedelta(seconds=capture)
    t_init_sq_st = t_init_sq.strftime(time_format)
    t_end_sq_st = t_end_sq.strftime(time_format)
    cmd = f'ffmpeg -y -ss {t_init_sq_st} -to {t_end_sq_st} -i "{movie_location}" {sq}_%05d.png'
    cmd = f'ffmpeg -y -ss {t_init_sq_st} -to {t_end_sq_st} -i "{movie_location}" -f gif {sq}.gif'
    return cmd


def get_frames(init_extraction, rewinds=3.5, capture=2):
    cmd = get_comand(init_extraction, rewinds, capture)
    print(cmd)
    os.system(cmd)


get_frames('00:01:00')
get_frames('00:01:13')
get_frames('00:01:18')
get_frames('00:01:48', rewinds=4, capture=2)
get_frames('00:01:59')
get_frames('00:02:23')
get_frames('00:02:41', rewinds=3, capture=2)
get_frames('00:03:05')
get_frames('00:05:12', rewinds=4, capture=2)
get_frames('00:09:29', rewinds=3, capture=1)
get_frames('00:12:38', rewinds=3, capture=1)
get_frames('00:18:36', rewinds=3, capture=3)
get_frames('00:19:04')
get_frames('00:19:09')
get_frames('00:19:29', rewinds=3.5, capture=5)
get_frames('00:20:04', rewinds=3.5, capture=5)
get_frames('00:20:19')
get_frames('00:20:51')
get_frames('00:21:06')
get_frames('00:21:34')
get_frames('00:21:38' , rewinds=2, capture=3)
get_frames('00:22:34', rewinds=3.5, capture=4)
get_frames('00:23:17', rewinds=3.5, capture=4)
get_frames('00:25:13')
get_frames('00:27:30', rewinds=3.5, capture=3)
get_frames('00:27:51', rewinds=2, capture=4)
get_frames('00:28:07')
get_frames('00:28:13', rewinds=2, capture=5)
get_frames('00:29:28')
get_frames('00:29:58', rewinds=2, capture=2)
get_frames('00:36:13')
get_frames('00:37:09')
get_frames('00:38:38')
get_frames('00:40:07', rewinds=1, capture=10)
get_frames('00:48:46', rewinds=5, capture=3)
get_frames('00:55:50', rewinds=3.5, capture=1)
get_frames('01:00:33', rewinds=0, capture=2)
get_frames('01:06:10', rewinds=1, capture=5)
get_frames('01:11:23')
get_frames('01:16:49')
get_frames('01:22:24', rewinds=2, capture=3)
get_frames('01:22:30',rewinds=2, capture=3)
get_frames('01:22:40', rewinds=4, capture=10)
get_frames('01:23:00', rewinds=1, capture=5)

