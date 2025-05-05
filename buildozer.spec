[app]
# --- معلومات أساسية ---
title           = CAPTCHA Solver
package.name    = capapp
package.domain  = org.yourdomain

# --- مصدر التطبيق ---
source.dir      = .
source.include_exts = py,png,jpg,kv,atlas,onnx

# --- إصدار التطبيق (اختر طريقة واحدة فقط) ---

# 1) تعريف ثابت للإصدار
version         = 1.0.0
#version.regex   = __version__ = ['"](.*)['"]
#version.filename = %(source.dir)s/main.py

# 2) أو باستخدام التعبير النظامي/التلقائي
#version         =
#version.regex   = __version__ = ['"](.*)['"]
#version.filename = %(source.dir)s/main.py

# --- المتطلبات ---
requirements    = python3,kivy,onnxruntime,opencv-python,numpy,pillow,requests,python-bidi

# --- إعدادات العرض --
orientation     = portrait
log_level       = 2
fullscreen      = 0

# --- أذونات الأندرويد ---
android.permissions = INTERNET

# --- معماريات الأندرويد المدعومة ---
android.arch    = armeabi-v7a,arm64-v8a

# --- (اختياري) مسارات SDK و NDK ---
# إذا استخدمت buildozer لتحميلها، لا حاجة لضبطها يدوياً:
#android.sdk_path = /home/username/.buildozer/android/platform/android-sdk
#android.ndk_path = /home/username/.buildozer/android/platform/android-ndk
