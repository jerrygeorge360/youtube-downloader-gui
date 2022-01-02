from tkinter import *
from tkinter import filedialog
from tkinter import ttk

from pytube import *

window = Tk()
window.title('YouTube downloader')
window.iconphoto(False, PhotoImage(file='youtubesmall.png'))
window.geometry('900x600')
window.resizable(width=0, height=0)
download = PhotoImage(file='download.png')
containerFrame = Frame(window, width=500, height=500, padx=3, pady=3, bg='black')
containerFrame.grid(row=0, column=0, sticky='nwse')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
containerFrame.grid_rowconfigure(0, weight=1)
containerFrame.grid_columnconfigure(0, weight=1)

headerFrame = Frame(containerFrame, width=500, height=150, bg='red')
headerFrame.grid(row=0, column=0, sticky='nwse')
headerLabel = Label(headerFrame, text='YouTube downloader', bg='red')
headerLabel.grid(row=0, column=0, sticky='nwse')
headerFrame.grid_columnconfigure(0, weight=1)
headerFrame.grid_columnconfigure(1, weight=1)
headerFrame.grid_columnconfigure(2, weight=1)
headerFrame.grid_rowconfigure(1, weight=1)
innerholder = Frame(headerFrame, width=100, height=100, bg='black')
innerholder.grid(row=1, column=0, sticky='nwse')

innerholder1 = Frame(headerFrame, width=100, bg='black', height=100)
innerholder1.grid(row=1, column=2, sticky='nswe')
innerholder2 = Frame(headerFrame, width=100, bg='grey', height=100)
innerholder2.grid(row=1, column=1, sticky='nswe')

headerEntry = Text(innerholder2, font=('Arial', 10))

headerEntry.grid(row=0, column=0)
innerholder2.grid_columnconfigure(0, weight=1)
innerholder2.grid_rowconfigure(0, weight=1)

middleFrame = Frame(containerFrame, width=500, height=250, bg='blue')
middleFrame.grid(row=1, column=0, sticky='nwse')

middleFrame.grid_rowconfigure(0, weight=1)
middleFrame.grid_columnconfigure(0, weight=1)
middleFrame.grid_columnconfigure(1, weight=1)
middleFrame.grid_columnconfigure(2, weight=1)
middleInnerLeft = Frame(middleFrame, width=16, height=250, padx=9, pady=9, bg='grey')
middleInnerLeft.grid(row=0, column=0, sticky='nwse')
middleInnerRight = Frame(middleFrame, width=16, height=250, padx=9, pady=9, bg='grey')
middleInnerRight.grid(row=0, column=1, sticky='nwse')
middleInnerCenter = Frame(middleFrame, width=16, height=250, padx=9, pady=9, bg='grey')
middleInnerCenter.grid(row=0, column=2, sticky='nwse')
progress = ttk.Progressbar(innerholder2, length=300, orient=HORIZONTAL, mode='determinate')


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress.grid(row=1, column=0, pady=3)

    print(bytes_downloaded)
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress['value'] = percentage_of_completion
    print(percentage_of_completion)


def audioonly():
    path = filedialog.askdirectory(title='select path')
    url = f"'{headerEntry.get(1.0, 'end-1c')}'"
    yt_obj = YouTube(url)
    yt_obj.register_on_progress_callback(on_progress)
    file_path = yt_obj.streams.get_audio_only().download(output_path=path)
    print(f'file_path is {file_path}')


middleButton = Button(middleFrame, activebackground='white', text='Only Audio', padx=40, background='red', fg='white',
                      borderwidth=4, font=('Arial', 20, 'bold'), command=audioonly, height=150, image=download,
                      compound=BOTTOM)
middleButton.grid(row=0, column=0, sticky='we')


def lowestrez():
    url = f"'{headerEntry.get(1.0, 'end-1c')}'"
    yt_obj = YouTube(url)
    yt_obj.register_on_progress_callback(on_progress)
    file_path = yt_obj.streams.filter(progressive=True).get_lowest_resolution().download()
    print(f'file_path is {file_path}')


middleButton1 = Button(middleFrame, text='Lowest resolution', activebackground='white', fg='grey', background='white',
                       borderwidth=4, font=('Arial', 20, 'bold'), command=lowestrez, height=150, image=download,
                       compound=BOTTOM)
middleButton1.grid(row=0, column=1, sticky='we')


def highestrez():
    url = f"'{headerEntry.get(1.0, 'end-1c')}'"
    yt_obj = YouTube(url)
    yt_obj.register_on_progress_callback(on_progress)
    file_path = yt_obj.streams.filter(progressive=True).get_highest_resolution().download()
    print(f'file_path is {file_path}')


middleButton2 = Button(middleFrame, text='Highest resolution', activebackground='white', fg='black', background='grey',
                       borderwidth=4, font=('Helvetica', 20, 'bold'), command=highestrez, height=150, image=download,
                       compound=BOTTOM)
middleButton2.grid(row=0, column=2, sticky='we')

bottomFrame = Frame(containerFrame, width=500, height=100, bg='red')
bottomFrame.grid(row=3, column=0, sticky='nwse')
bottomFrame.grid_columnconfigure(0, weight=1)
bottomFrame.grid_columnconfigure(1, weight=1)
bottomFrame.grid_columnconfigure(2, weight=1)
bottomFrame.grid_rowconfigure(0, weight=1)
bottominner1 = Frame(bottomFrame, width=230, bg='black')
bottominner = Frame(bottomFrame, width=40)
bottominner2 = Frame(bottomFrame, width=230, bg='black')
bottominner1.grid(row=0, column=0)
bottominner.grid(row=0, column=1)
bottominner2.grid(row=0, column=2)
img = PhotoImage(file='youtubesmall.png')
label = Label(bottominner, image=img)
label.grid(row=0, column=0, sticky='ew')

window.mainloop()
