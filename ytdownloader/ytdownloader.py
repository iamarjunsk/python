from pytube import YouTube

link = input("Enter Link: ")

yt = YouTube(link)

print(yt.streams)

# ys = yt.streams.get_highest_resolution()
# ys.download()