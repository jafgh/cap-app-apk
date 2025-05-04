[app]
title = CapApp
package.name = capapp
package.domain = org.jafgh
source.dir = .
source.include_exts = py,kv,png,jpg,atlas,onnx
source.include_dirs = assets
version = 0.1
requirements = python3,kivy,requests,onnxruntime
orientation = portrait
fullscreen = 0
window.fsaa = 2

[buildozer]
log_level = 2
warn_on_root = 1

# Android settings
android.api = 33
android.minapi = 21
android.sdk = 20
android.ndk = 23b
android.arch = arm64-v8a
