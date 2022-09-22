#https://stackoverflow.com/questions/64670507/pytube-youtube-object-has-no-attribute-filter
from pytube import YouTube

link = "https://www.youtube.com/watch?v=zo_P8pAdqaA"

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").get_highest_resolution().download(output_path = r"C:\Users\Stanley\Desktop\Free", 
filename = "ZwagLeona")
except:
    print("Some Error!")
print('Task Completed!')