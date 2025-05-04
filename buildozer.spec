[app]

# (اسم تطبيقك الظاهر للمستخدم)
title = CapApp

# (اسم الحزمة ورابط الدومين الخاص بك)
package.name = capapp
package.domain = org.jafgh

# مسار المجلد الذي يحتوي على شيفرتك المصدرية
source.dir = .

# امتدادات الملفات التي تريد تضمينها (كالموديل ONNX والصور وملفات KV)
source.include_exts = py,kv,png,jpg,atlas,onnx
source.include_dirs = assets

# رقم الإصدار
version = 0.1

# المتطلبات: عدّل حسب المكتبات التي يستخدمها مشروعك
requirements = python3,kivy,requests,onnxruntime

# إعدادات الواجهة
orientation = portrait
fullscreen = 0
window.fsaa = 2

# (اختياري) إذا لديك أيقونات أو صور شاشة تحميل
# android.icon = assets/icon.png
# android.presplash = assets/presplash.png

[buildozer]

# مستوى الطباعة في اللوغ
log_level = 2
warn_on_root = 1

# إذا أردت ملف خارجي لبيانات اللوغ
# log_file = buildozer.log

#------------------------------------------------------------------------------  
# إعدادات Android (عدّل الأرقام إذا لزم الأمر)
#------------------------------------------------------------------------------

# نسخة API التي تريد البناء ضدّها
android.api = 33

# أقل نسخة Android تدعمها
android.minapi = 21

# إعدادات SDK/NDK (يمكنك تغيير الإصدارات حسب حاجة Buildozer لديك)
android.sdk = 20
android.ndk = 23b

# بنية المعالج
android.arch = arm64-v8a

# (اختياري) إذا كنت تريد تضمين صلاحيات إضافية
# android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE
