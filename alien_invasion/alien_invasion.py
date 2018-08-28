import pygame
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	#创建一艘飞船
	ship = Ship(ai_settings, screen)

    #创建一个用于存储子弹的编组
	bullets = Group()
	aliens = Group()
	#创建一个外星人
	# alien = Alien(ai_settings, screen)
	gf.create_fleet(ai_settings,screen, ship, aliens)
	# 创建Play按钮
	play_button = Button(ai_settings, screen, "Play")
	# 创建存储游戏统计信息的实例，并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏的主循环
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			bullets.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
	#  让最近绘制的屏幕可见
		pygame.display.flip()

run_game()

