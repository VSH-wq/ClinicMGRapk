[app]
# Application title
title = ClinicMGR

# Package details (all lowercase)
package.name = clinicmgr
package.domain = org.example

# Where your main.py is located
source.dir = .
source.main = main.py

# Version of your app
version = 0.1

# Application requirements (add any additional libraries if needed)
requirements = python3,kivy,cython

# Icon file (optional)
icon.filename = %(source.dir)s/icon.png

# Supported orientation: portrait, landscape, or all
orientation = portrait

# Fullscreen mode (1 for yes, 0 for no)
fullscreen = 1

[buildozer]
# Log level: 0=error, 1=info, 2=debug
log_level = 2
warn_on_root = 1

[app:android]
# Android permissions required by your app
android.permissions = INTERNET

# Android API levels and SDK/NDK settings (adjust these if needed)
android.api = 29
android.minapi = 21
android.sdk = 20
android.ndk = 19b
android.ndk_api = 21

# Automatically accept SDK licenses (helps avoid interactive prompts)
android.accept_sdk_license = True

# Android architecture (you can list multiple comma-separated values)
android.arch = armeabi-v7a
