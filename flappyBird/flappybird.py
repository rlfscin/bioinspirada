import pygame as pg
from pygame.locals import *
import numpy as np
from collections import deque
import setup as sp
import utils
from bird import Bird




def main():
	pg.init()

	display_surface = pg.display.set_mode((sp.WIN_WIDTH, sp.WIN_HEIGHT))
	pg.display.set_caption('Pygame Flappy Bird')

	images = utils.load_images()

	score_font = pg.font.SysFont(None, 32, bold=True)  # default font

	bird = Bird(50, int(sp.WIN_HEIGHT/2 - Bird.HEIGHT/2), sp.BIRD_ANIMATE,
    						(images['bird-wingup'], images['bird-wingdown']))


	pipes = deque()

    #frame_clock = 0  # this counter is only incremented if the game isn't paused
	score = 0
	done = False
	while not done:
		pg.time.delay(sp.SLEEP_TIME)

        # Handle this 'manually'.  If we used pygame.time.set_timer(),
        # pipe addition would be messed up when paused.
        #if not (paused or frame_clock % msec_to_frames(PipePair.ADD_INTERVAL)):
        #    pp = PipePair(images['pipe-end'], images['pipe-body'])
        #    pipes.append(pp)

		for e in pg.event.get():
			if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
				done = True
				break
			elif e.type == MOUSEBUTTONUP or (e.type == KEYUP and
        			e.key in (K_UP, K_RETURN, K_SPACE)):
				bird.jump = sp.JUMP_TIME
			elif e.type == KEYUP and e.key == K_KP_PLUS:
				sp.SLEEP_TIME -= 5
			elif e.type == KEYUP and e.key == K_KP_MINUS:
				sp.SLEEP_TIME += 5
        #    elif e.type == KEYUP and e.key in (K_PAUSE, K_p):
        #        paused = not paused
        	

        # check for collisions
        #pipe_collision = any(p.collides_with(bird) for p in pipes)
        #if pipe_collision or 0 >= bird.y or bird.y >= WIN_HEIGHT - Bird.HEIGHT:
        #    done = True

		for x in range(0, sp.WIN_WIDTH, sp.WIN_BACKGROUND_SIZE):
			display_surface.blit(images['background'], (x, 0))

        #while pipes and not pipes[0].visible:
        #    pipes.popleft()

        #for p in pipes:
        #    p.update()
        #    display_surface.blit(p.image, p.rect)

		bird.update()
		display_surface.blit(bird.image, bird.rect)

        # update and display score
        #for p in pipes:
        #    if p.x + PipePair.WIDTH < bird.x and not p.score_counted:
        #        score += 1
        #        p.score_counted = True

        #score_surface = score_font.render(str(score), True, (255, 255, 255))
        #score_x = WIN_WIDTH/2 - score_surface.get_width()/2
        #display_surface.blit(score_surface, (score_x, PipePair.PIECE_HEIGHT))

		pg.display.flip()
        #frame_clock += 1
	print('Game over! Score: %i' % score)
	pg.quit()







main()