from pytube import YouTube  
link = input("Video url : ")  
yt = YouTube(link)  
print(yt.title)  
print(yt.thumbnail_url)  
videos = yt.streams.filter(progressive = True)  
i = 1  
for stream in videos:  
    print(str(i)+ " " +str(stream))  
    i += 1  
stream_number = int(input("enter number :"))  
video = videos[stream_number-1]  
video.download()  
video.on_complete(print("Video Downloaded Succesfully ."))  