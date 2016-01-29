import curses
import time
import sys
import random

# function to add a number to an empty place on the screen

def add_number(scr, width, height):
  # loop forever

  while True:
    # make up a random position
  
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    
    # check if the character at the position is a space
    
    if scr.inch(y, x) == ord(" "):
      # if it is, replace it with a number and return
    
      scr.addch(y, x, ord("0") + random.randint(1, 9))
      
      return

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

  # empty tail
  
  tail = []
  length = 10

  # add the first number
      
  add_number(scr, width, height)
    
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

    # change the current position
          
    x = x + dx
    y = y + dy

    # get the character at the current position
    
    ch = scr.inch(y, x)

    if ch >= ord("1") and ch <= ord("9"):    
      # it's a number
    
      length = length + ch - ord("0")
      
      # add a new number
      
      add_number(scr, width, height)
    elif ch != ord(" "):   
      # it's not a space
             
      break

    # check if the tail has reached the maximum length      
      
    if len(tail) == length:
      # get the position of the end of the tail
    
      xb, yb = tail.pop(0)
      
      # replace the character with a space
      
      scr.addch(yb, xb, ord(" "))

    # add the current position to the tail      
                    
    tail.append((x, y))
    
    # replace the character with a "O"
    
    scr.addch(y, x, ord("O"), curses.color_pair(1))
    
    # update the screen
    
    scr.refresh()
    
    # wait for 1/20 of a second
    
    time.sleep(0.05)
    
curses.wrapper(snake)
