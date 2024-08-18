import time
from mcpi.minecraft import Minecraft
time.sleep(3)
mc = Minecraft.create()
mc.postToChat("火柴盒建造开始")
x, y, z = mc.player.getTilePos()
Block = 0
# Block = (可以填0或5，0是清除；5是填充)
# 下面请别改
for i in range(8):
    for j in range(5):
        mc.setBlock(x + 3 + j, y, z + i, Block, 0)
for q in range(5):
    for p in range(5):
        mc.setBlock(x + 3 + q, y + p, z, Block, 0)
for n in range(5):
    for m in range(5):
        mc.setBlock(x + 3 + n, y + m, z + 7, Block, 0)
for f in range(8):
    for g in range(5):
        mc.setBlock(x + 7, y + g, z + f, Block, 0)
for a in range(5):
    for k in range(3):
        mc.setBlock(x + 3, y + a, z + k, Block, 0)
for w in range(5):
    for e in range(3):
        mc.setBlock(x + 3, y + w, z + 5 + e, Block, 0)
for r in range(2):
    for t in range(2):
        mc.setBlock(x + 3, y + 3 + r, z + 3 + t, Block, 0)
for v in range(8):
    for h in range(5):
        mc.setBlock(x + 3 + h, y + 4, z + v, Block, 0)