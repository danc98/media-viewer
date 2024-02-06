from random import randint
from PIL import ImageTk, Image
from dotenv import load_dotenv
from pathlib import Path
import os
import subprocess
import tkinter.font as font
import tkinter as tk

# Load .env file.
load_dotenv()

# Target directories for media.
cover_dir = os.getenv('COVER_DIR')
media_dir = os.getenv('MEDIA_DIR')

# Finds associated media file with cover and opens it.
def playFile():
    # Select the media file selected to open, if nothing selected, default to first item.
    selected_media = listbox.curselection()
    if not selected_media:
        selected_media = os.listdir(media_dir)[0]

    # Search media directory for file that matches selected cover and open it.
    for filename in os.listdir(media_dir):
        if listbox.get(selected_media) in filename:
            media = media_dir + '\\' + filename
            subprocess.Popen('explorer ' + media)
            break

# Function that updates cover image when list item is double clicked.
def updateCover(event=None):
    os.chdir(cover_dir)
    update_cover = ImageTk.PhotoImage(Image.open(
                   listbox.get(listbox.curselection()) + '.jpg')
                   .resize((350, 550)))
    display_cover.configure(image=update_cover)
    display_cover.image = update_cover

# Selects a random item and displays image.
def randFile():
    listbox.selection_clear(0, listbox.size())
    random_index = randint(0, listbox.size())
    listbox.selection_set(random_index)
    listbox.see(random_index)
    updateCover()

## Building tkinter GUI ##
# Create tkinter window.
window = tk.Tk()
window.title(os.getenv('APP_TILE'))
window.geometry('970x720')
window.resizable(0, 0)
myFont = font.Font(family='Helvetica', size=12)

# Left Frame
left_frame = tk.Frame(window)
left_frame.pack(side='left')

# Dimensions for listbox.
listbox = tk.Listbox(left_frame, height=44, width=30, activestyle='none')
listbox.pack(side='left')

# Populates list with items in current directory.
for filename in os.listdir(cover_dir):
    new_filename=Path(filename).stem
    listbox.insert(tk.END, new_filename)

# Sets font for text in listbox.
listbox.config(font=myFont)

# Binds scroll bar to list.
scrollbar = tk.Scrollbar(left_frame)
scrollbar.pack(side='right', fill='y')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Sets initial media display to first item in cover directory.
file_list = os.listdir(cover_dir)
first_file = cover_dir + '\\' + file_list[0]
cover = ImageTk.PhotoImage(Image.open(first_file).resize((350, 550)))
listbox.bind("<Double-Button-1>", updateCover)

# Dimensions for cover image.
display_cover = tk.Label(window, image=cover)
display_cover.pack()
display_cover.place(bordermode=tk.OUTSIDE, x=440, y=30)

# Dimensions for start button.
start_button = tk.Button(window, width=32, height=3,
                         text="Play", font=myFont, command=playFile)
start_button.pack()
start_button.place(bordermode=tk.OUTSIDE, x=560, y=620)

# Dimensions for random button.
rando_button = tk.Button(window, width=16, height=3,
                         text="Random", font=myFont, command=randFile)
rando_button.pack()
rando_button.place(bordermode=tk.OUTSIDE, x=360, y=620)

# Only open mediaViewer if called directly.
if __name__ == '__main__':
    window.mainloop()
