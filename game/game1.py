import curses
import time
import sys
import random

def snake(scr):
  scr.nodelay(1)
  
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

  # get screen size
  
  height, width = scr.getmaxyx()

  # start in middle of screen, moving right
  
  x = width / 2
  y = height / 2
  dx = 1
  dy = 0

  while True:
    # read a key
  
    c = scr.getch()
    
    # check for each of the four cursor directions
    
    if c == curses.KEY_UP:
      dx = 0
      dy = -1
    if c == curses.KEY_DOWN:
      dx = 0
      dy = 1
    if c == curses.KEY_LEFT:
      dx = -1
      dy = 0
    if c == curses.KEY_RIGHT:
      dx = 1
      dy = 0

    # replace the character with a space
      
    scr.addch(y, x, ord(" "))

    # change the current position
          
    x = x + dx
    y = y + dy

    # get the character at the current position
    
    ch = scr.inch(y, x)

    if ch != ord(" "):   
      # it's not a space
             
      break

    # replace the character with a "O"
    
    scr.addch(y, x, ord("O"), curses.color_pair(1))
    
    # update the screen
    
    scr.refresh()
    
    # wait for 1/20 of a second
    
    time.sleep(0.05)
    
curses.wrapper(snake)
