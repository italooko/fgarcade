import fgarcade as ge
import arcade
from arcade import SpriteList


class Player(ge.Player):
	def update_actions(self, commands, physics):
		super().update_actions(commands, physics)
		vx = self.change_x
		self.change_x = 3

		if self.change_x == 0 :
			pass

class Game(ge.Platformer):
	"""
	Gaguita's Game
	"""

	title = 'You Need To Calm Down'
	width = 1850
	height = 1000
	world_theme = 'brown'
	player_initial_tile = -2, 1.5
	jumping = False

	player_class = Player
	viewport_margin_horizontal = 1500
	viewport_margin_vertical = 0

	start_sound = arcade.load_sound('gaguita/src/sounds/MattOglseby-3.wav')
	coin_sound = arcade.load_sound('gaguita/src/sounds/UI1.wav')
	jump_sound = arcade.load_sound('gaguita/src/sounds/Sword-Swing.wav')
	die_sound = arcade.load_sound('gaguita/src/sounds/SFX5.ogg')

	def init_world(self, ):
	
		arcade.play_sound(self.start_sound)
		
		"""
		Gui's fase
		Part 1
		"""
		
		self.coin_list = SpriteList()
		self.spike_list = SpriteList()
	
		self.create_arrow('right', (1, 1))
		self.create_ground(6, coords=(-3, 0))
		
		self.create_ground(35, coords=(5, 2)) 
		"""
		self.create_ground(3, coords=(5, 2))            
		self.create_ground(1, coords=(7, 5))
		self.create_ground(1, coords=(16, 1))
		self.create_ground(3, coords=(3, -5))
		self.create_ground(1, coords=(11, 5))
		self.create_ground(1, coords=(15, 6))
		self.create_ground(4, coords=(17, 4))
		self.create_ground(5, coords=(18, 7))
		self.create_ground(3, coords=(20, 9))	
		self.create_ground(1, coords=(27, 6))
		self.create_ground(4, coords=(22, 2))
		self.create_ground(6, coords=(27, 0))
		self.create_ground(1, coords=(35, 3))
		self.create_ground(2, coords=(31, 6))
		self.create_ground(2, coords=(37, 5))
		#self.create_ground(8, coords=(40, 4))
		"""
		
		"""
		Italo's fase
		Part 2
		"""
		self.create_tower(3, 17, coords=(42, 0))
		self.create_foreground('other/plant/red-4', (43, 3))
		self.create_arrow('right', (45, 3))
		self.create_object('other/items/yellowCrystal', (46, 6)) #coin
		self.create_block('grey', (46, 5))
		self.create_foreground('other/plant/red-5', (49, 3))
		self.create_background('other/plant/top-read', (50, 6))
		self.create_background('other/plant/bottom-2', (50, 5))
		self.create_background('other/plant/stem-vertical', (50, 4))
		self.create_background('other/plant/leaf-1', (50, 3))
		self.create_background('other/plant/top-blue', (52, 7))
		self.create_background('other/plant/leaf-2', (52, 6))
		self.create_background('other/plant/leaf-1', (52, 5))
		self.create_background('other/plant/leaf-2', (52, 4))
		self.create_background('other/plant/stem-vertical', (52, 3))
		self.create_background('other/plant/top-yellow', (53, 7))
		self.create_background('other/plant/bottom-2', (53, 6))
		self.create_background('other/plant/leaf-1', (53, 5))
		self.create_background('other/plant/stem-vertical', (53, 4))
		self.create_background('other/plant/leaf-1', (53, 3))
		self.create_object('other/spikes/spikes-high', (54, 3), sprite_list=self.spike_list) #spike
		self.create_object('other/items/yellowCrystal', (57, 6)) #coin
		self.create_block('grey', (57, 5))
		self.create_foreground('other/plant/red-2', (57, 3))
		self.create_tower(4, 2, coords=(59, 0)) #smooth_ends=False
		self.create_tower(6, 3, coords=(61, 0))
		self.create_foreground('other/plant/red-6', (62, 6))

		self.create_ground(6, coords=(66, 2), end='sharp')
		self.create_foreground('other/plant/red-3', (67, 3))
		self.create_object('other/spikes/spikes-high', (68, 3)) #spike
		self.create_background('other/plant/top-read', (70, 6))
		self.create_background('other/plant/bottom-2', (70, 5))
		self.create_background('other/plant/leaf-1', (70, 4))
		self.create_background('other/plant/leaf-2', (70, 3))

		self.create_platform(5, coords=(74, 4))
		self.create_foreground('other/plant/red-2', (76, 5))
		self.create_arrow('right', (81, 7))
		self.create_platform(1, coords=(81, 6))
		
		self.create_ground(10, coords=(75, 1), end='sharp')
		self.create_foreground('other/plant/red-1', (77, 2))
		self.create_foreground('other/plant/red-1', (80, 2))
		self.create_background('other/plant/top-read', (81, 4))
		self.create_background('other/plant/leaf-1', (81, 3))
		self.create_background('other/plant/bottom-2', (81, 2))
		self.create_object('other/spikes/spikes-high', (82, 2)) #spike
		self.create_foreground('other/plant/red-6', (83, 2))

		self.create_foreground('other/plant/red-2', (87, 7))		
		self.create_platform(1, coords=(87, 6))
		self.create_arrow('top-right', (92, 4))
		self.create_platform(1, coords=(92, 3))
		self.create_object('other/items/discGreen', (95, 3)) #life
		self.create_platform(1, coords=(95, 2))
		self.create_object('other/items/yellowCrystal', (97, 6)) #coin
		self.create_platform(1, coords=(97, 5))

		self.create_arrow('right', (103, 9))
		self.create_tower(8, 16, coords=(102, 1))
		self.create_foreground('other/plant/red-6', (101, 8))
		self.create_ground(3, coords=(100, 7), end='round')
		self.create_block('grey', (100, 5))

		self.create_object('other/spikes/spikes-high', (99, 2), sprite_list=self.spike_list) #spike
		self.create_foreground('other/plant/red-6', (100, 2))
		self.create_ground(5, coords=(98, 1))

		"""
		self.create_object('other/plant/red-3', (5, 7))
		self.create_ground(2, coords=(42, 4))
		self.create_ground(2, coords=(46, 6)) #plant
		self.create_block('red', (50, 9)) #coin
		self.create_tower(5, 4, coords=(49, 0))
		self.create_ground(3, coords=(54, 2))

		self.create_block('brown', (58, 5))
		
		self.create_ground(5, coords=(59, 6)) #fence
		self.create_tower(8, 1, coords=(67, 0))
		self.create_tower(7, 4, coords=(68, 0))
		
		self.create_foreground('other/plant/red-3', (46, 7))
		self.create_foreground('other/plant/red-1', (55, 3))

		self.create_fence('left', (60, 7))
		self.create_fence('middle', (61, 7))
		self.create_fence('right', (62, 7))
		"""

	def init_enemies(self):
		pass

	def init_items(self):
		pass

	def init(self):
		self.init_world()
		self.init_items()
		self.init_enemies()
		
	def on_update(self, dt):
		super().on_update(dt)
		
		if self.player.center_y < 0:
			exit()
		
		if self.player.change_y > 0:
			if not self.jumping:
				arcade.play_sound(self.jump_sound)
			self.jumping = True
		else:
			self.jumping = False		
			
		cols = arcade.check_for_collision_with_list(self.player, self.spike_list)
		if cols:
			print(cols)
		

if __name__ == "__main__":
	Game().run()
