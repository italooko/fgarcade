import fgarcade as ge
import arcade
from arcade import SpriteList
from fgarcade.enums import Role
import pyglet


class Player(ge.Player):
	def update_actions(self, commands, physics):
		super().update_actions(commands, physics)
		vx = self.change_x
		self.change_x = 3

class Game(ge.Platformer):
	"""
	Gaguita's Game
	"""

	title = 'Gaguita: Platformer Game'
	width = 1850
	height = 1000
	world_theme = 'brown'
	#background_color = (120, 213, 219)
	#background_near = SpriteList(use_spatial_hash=False)
	#background_fixed = SpriteList(use_spatial_hash=False)
	
	player_color = 'red'
	player_initial_tile = -2, 3
	player_class = Player
	viewport_margin_horizontal = 900
	viewport_margin_vertical = 0

	player_score = 0
	player_life = 3
	count_frames = 0
	jumping = False
	spike_collision = False
	enemy_collision = False

	start_sound = pyglet.media.load('gaguita/src/sounds/MattOglseby-3.wav')
	coin_sound = arcade.load_sound('gaguita/src/sounds/SFX1.wav')
	jump_sound = arcade.load_sound('gaguita/src/sounds/Sword-Swing.wav')
	life_sound = arcade.load_sound('gaguita/src/sounds/UI1.wav')
	life_lost_sound = arcade.load_sound('gaguita/src/sounds/SFX5.wav')
	enemy_killed_sound = arcade.load_sound('gaguita/src/sounds/Lazer-Ricochet.wav')

	level_sound = pyglet.media.Player()
	level_sound.loop = True
	level_sound.queue(start_sound)

	def init_world(self):
		self.level_sound.play()

		"""
		Gui's fase
		Part 1
		"""
		self.world_theme = 'green'

		# primeiro bloco
		self.create_arrow('right', (1, 2))
		self.create_foreground('other/plant/green-6', (3, 2))
		self.create_tower(2, 8, coords=(-3, 0))

		# torre / segundo bloco
		self.create_tower(4, 3, coords=(5, 0))   
		self.create_foreground('other/plant/green-4', (6, 4))         
		self.create_platform(1, coords=(7, 5))
		self.create_enemy(2, direction='y', coords=(9, 6), walk_size=4) #enemy
		
		self.create_object('other/spikes/spikes-high', (8, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (9, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (10, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (11, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (12, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (13, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (14, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (15, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (16, 0), sprite_list=self.spikes) #spike

		# bloco cinzento / terceiro bloco
		self.create_block('grey', (11.5, 5.5)) #block #coin
		
		# bloco cinzento / quarto bloco
		self.create_block('grey', (15.5, 6.5))

# CAMINHO DE CIMA
		# ground / quinto bloco
		self.create_ground(5, coords=(18, 7), end='round')
		self.create_platform(3, coords=(20, 9))
		self.create_foreground('other/plant/dark-4', (21, 9.89)) #plant
		
		# ground / sexto bloco
		self.create_foreground('other/plant/dark-6', (27, 7)) #plant
		self.create_ground(1, coords=(27, 6))
		
		# ground / setimo bloco
		self.create_ground(2, coords=(31, 6), end='sharp')

		self.create_object('other/items/yellowCrystal', (34, 10), sprite_list=self.coins) #coin

# CAMINHO DE BAIXO
		# torre / quinto bloco 
		self.create_tower(5, 4, coords=(17, 0))
		
		# ground / sexto bloco
		self.create_enemy(coords=(22, 3), walk_size=4) #enemy
		self.create_ground(4, coords=(22, 2), end='round')

		# groun / setimo bloco
		self.create_ground(6, coords=(27, 0))
		self.create_object('other/spikes/spikes-high', (28, 1), sprite_list=self.spikes) #spike
		self.create_background('other/plant/top-read', (30, 4))
		self.create_background('other/plant/bottom-2', (30, 3))
		self.create_background('other/plant/stem-vertical', (30, 2))
		self.create_background('other/plant/leaf-1', (30, 1))
		
		# ground / oitavo bloco
		self.create_foreground('other/plant/dark-2', (35, 3)) #plant
		self.create_ground(1, coords=(35, 2))	

# CAMINHO COMUM 
		# tower / ultimo bloco
		self.create_object('other/items/discGreen', (38, 6), sprite_list=self.lifes) #life
		self.create_tower(5, 3, coords=(37, 0))	

		# Tiles
		self.create_foreground('tile/green/e2', (2, 0))
		self.create_foreground('tile/green/e3', (6, 1))
		self.create_foreground('tile/green/e3', (6, 2))

		self.create_foreground('tile/green/e2', (18, 1))
		self.create_foreground('tile/green/e2', (18, 2))
		self.create_foreground('tile/green/e3', (19, 2))
		self.create_foreground('tile/green/e2', (18, 3))

		self.create_foreground('tile/green/e2', (38, 1))
		self.create_foreground('tile/green/e2', (38, 2))
		self.create_foreground('tile/green/e2', (39, 0))
		self.create_foreground('tile/green/e2', (39, 3))

# Fim da parte super legal, agora comeca a super chata
		"""
		Italo's fase
		Part 2
		"""
		self.world_theme = 'brown'

		self.create_tower(3, 17, coords=(42, 0))
		self.create_foreground('other/plant/red-4', (43, 3))
		self.create_arrow('right', (45, 3))
		self.create_object('other/items/yellowCrystal', (45.5, 6), sprite_list=self.coins) #coin
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
		self.create_enemy(coords=(52, 3), walk_size=4) #enemy
		self.create_object('other/spikes/spikes-high', (54, 3), sprite_list=self.spikes) #spike
		self.create_object('other/items/yellowCrystal', (56.5, 6), sprite_list=self.coins) #coin
		self.create_block('grey', (57, 5))
		self.create_foreground('other/plant/red-2', (57, 3))
		self.create_tower(4, 2, coords=(59, 0))
		self.create_tower(5, 3, coords=(61, 0))
		self.create_foreground('other/plant/red-6', (62, 5))

		self.create_ground(6, coords=(66, 2), end='sharp')
		self.create_enemy(coords=(66, 3), walk_size=6) #enemy
		self.create_foreground('other/plant/red-3', (67, 3))
		self.create_object('other/spikes/spikes-high', (68, 3), sprite_list=self.spikes) #spike
		self.create_background('other/plant/top-read', (70, 6))
		self.create_background('other/plant/bottom-2', (70, 5))
		self.create_background('other/plant/leaf-1', (70, 4))
		self.create_background('other/plant/leaf-2', (70, 3))

		self.create_platform(5, coords=(74, 4))
		self.create_enemy(coords=(74, 5), walk_size=4) #enemy
		self.create_foreground('other/plant/red-2', (76, 5))
		self.create_arrow('right', (81, 7))
		self.create_platform(1, coords=(81, 6))		
		self.create_ground(10, coords=(75, 1), end='sharp')
		self.create_enemy(coords=(76, 2), walk_size=7) #enemy
		self.create_foreground('other/plant/red-1', (77, 2))
		self.create_foreground('other/plant/red-1', (80, 2))
		self.create_background('other/plant/top-read', (81, 4))
		self.create_background('other/plant/leaf-1', (81, 3))
		self.create_background('other/plant/bottom-2', (81, 2))
		self.create_object('other/spikes/spikes-high', (82, 2), sprite_list=self.spikes) #spike
		self.create_foreground('other/plant/red-6', (83, 2))

		self.create_foreground('other/plant/red-2', (86, 7))		
		self.create_platform(1, coords=(86, 6))
		self.create_enemy(2, direction='y', coords=(89, 3), walk_size=6) #enemy
		self.create_arrow('top-right', (91, 4))
		self.create_platform(1, coords=(91, 3))
		self.create_object('other/items/yellowCrystal', (96, 6), sprite_list=self.coins) #coin
		self.create_platform(3, coords=(95, 5))

		#self.create_arrow('right', (103, 9))
		#self.create_tower(9, 4, coords=(102, 0))
		self.create_foreground('other/plant/red-6', (101, 8))
		self.create_object('other/items/discGreen', (102, 8), sprite_list=self.lifes) #life
		self.create_ground(3, coords=(100, 7), end='round')
		self.create_block('grey', (100, 5))

		self.create_object('other/spikes/spikes-high', (99, 2), sprite_list=self.spikes) #spike
		self.create_foreground('other/plant/red-6', (100, 2))
		self.create_ground(5, coords=(98, 1))

		# Tiles
		self.create_foreground('tile/brown/e2', (42, 1))
		self.create_foreground('tile/brown/e2', (44, 1))
		self.create_foreground('tile/brown/e2', (46, 0))
		self.create_foreground('tile/brown/e3', (49, 1))
		self.create_foreground('tile/brown/e3', (51, 1))
		self.create_foreground('tile/brown/e3', (54, 0))
		self.create_foreground('tile/brown/e2', (58, 1))
		self.create_foreground('tile/brown/e2', (60, 1))
		self.create_foreground('tile/brown/e3', (61, 2))
		self.create_foreground('tile/brown/e2', (62, 3))
		self.create_foreground('tile/brown/e3', (63, 2))
		self.create_foreground('tile/brown/e3', (63, 1))

		"""
		Gabrie's fase
		Part 3
		"""
		self.world_theme = 'blue'
		
		self.create_arrow('sign', (105, 7))
		self.create_foreground('other/plant/dark-2', (107, 7))
		self.create_tower(7, 4, coords=(105, 0))

		self.create_fence('middle', (109, 5))
		self.create_fence('right', (110, 5))
		self.create_foreground('other/plant/dark-6', (111, 5))
		self.create_foreground('other/plant/top-yellow', (112, 6))
		self.create_foreground('other/plant/bottom-2', (112, 5))
		self.create_tower(5, 5, coords=(108, 0))

		self.create_object('other/spikes/spikes-high', (113, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (114, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (115, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (116, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (117, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (118, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (119, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (120, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (121, 0), sprite_list=self.spikes) #spike
		self.create_object('other/spikes/spikes-high', (122, 0), sprite_list=self.spikes) #spike

		self.create_enemy(coords=(114, 4), walk_size=4) #enemy
		self.create_foreground('other/plant/blue-6', (115, 4))
		self.create_ground(4, coords=(114, 3), end='round')

		self.create_block('grey', (116, 9))
		self.create_enemy(2, direction='y', coords=(118, 8), walk_size=4) #enemy
		self.create_block('grey', (120, 11))

		self.create_foreground('other/plant/blue-1', (120, 4))
		self.create_ground(2, coords=(120, 3), end='sharp')
		self.create_foreground('other/plant/blue-4', (124, 6))
		self.create_tower(6, 3, coords=(123, 0))
		
		self.create_foreground('other/plant/blue-5', (128, 7))
		self.create_tower(7, 3, coords=(127, 0))

		self.create_foreground('other/plant/blue-2', (132, 8))
		self.create_tower(8, 3, coords=(131, 0))

		self.create_arrow('top-right', (136, 10))
		self.create_object('other/items/yellowCrystal', (137, 10), sprite_list=self.coins) #coin
		self.create_platform(2, coords=(136, 9))
		
		self.create_enemy(coords=(140, 11), walk_size=2) #enemy
		self.create_platform(2, coords=(140, 10))
		self.create_object('other/items/yellowCrystal', (145, 11), sprite_list=self.coins) #coin
		self.create_platform(2, coords=(144, 10))
		self.create_enemy(2, direction='y', coords=(147, 8), walk_size=5) #enemy

		self.create_ground(2, coords=(137, 6), end='sharp')
		self.create_foreground('other/plant/blue-6', (141, 5))
		self.create_ground(3, coords=(140, 4), end='round')
		self.create_ground(2, coords=(144, 2), end='sharp')

		self.create_block('grey', (150, 8))
		self.create_block('grey', (154, 6))
		self.create_background('other/plant/top-read', (150, 4))
		self.create_background('other/plant/bottom-2', (150, 3))
		self.create_background('other/plant/stem-vertical', (150, 2))
		self.create_background('other/plant/leaf-1', (150, 1))
		self.create_foreground('other/plant/blue-5', (151, 1))
		self.create_object('other/spikes/spikes-low', (153, 1), sprite_list=self.spikes) #spike
		self.create_ground(7, coords=(149, 0))

		# Tiles
		self.create_foreground('tile/blue/e2', (106, 5))
		self.create_foreground('tile/blue/e2', (106, 1))
		self.create_foreground('tile/blue/e2', (106, 2))
		self.create_foreground('tile/blue/e2', (107, 1))
		self.create_foreground('tile/blue/e3', (110, 3))
		self.create_foreground('tile/blue/e3', (111, 3))
		self.create_foreground('tile/blue/e3', (111, 2))
		
		self.create_foreground('tile/blue/e2', (124, 4))
		self.create_foreground('tile/blue/e2', (124, 2))
		self.create_foreground('tile/blue/e2', (128, 5))
		self.create_foreground('tile/blue/e2', (128, 2))
		self.create_foreground('tile/blue/e2', (128, 3))
		self.create_foreground('tile/blue/e2', (132, 6))
		self.create_foreground('tile/blue/e2', (132, 2))
		self.create_foreground('tile/blue/e2', (132, 3))
		self.create_foreground('tile/blue/e2', (132, 4))

	def create_enemy(self, enemy_type=1, direction='x', coords=(0, 0), walk_size=4):
		"""
		Creates enemies in the world.

		Enemy type 1: Walking.
		Enemy type 2: Flying.
		"""
		enemy = arcade.AnimatedWalkingSprite()
		enemy_name = 'enemyFlying_' if enemy_type == 2 else 'enemyWalking_'
		enemy_path = 'fgarcade/data/themes/abstract/enemy/'

		x, y = coords
		bound1_x, bound1_y = x - 1, y
		bound2_x, bound2_y = x + walk_size, y

		border_path = '../../../../../fgarcade/gaguita/src/img/'
		texture_range = (2, 3, 2, 1) if enemy_type == 2 else (2, 1, 2, 1)
		speed_x = 1.3
		speed_y = 0

		if direction == 'y':
			bound1_x, bound1_y = x, y - 1
			bound2_x, bound2_y = x, y + walk_size
			speed_x = 0
			speed_y = 1.0
		
		# First enemy boundary
		self.create_object(
            border_path + 'transparent',
            coords = (bound1_x, bound1_y),
            role = Role.BACKGROUND,
            sprite_list = self.enemy_limits
        )

		# Second enemy boundary
		self.create_object(
            border_path + 'transparent',
            coords = (bound2_x, bound2_y),
            role = Role.BACKGROUND,
            sprite_list = self.enemy_limits
        )
		
		enemy.stand_left_textures = []
		enemy.stand_right_textures = []
		enemy.walk_left_textures = []
		enemy.walk_right_textures = []
		
		enemy.stand_left_textures.append(
            arcade.load_texture(enemy_path + enemy_name + "1.png", scale=self.scaling, mirrored=True)
        )
		enemy.stand_right_textures.append(
            arcade.load_texture(enemy_path + enemy_name + "1.png", scale=self.scaling)
        )
		
		for i in texture_range:
			enemy.walk_left_textures.append(
				arcade.load_texture(enemy_path + enemy_name + str(i) + ".png", scale=self.scaling, mirrored=True)
			)
		
		for i in texture_range:
			enemy.walk_right_textures.append(
				arcade.load_texture(enemy_path + enemy_name + str(i) + ".png", scale=self.scaling)
			)

		x = int(64 * x + 32)
		y = int((64 * y) + (44 / 2))

		enemy.change_x = speed_x
		enemy.change_y = speed_y
		enemy.texture_change_distance = 20
		enemy.left = x
		enemy.bottom = y

		self.enemies.append(enemy)
		return enemy
	
	def init_enemies(self):
		self.enemies = SpriteList()
		self.enemy_limits = SpriteList()

	def init_items(self):
		self.coins = SpriteList()
		self.lifes = SpriteList()
		self.spikes = SpriteList()

	def init(self):
		self.init_items()
		self.init_enemies()
		self.init_world()
		
	def collision_with_coins(self):
		self.coins.update()
		coins_hit_list = arcade.check_for_collision_with_list(self.player, self.coins)

		for coin in coins_hit_list:
			coin.remove_from_sprite_lists()
			self.player_score += 1
			arcade.play_sound(self.coin_sound)

	def collision_with_lifes(self):
		self.lifes.update()
		lifes_hit_list = arcade.check_for_collision_with_list(self.player, self.lifes)

		for life in lifes_hit_list:
			life.remove_from_sprite_lists()
			self.player_life += 1
			arcade.play_sound(self.life_sound)
	
	def collision_with_spikes(self):
		self.spikes.update()
		spikes_hit_list = arcade.check_for_collision_with_list(self.player, self.spikes)

		if len(spikes_hit_list) > 0:
			if not self.spike_collision:
				self.player_life -= 1
				arcade.play_sound(self.life_lost_sound)
			self.spike_collision = True
		else:
			self.spike_collision = False
	
	def collision_with_enemies(self):
		self.enemies.update()
		enemies_hit_list = arcade.check_for_collision_with_list(self.player, self.enemies)

		for enemy in self.enemies:
			for border in self.enemy_limits:
				if arcade.check_for_collision(enemy, border):
					enemy.change_x *= -1
					enemy.change_y *= -1
		
		if len(enemies_hit_list) > 0:
			for enemy in enemies_hit_list:
				if self.player.change_y < -0.5 and not self.enemy_collision:
					enemy.remove_from_sprite_lists()
					self.player_score += 3
					arcade.play_sound(self.enemy_killed_sound)
				else:
					if not self.enemy_collision:
						self.player_life -= 1
						arcade.play_sound(self.life_lost_sound)
					self.enemy_collision = True
		else:
			self.enemy_collision = False

	def player_info(self):
		text_x = (self.viewport_horizontal_start + self.width) - (self.width * 0.15)
		text_y = (self.viewport_vertical_start + self.height) - (self.height * 0.1)
		
		score_text = f"SCORE:  {self.player_score}"
		arcade.draw_text(score_text, text_x, text_y, arcade.csscolor.GRAY, 45, font_name=('fgarcade/data/fonts/monogram_extended.ttf'))

		life_text = f"LIFE:  {self.player_life}"
		arcade.draw_text(life_text, text_x, text_y - 35, arcade.csscolor.GREY, 45, font_name=('fgarcade/data/fonts/monogram_extended.ttf'))

	def on_update(self, dt):
		super().on_update(dt)
		
		self.enemies.update()
		self.enemies.update_animation()
		
		self.collision_with_coins()
		self.collision_with_lifes()
		self.collision_with_spikes()
		self.collision_with_enemies()

		if self.player.change_y > 0:
			if not self.jumping:
				arcade.play_sound(self.jump_sound)
			self.jumping = True
		else:
			self.jumping = False
		
		if self.player_life <= 0:
			self.game_over()
		
		if self.player.center_x > self.width:
			#self.next_level()
			pass
		
		if self.player.center_y < 10:
			self.game_over()

		if self.player.change_x == 0:
			self.count_frames += 1
			if self.count_frames >= 50:
				self.count_frames = 0
				self.game_over()

	def draw_elements(self):
		super().draw_elements()

		self.coins.draw()
		self.lifes.draw()
		self.spikes.draw()
		self.enemies.draw()
		self.enemy_limits.draw()
		self.player_info()
	
	def game_over(self):
		arcade.pause(1)
		arcade.close_window()

if __name__ == "__main__":
	Game().run()
