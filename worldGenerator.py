class World:
	def __init__(self, width, height):
		self.world = self.generate_world(width, height)
		
	def generate_world(self, width, height):
	    return [["*" for i in range(width)] for i in range(height)]
    
	def display(self):
		print("\n".join([" ".join(i) for i in self.world]))
		
	def place(self, x, y, symbol="@"):
	    self.world[len(self.world) - y - 1][x] = symbol
	
	def obtain(self, x, y):
	    return self.world[len(self.world) - y - 1][x]
		
if __name__ == "__main__":
	WIDTH, HEIGHT = 5, 5
	world = World(WIDTH, HEIGHT)
	world.place(1, 1, "&")
	world.place(2, 2, "@")
	world.display()
