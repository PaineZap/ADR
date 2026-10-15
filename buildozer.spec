[app]
title = Discord Android Agent
package.name = discordagent
package.domain = org.bot
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Sử dụng aiohttp==3.9.5 tương thích hoàn toàn với bản python-for-android hiện tại
requirements = python3,kivy==2.2.1,discord.py,asyncio,aiohttp==3.9.5,charset-normalizer,idna,multidict,yarl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
