import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()               #width and height
w = curses.newwin(sh, sw, 0, 0)     #will open new window and start from top left
w.keypad(1)
w.timeout(100)			            #screen will refresh after 100ms

snk_x = sw/4			            #snakes initial position
snk_y = sh/2			
snake = [					        #snakes body parts
	[snk_y, snk_x],
	[snk_y, snk_x-1],
	[snk_y, snk_x-2]
]

food = [sh/2, sw/2]   	            #food would at center of screen
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)	 		

key = curses.KEY_RIGHT

while True:
	next_key = w.getch()
	key = key if next_key == -1 else next_key

	if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:	#condition if user lost the game
		curses.endwin()
		quit()

	new_head = [snake[0][0], snake[0][1]]

	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_LEFT:
		new_head[1] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1

	snake.insert(0, new_head)

	if snake[0] == food: 				#if snake eats the food
		food = None
		while food is None:
			nf = [
				random.randint(1, sh-1), 
				random.randint(1, sw-1)
			]				#new loc of food
			food = nf if nf not in snake else None
		w.addch(food[0], food[1], curses.ACS_PI)
	else:
		tail = snake.pop()
		w.addch(int(tail[0]), int(tail[1]), ' ')
 
	w.addch(int(snake[0][0]), int(snake[0],[1]), curses.ACS_CKBOARD)
