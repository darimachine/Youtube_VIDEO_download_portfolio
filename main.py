from pytube import YouTube
import ffmpeg



link = input("Enter Your Link")
yt = YouTube(link)
print(yt.title)
print(yt.thumbnail_url)
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)

dn_option = int(input("Enter the option: "))
dn_video = videos[dn_option]
dn_video.download()
# Video audio mixing
# dn_option = int(input("Enter the option for audio: "))
# dn_video = videos[dn_option]
# format = dn_video.mime_type
# format = format[6:]
#
# dn_video.download()
#
# video_stream = ffmpeg.input(f'{yt.title}.{format}')
# audio_stream = ffmpeg.input(f'{yt.title}_audio.mp4')
# ffmpeg.output(audio_stream, video_stream, f'{yt.title}_final.mp4').run()

print("Downloaded succesfully")

