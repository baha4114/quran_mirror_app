[app]

# نام اپلیکیشن (روی گوشی نمایش داده می‌شود)
title = Quran Mirror

# نام بسته و دامنه (این‌ها را می‌توانید تغییر دهید)
package.name = quranmirror
package.domain = ir.parsavesta.quranmirror

source.dir = .

# پسوندهایی که داخل اپلیکیشن گنجانده می‌شوند
source.include_exts = py,csv,json,ttf,otf,jpg,jpeg,png,mp3,mp4,pdf,txt

# پوشهٔ assets به‌طور کامل داخل اپ قرار می‌گیرد (دیتا، فونت، تصویر، صدا)
source.include_patterns = assets/*

# پوشه‌هایی که نادیده گرفته می‌شوند
source.exclude_dirs = tests, bin, .git, __pycache__, .buildozer

version = 2.0

# کتابخانه‌های مورد نیاز
# python-bidi روی نسخهٔ خالص پایتون (0.4.2) قفل شده تا روی اندروید بدون خطا بیلد شود
requirements = python3,kivy==2.3.0,arabic_reshaper,python-bidi==0.4.2

# جهت نمایش — عمودی (موبایل)
orientation = portrait
fullscreen = 0

# آیکون و اسپلش (در صورت تمایل جایگزین کنید)
# icon.filename = %(source.dir)s/assets/icon.png
# presplash.filename = %(source.dir)s/assets/bg.jpg
presplash.filename = %(source.dir)s/assets/bg.jpg

android.presplash_color = #0d1424

# دسترسی‌ها (حداقلی — اپ آفلاین کار می‌کند)
android.permissions = INTERNET

# نسخه‌های API اندروید
android.api = 34
android.minapi = 24
android.ndk_api = 24

# معماری‌های پردازنده (اکثر گوشی‌های امروزی arm64-v8a هستند)
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = 1

# bootstrap پیش‌فرض برای Kivy
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
