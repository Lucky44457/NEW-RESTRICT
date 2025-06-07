# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import asyncio
import os
import sys
import importlib
from shared_client import app  # Shared Pyrogram client instance

PLUGIN_DIR = "plugins"

async def load_plugins():
    # Scan the plugins directory and import each .py file
    for filename in os.listdir(PLUGIN_DIR):
        if filename.endswith(".py") and filename != "__init__.py":
            plugin_name = filename[:-3]
            try:
                importlib.import_module(f"{PLUGIN_DIR}.{plugin_name}")
                print(f"✅ Loaded plugin: {plugin_name}")
            except Exception as e:
                print(f"❌ Failed to load {plugin_name}: {e}")

async def main():
    await load_plugins()
    print("🚀 Bot is running...")
    await app.start()  # Start the shared Pyrogram client
    await idle()       # Keeps the bot running (like infinite loop)

from pyrogram import idle

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("🛑 Shutdown by user")
    except Exception as e:
        print(f"⚠️ Error: {e}")
        sys.exit(1)
    finally:
        try:
            loop.run_until_complete(app.stop())
            loop.close()
        except Exception:
            pass
