import fgarcade as ge
import arcade

class Player(ge.Player):
	def update_actions(self, commands, physics):
		super().update_actions(commands, physics)
		vx = self.change_x
		self.change_x = 3

		if self.change_x == 0 :
			pass

	""" def update(self, dt):
		super().update(dt)

		if self.player.center_y < -500:
			arcade.draw_text('MORREU', 10 + self.viewport_horizontal_start, 10 + self.viewport_vertical_start, arcade.csscolor.BLACK, 18) */ 
	"""

class Game(ge.Platformer):
	"""
	Gaguita's Game
	"""

	title = 'You Need To Calm Down'
	player_initial_tile = -2, 1.5
	player_class = Player
	viewport_margin_horizontal = 600
	viewport_margin_vertical = 0

	start_sound = arcade.load_sound('gaguita/src/sounds/MattOglseby-3.wav')
	coin_sound = arcade.load_sound('gaguita/src/sounds/UI1.wav')

	def init_world(self):
		arcade.play_sound(self.start_sound)

		self.create_ground(1, coords=(1, 8.5))
		self.create_ground(6, coords=(-3, 0))
		self.create_ground(3, coords=(5, 3))
		self.create_ground(1, coords=(9, 2))
		self.create_ground(1, coords=(9, 3))
		self.create_ground(1, coords=(9, 4))
		self.create_ground(100, coords=(11, 0))
		self.create_ground(1, coords=(16, 1))

	def init_enemies(self):
		pass

	def init_items(self):
		pass


	def init(self):
		self.init_world()
		self.init_items()
		self.init_enemies()


if __name__ == "__main__":
	Game().run()
