from pytube import YouTube
from sys import argv

link = argv[1]

#link= "https://www.youtube.com/watch?v=WTpXukCywiw"
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download(r'C:\Users\Bernardo\Desktop\Carrera Developer\Cuarto Bimestre\Infraestrucuta I\3-Simple-Python-Projects-master\YTfolder')