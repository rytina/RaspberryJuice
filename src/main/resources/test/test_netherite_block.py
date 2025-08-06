import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

mc.postToChat("Test: place NETHERITE_BLOCK")
time.sleep(1)

x, y, z = mc.player.getPos()

try:
    mc.setBlock(x + 1, y, z, block.NETHERITE_BLOCK)
    mc.postToChat("Block successfully placed!")
except AttributeError:
    mc.postToChat("The MCPI API does not know 'NETHERITE_BLOCK'.")
except Exception as e:
    mc.postToChat(f"Server error: {e}")
