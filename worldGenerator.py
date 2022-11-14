class World:
	def __init__(self, width, height):
		self.world = self.generate_world(width, height)
		
	def generate_world(self, width, height):
	    return [["*" for i in range(width)] for i in range(height)]
    
	def display(self):
		print("\n".join([" ".join(i) for i in self.world]))
		
if __name__ == "__main__":
	WIDTH, HEIGHT = 5, 5
	world = World(WIDTH, HEIGHT)
	world.display()
