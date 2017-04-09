################################################################################
#   Lamps.py
#
#   <Module Purpose>
#
#   06.04.2017  Created by: Rada Telyukova
################################################################################

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
time.sleep(3)
#mc.postToChat('Hello Minecraft!')

# Posishon

pos = mc.player.getPos()
mc.postToChat(str(pos.x) + ', ' + str(pos.y) + ', ' + str(pos.z))

def build_base(x, y, z, blockType):
    mc.setBlock(x, y, z, blockType)
    
build_base(pos.x, pos.y, pos.z, 1)
