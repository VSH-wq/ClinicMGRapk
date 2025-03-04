[app]
# (str) Title of your application
title = ClinicMGR

# (str) Package name (all lowercase, no spaces)
package.name = clinicmgr

# (str) Package domain (unique identifier, usually in reverse domain notation)
package.domain = org.example

# (str) Source code directory (where main.py is located)
source.dir = .

# (str) The main .py file of your app
source.main = main.py

# (str) Application versioning
version = 0.1

# (list) Application requirements separated by commas
requirements = python3,kivy,cython

# (str) Icon file path (optional, adjust if you have an icon)
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation: portrait, landscape or all
orientation = portrait

# (bool) Set to 1 to enable fullscreen mode
fullscreen = 1

[buildozer]
# (str) Buildozer configuration log level
log_level = 2

# (bool) Warn if running Buildozer as root (not recommended)
warn_on_root = 1

[app:android]
# (list) Android permissions your app needs (e.g., INTERNET)
android.permissions = INTERNET

# (int) Android API level to use (adjust based on your target)
android.api = 28

# (int) Minimum API level supported by your app
android.minapi = 21

# (str) Android SDK version to use (typically set automatically)
android.sdk = 20

# (str) Android NDK version to use (must be compatible with your SDK/API)
android.ndk = 19b

# (int) Android NDK API level (recommended value is 21)
android.ndk_api = 21
