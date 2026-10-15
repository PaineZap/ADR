[app]

# (str) Title of your application
title = Discord Android Agent

# (str) Package name
package.name = discordagent

# (str) Package domain (needed for android packaging)
package.domain = org.bot

# (str) Source directory where the main file resides
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# 👉 KHÓA BẢN aiohttp==3.8.6 ĐỂ KHÔNG BỊ LỖI C-API CỦA CYTHON
requirements = python3,kivy==2.2.1,discord.py,asyncio,aiohttp==3.8.6,charset-normalizer,idna,multidict,yarl

# (str) Supported orientations
orientation = portrait

# (int) Indicate if the application should be full screen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK version
android.sdk = 33

# (str) List of architectures to build for
android.archs = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
