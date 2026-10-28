# بازی چکش‌زدن — پروژه اندروید

این نسخه، بازی Pygame اولیه را با Kivy بازنویسی می‌کند تا لمس صفحه در اندروید به‌عنوان ورودی بازی عمل کند.

## فایل‌ها
- `main.py`: کد بازی
- `buildozer.spec`: تنظیمات بسته‌بندی APK

## ساخت APK در Ubuntu یا WSL2

1. کپی کردن این پوشه در محیط Ubuntu/WSL2
2. نصب وابستگی‌های سیستم طبق راهنمای رسمی Buildozer:
   https://buildozer.readthedocs.io/en/stable/installation.html
3. ساخت محیط مجازی:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install buildozer
   ```
4. در همین پوشه اجرا کن:
   ```bash
   buildozer -v android debug
   ```
5. پس از موفقیت، فایل APK در پوشه `bin/` ساخته می‌شود.

ساخت اولیه ممکن است زمان‌بر باشد چون Android SDK و NDK دانلود می‌شوند.

## نکته
این ZIP شامل سورس و تنظیمات پروژه است، نه فایل APK کامپایل‌شده. برای تولید APK به محیط ساخت اندروید نیاز است.
