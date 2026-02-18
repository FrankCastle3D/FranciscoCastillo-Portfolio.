

class fbmParameters(object):
    def __init__(self, name, octaves, gain, persistence, frequency, lacunarity, offset):
        self.name = name
        self.octaves = octaves
        self.gain = gain
        self.persistence = persistence
        self.frequency = frequency
        self.lacunarity = lacunarity
        self.offset = offset

# cells from hell - use turbulence instead of snoise in octavedNoise
# octaves = 3
# gain = 2.0
# persistence = 1.0
# frequency = 4
# lacunarity = 1.0
# offset = 1.0

# bizzare funkadelic terrain - use turbulence, swap blue and green channels
# octaves = 1
# gain = 1.0
# persistence = 1.25
# # stick with powers of 2 for best results
# frequency = 8
# lacunarity = .75
# offset = 1.0

# fractal capsules, use the sin(x), cos(y) code to warp
# octaves = 1
# gain = 1.0
# persistence = 1.25
# # stick with powers of 2 for best results
# frequency = 32
# lacunarity = .75
# offset = 1.0

# rough brushstroke fractal capsules, just different octave value and turbulent noise vs snoise
# octaves = 3
# gain = 1.0
# persistence = 1.25
# # stick with powers of 2 for best results
# frequency = 32
# lacunarity = .75
# offset = 1.0

             # name, octaves, gain, persistence, frequency, lacunarity, offset    
brownianClouds = fbmParameters("Brownian Clouds", 1, 1.25, 1.1, 5, 0.1, 1.0)
plasmaLineblobs = fbmParameters("Plasma Lineblobs", 3, 2.0, 1.0, 4, 1.0, 1.0)
