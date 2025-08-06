import mcpi.minecraft as minecraft
import mcpi.entity as entity
import time

mc = minecraft.Minecraft.create()

mc.postToChat("Test: spawn AXOLOTL")
time.sleep(1)

x, y, z = mc.player.getPos()

try:
    axolotl = getattr(entity, "AXOLOTL")
    mc.spawnEntity(x + 2, y, z, axolotl)
    mc.postToChat("Entity successfully spawned!")
except AttributeError:
    mc.postToChat("The MCPI API does not know 'AXOLOTL'.")
except Exception as e:
    mc.postToChat(f"Server error: {e}")
