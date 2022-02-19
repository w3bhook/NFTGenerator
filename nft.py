from random import randint, choice
from os import system, listdir, mkdir
from json import load
from time import sleep, perf_counter
from PIL import Image
import matplotlib.pyplot as plt

class NFT:
	def __init__(self):
		self.files = {}
		self.cache = []
		self.tint = []
		self.outputdir = "assets/output/"
		self.ph = []		
	
	def generate(self, folders, iterations):

		self._n = iterations

		for i in folders:
			try:
				self.files[i] = listdir(i)
			except IndexError:
				pass

		self.rgb()
		self.apply()
		
	def rgb(self):
		for i in range(self._n):
			bg = Image.new(mode="RGB", size=(image_size, image_size), color=(0, 0, 0))

			_ph1 = Image.new(mode="RGB", size=(int(image_size/2), int(image_size/2)), color=(randint(50,255), randint(50,255), randint(50,255)))
			_ph2 = Image.new(mode="RGB", size=(int(image_size/2), int(image_size/2)), color=(randint(50,255), randint(50,255), randint(50,255)))
			_ph3 = Image.new(mode="RGB", size=(int(image_size/2), int(image_size/2)), color=(randint(50,255), randint(50,255), randint(50,255)))
			_ph4 = Image.new(mode="RGB", size=(int(image_size/2), int(image_size/2)), color=(randint(50,255), randint(50,255), randint(50,255)))

			bg.paste(_ph1, (0, int(image_size/2)))
			bg.paste(_ph2, (int(image_size/2), 0))
			bg.paste(_ph3, (0, 0))
			bg.paste(_ph4, (int(image_size/2), int(image_size/2)))

			self.ph.append(bg)

		for i in self.files:
			self.tint.append((randint(50,255), randint(50,255), randint(50,255)))
		
	def apply(self):
		for self.bg_img in self.ph:
			self.addons = []
			for i in self.files:
				if len(self.files[i]) != 0:
					chf = choice(self.files[i])
				else:
					pass

				self.addons.append(Image.open(f"{i}{chf}"))
			 
			for i in self.addons:
				i.resize((256, 256))
				self.tm = i.convert("RGBA")
				self.bg_img.paste(i, (0, 0), self.tm)

			for x in self.files:
				for i in self.files[x]:
					try:
						self.bg_img.save(str(self.outputdir + 
											 "__final__" + 
											 i.split(".")[0][0] +
											 i.split(".")[0][-1] +
											 str(randint(1111, 9999)) +
											 str(sum([int(str(perf_counter())[-1]), int(str(perf_counter())[-2])])) + 
											 "." +
											 i.split(".")[1])
						)
					except FileNotFoundError:
						mkdir("assets")
						mkdir(self.outputdir)
						self.bg_img.save(str(self.outputdir + 
											 "__final__" + 
											 i.split(".")[0][0] +
											 i.split(".")[0][-1] +
											 str(randint(1111, 9999)) +
											 str(sum([int(str(perf_counter())[-1]), int(str(perf_counter())[-2])])) + 
											 "." +
											 i.split(".")[1])
						)


if __name__ == '__main__':
	# tests
	nft = NFT()

	with open("config.json") as cfg:
		cfg = load(cfg)
		image_size = cfg["image_size"]

	nft.generate(cfg["folders"], cfg["amount_of_iterations"])
	print(f"succesfully generated {cfg['amount_of_iterations']} nft images!")