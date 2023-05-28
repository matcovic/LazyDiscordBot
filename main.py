import os, discord
from keep_alive import keep_alive
from bot import run_bot

while __name__ == '__main__':
  try:
    keep_alive()
    run_bot()
  except discord.errors.HTTPException as e:
    print(e)
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system('kill 1')
