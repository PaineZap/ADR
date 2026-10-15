[app]
title = Discord Android Agent
package.name = discordagent
package.domain = org.bot
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Khai báo các thư viện phụ thuộc đúng với requirements.txt
requirements = python3,kivy,discord.py,asyncio,aiohttp,charset-normalizer,idna,multidict,yarl

orientation = portrait
fullscreen = 0

# Bắt buộc phải có quyền INTERNET để app kết nối Discord
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
