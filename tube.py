import tkinter
import customtkinter
from pytube import YouTube
# from sys import argv

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        video.download('C:/Users/User/Downloads/tube')

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        views.configure(text=ytObject.views, text_color="white")
        finishLabel.configure(text="")

        video.download()

        finishLabel.configure(text="Downloaded")  
    except Exception as e:
        finishLabel.configure(text="Download Error", text_color="red")
        print(f"Error: {e}")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

views = customtkinter.CTkLabel(app, text="")
views.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkButton(app, text="")
finishLabel.pack()

pPercentage  = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady= 10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


app.mainloop();
# link = argv[1]
# yt = YouTube(link)

# print("Title: ", yt.title)

# print("Views: ", yt.views)

# yd = yt.streams.get_highest_resolution()

# yd.download('C:/Users/User/Downloads/tube')

