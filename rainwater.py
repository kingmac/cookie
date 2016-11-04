class RainWater:
	def __init__(self):
		self.rainfall = float(input("How many inches of rain fall?\n")) or int(input("How many inches of rain fall?\n"))
		self.wide = int(input("How wide is your catchment area?\n"))
		self.length = int(input("How long is your catchment area?\n"))
		print(self.calc())

	# rainfall/12 * width * length * 7.48
	def calc(self):
		cacl1 = self.rainfall / 12
		cacl2 = cacl1 * self.wide * self.length
		return cacl2 * 7.48



def main():
	rain_water = RainWater()


if __name__ == "__main__":
	main()