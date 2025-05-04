[app]
# اسم التطبيق الظاهر على الجهاز
title = CAP App

# اسم الحزمة والدومين العكسي
package.name = capapp
package.domain = org.example

# مسار الكود المصدري
source.dir = .

# نسخة التطبيق
version = 0.1

# المتطلبات (حذفت onnxruntime)
requirements = python3,kivy,requests

# طبق هذا الباتش قبل البناء
p4a_patch = patches/libffi-fix.patch

# معماريات الأندرويد المدعومة
android.arch = armeabi-v7a, arm64-v8a

# صلاحيات التطبيق
android.permissions = INTERNET

# اختيارات إضافية (اختياري)
# icon.filename = %(source.dir)s/assets/icon.png
# log_level = 2
# android.api = 31
# android.minapi = 21

[buildozer]
# نظّف البيئة تلقائياً عند إعادة البناء
clean_on_rebuild = True
