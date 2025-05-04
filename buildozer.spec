[app]
# اسم التطبيق الظاهر للمستخدم
title = CapApp

# اسم الحزمة ودومينك العكسي
package.name = capapp
package.domain = org.jafgh

# مسار الشيفرة المصدرية
source.dir = .

# امتدادات وملفات الأصول المطلوب تضمينها
source.include_exts = py,kv,png,jpg,atlas,onnx
source.include_dirs = assets

# إصدار التطبيق
version = 0.1

# المتطلبات البرمجية
requirements = python3,kivy,requests,onnxruntime

# إعدادات الواجهة
orientation = portrait
fullscreen = 0
window.fsaa = 2

[buildozer]
log_level = 2
warn_on_root = 1

#------------------------------------------------------------------------------  
# إعدادات Android
#------------------------------------------------------------------------------

# نسخة Android API المستهدفة
android.api = 33

# أقل نسخة Android مدعومة
android.minapi = 21

# إعدادات SDK/NDK الخاصة بـ Buildozer
android.sdk = 20
android.ndk = 23b

# معمارية المعالج
android.arch = arm64-v8a, armeabi-v7a

# استخدم فرع الـ python-for-android الأحدث (اختياري)
p4a.branch = develop
