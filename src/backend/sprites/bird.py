from random import uniform
from backend.sprites.bullet import Bullet


class Bird:
	def __init__(self, position, move_strategy, board):
		self.position = position # x and y ints
		self.health = 2 # max = 10, min = 0
		self.strength = 1 # min = 1, max = 5
		self.move_strategy = move_strategy
		self.board = board
		self.is_dead = False

	def move(self):
		self.position.x += self.move_strategy.get_delta_x()
		self.position.y += self.move_strategy.get_delta_y()
		print("Moved according to the strategy")

		if self.board.matrix[self.position.x][self.position.y] == "^":
			kat = board.get_kat_on_pos(self.position.x, self.position.y)
			kat.get_shot()

	def shoot(self):
		if uniform(0, 10) > 8:
			bullet = Bullet(self.position, self.strength, self.board, False)
			# bullet.move()

	def get_shot(self, strength):
		print("Bird got shot")
		self.health -= strength
		if self.health <= 0:
			self.is_dead = True