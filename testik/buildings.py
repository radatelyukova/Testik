################################################################################
#   buildings.py
#
#   <Module Purpose>
#
#   08.04.2017  Created by: Rada Telyukova
################################################################################

from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc = Minecraft.create()
time.sleep(2)
mc.postToChat('Hello Minecraft!: ' + str(block.STONE.id))

# Posishon
#pos = mc.player.getPos()
#mc.postToChat(str(pos.x) + ', ' + str(pos.y) + ', ' + str(pos.z))
#x = pos.x
#y = pos.y
#z = pos.z

x = -74.0
y = 15.0
z = 246.0

# Building size
width  = 9
height = 5
length = 6 

# Building
mc.setBlocks(x, y, z, x + width, y + height, z + length, block.BRICK_BLOCK.id)
mc.setBlocks(x+1, y, z+1, x + width-1, y + height-1, z + length-1, block.AIR.id)

# Window
x_win = x + width
y_win = y + height / 2 - 1
z_win = z + length / 2 - 1
mc.setBlocks(x_win, y_win, z_win, x_win, y_win + 2, z_win + 2, block.GLASS_PANE.id)


# Door
mc.setBlocks(x + width/2, y, z, x + width/2, y + 1, z, block.AIR.id)
mc.setBlock(x + width/2, y, z, block.DOOR_WOOD.id)

# Destroy
#mc.setBlocks(x, y, z, x + width, y + height, z + length, block.AIR.id)