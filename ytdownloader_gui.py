import tkinter as tink
from pytube import YouTube
from tkinter import ttk


def SearchAction(label):
    yturl = link_field.get()
    def Search():
        vid_details['text'] = "Title : "+ ytvideo.title
        download_btn['state'] = 'normal'
    try:
        if yturl != "":
            vid_details['text'] = "Searching..."
            ytvideo = YouTube(yturl)
            vid_details.after(3000,Search)
    except:
        vid_details['text'] = "Try again entering valid URL !"

def DownloadVideo(label):
    yturl = link_field.get()
    ytpath=path_field.get()
    def DoIt():
        ytstream.first().download(str(ytpath))
        download_view['text']="Video downloaded sucessfully !"
    try:
        if yturl != "":
            ytvideo = YouTube(yturl)
            if ytpath != "":
                download_view['text'] = "Starting Download..."
                ytstream = ytvideo.streams
                download_view.after(3000, DoIt)
    except:
        print("Oops, something went wrong !")

body=tink.Tk()
body.title("YT Video Downloader")
body.maxsize(width=1080, height=720)
body.minsize(width=500, height=400)

label=tink.Label(body, text="Welcome to YT Video Downloader ! ", fg="green", font="Verdana 12")
label.pack()

link_section=ttk.Frame(body)
link_box=ttk.Label(link_section, text="Link : ", font="Verdana 10")
link_field=ttk.Entry(link_section, width=50)
search_btn=ttk.Button(link_section, text="Search", command=lambda:SearchAction(vid_details))
link_section.pack()
link_box.pack(side="left")
link_field.pack(side="left")
search_btn.pack(side="right")

details_section=ttk.Frame(body)
vid_details=tink.Label(details_section, text="", font="Verdana 10 bold")
details_section.pack()
vid_details.pack(side="bottom")

path_section=ttk.Frame(body)
path_box=ttk.Label(path_section, text="Path : ", font="Verdana 10")
path_field=ttk.Entry(path_section, width=50)
download_view=ttk.Label(path_section, text="Waiting to download...", font="Verdana 10")
download_btn=ttk.Button(path_section, state='disabled', text="Download", command=lambda:DownloadVideo(download_view))
download_view.pack(side="bottom")
path_section.pack()
path_box.pack(side="left")
path_field.pack(side="left")
download_btn.pack(side="right")

body.mainloop()
