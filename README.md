# NFTGenerator
Hey, welcome to my <b>NFT Generator project</b>, this was aimed to be
a hackable library to generate a large batch of nft's while using
your own images! It was originally intended as just a fun little
project to test myself, but I might eventually maintain it and
work on suggestions, thanks :)

# Now for the setup...
To run it is easy, just make sure you have python3.8.x+ installed
before carrying onto the next steps. now read through the config
setup (based at the bottom of the README.md), now you can finally
run <code>python nft.py</code>, this will run for a few seconds
untill it has successfully saved the newly generated nft's to
<b>assets/output/\*.png</b>, and you are done! enjoy :)

# Project config?
The config for the project is stored in <b>config.json</b>, the "folders"
list represents all of the folders that contain your images, keep
in mind you will have to seperate different types of images, lets
say you have a hat and shoes in the same folder, and you want
them both to have a chance to be present on the image at the same
time, that won't happen, since my code is aimed at choosing random
'accessories' from various input folders, lets say <b>/glasses/</b>,
<b>/characters/</b>, <b>/hats/</b>, <b>/bowties/</b>, and <b>etc</b>, you can either enter the
path to these folders relative to the folder which houses <b>nft.py</b>,
or you can enter an absolute path to somewhere else in your drive!
now for "image_size", this represents the dimensions of your files,
(keep in mind all of your files need to have the exact same size),
entering 512 as the size will mean that your images are 512x512,
i might implement auto resizing in the future just incase, but keep
this in mind :)