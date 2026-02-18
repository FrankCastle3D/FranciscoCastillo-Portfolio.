
from noise import snoise2
from PIL import Image
import noise_data
from math import sin, cos


# height and width of the output
h, w = 512,512

# holds the RGB channels to dump as an image later
pixels = []


# use this to map different heights to different colors
def mapColor(noise):
	r = int(noise * 255)
	b = int(noise * 255)
	g = int(noise * 255)

	return (r, g, b)

#utils
#-------------------------
def mapRange(value, start1, stop1, start2, stop2):
	return (start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1)))

def turbulence(x, y, z, w):
	t = -.5
	f = 1
	while f <= w / 4:
		t += abs(snoise2(f * x, f * y) / f)
		f *= 2
	return t

#-------------------------

# fractional brownian motion -> fbm
def octavedNoise(x, y, octaves, gain, persistence, frequency, lacunarity, offset):
	
	signal = 0.0
	curFrequency = frequency

	val = 0.0
	amp = gain
	prev = 1.0

	for i in range(0, octaves):
# you can play with the math here.
		ax = x * curFrequency
		ay = y * curFrequency

		# play with different math functions to skew the noise, or not
		#ax = sin(ax) * .5 + .5
		#ay = cos(ay) * .5 + .5

		#n = snoise2(ax, ay)
		n = turbulence(ax, ay, 0.0, 512) 

		# ridged, sharper peaks
		signal = abs(n)
		signal = offset - signal
		signal *= signal

		# non-ridged noise
		# signal = n;

		val += signal * amp
		val += signal * amp * prev

		prev = n

		amp *= persistence
		curFrequency *= lacunarity

	return val



#parameters for fBm

octaves = noise_data.brownianClouds.octaves
gain = noise_data.brownianClouds.gain
persistence = noise_data.brownianClouds.persistence
frequency = noise_data.brownianClouds.frequency
lacunarity = noise_data.brownianClouds.lacunarity
offset = noise_data.brownianClouds.offset


# given a pixel buffer / list of RGB values, looop
min = 1000000
max = 0
v = []
for x in range(0, w):
	for y in range(0, h):
		noise = snoise2(float(x) / w, float(y) / h)
		noise = octavedNoise(float(x) / w, float(y) / h, octaves, gain, persistence, frequency, lacunarity, offset)
		if min > noise:
			min = noise
		if max < noise:
			max = noise
		
		v.append(noise)
		
# remap noise range to ensure it's between 0 to 1 after fBm so there's a clean linear mapping to RGB
for n in v:
	no = mapRange(n, min, max, 0., 1.)

	# change these to be weighted differently for wacky colors, same weight on each color --> greyscale...
	# 			   r 			  	  g              b
	pixels.append(mapColor(no)) # eventually becomes unsigned bytes 0 to 255

im = Image.new('RGB', (w, h)) # create a new image
im.putdata(pixels) # put the RGB data into the image
im.save("brownian.png") # save the file in the current working directory