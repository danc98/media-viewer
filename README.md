## DESCRIPTION
A simple media library GUI made with Tkinter in Python.
Originally designed some years ago for use with my personal movie/TV show library.

## SETUP
1. Written in Python 3.10.6, although basic enough that early versions may work fine.
2. Run pip install -r requirements.txt to install all modules.
3. This program requires two folders, one with your media (movies, TV shows, etc.) and one with cover images.
4. Make sure the filename of each cover reflects the name of the associated media, or else the play button may not work.

## USING THE APP
1. Configure the .env file to point to your media folder and your cover image folder.
2. Run mediaViewer.pyw.

## FEATURES
1. Play button to automatically play your media files from the app.
2. Random button for when you can't decide what to watch.

## TO-DO
Currently cover image sizes are hard-coded around average movie poster dimensions,
but it would be much better to have dynamic image sizing that properly resized cover images based on aspect ratio.