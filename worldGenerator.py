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
	
	PLAYER_X = 1
	PLAYER_Y = 1
	
	world.place(PLAYER_X, PLAYER_Y, "P")
	
	while True:
	    world.display()
	    user_input = input("Command >> ")
	    
	    if user_input.lower() == "up":
	        world.place(PLAYER_X, PLAYER_Y, "*")
	        PLAYER_Y += 1
	        world.place(PLAYER_X, PLAYER_Y, "P")
