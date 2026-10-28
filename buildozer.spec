[app]

title = بازی چکش‌زدن
package.name = hammergame
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Uncomment and set a 512x512 PNG icon if you have one.
# icon.filename = %(source.dir)s/icon.png

android.permissions =
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
