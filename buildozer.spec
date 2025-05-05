[app]
# اسم التطبيق كما سيظهر على الجهاز
title = CAPTCHA Solver
# اسم الحزمة (حروف وأرقام وبدون مسافات)
package.name = capapp
# نطاق الحزمة
package.domain = org.yourdomain

# المجلد الرئيسي للمصدر
source.dir = .
# امتدادات الملفات التي يجب تضمينها
source.include_exts = py,png,jpg,kv,atlas,onnx

# المتطلبات التي يحتاجها التطبيق
# ملاحظة: torch و torchvision قد لا يعملان بشكل مباشر على Android،
# يمكن استبدالهما بنسخ tflite أو استخدام onnxruntime فقط.
requirements = python3,kivy,onnxruntime,opencv-python,numpy,pillow,requests,python-bidi

# اتجاه التطبيق (portrait أو landscape)
orientation = portrait

# مستوى السجل (0–2)
log_level = 2

# أذونات الأندرويد المطلوبة
android.permissions = INTERNET

# إعدادات توليد الحزمة للأندرويد
# نسخة تنفيذية مُشترَكة مع armeabi-v7a و arm64-v8a تلقائيًا
android.arch = armeabi-v7a,arm64-v8a

# إصدار SDK الأدنى والأقصى (يمكن تعديله حسب حاجتك)
# android.minapi = 21
# android.target = 30

[buildozer]
# مسار ملف الجافا السمتيك
android.sdk_path = /home/builduser/.buildozer/android/platform/android-sdk
android.ndk_path = /home/builduser/.buildozer/android/platform/android-ndk
