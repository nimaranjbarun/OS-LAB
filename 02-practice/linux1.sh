mkdir test # ساخت پوشه تست
ls # نمایش پوشه فعلی بعد از ساخت پوشه تست
touch php.php go.go python.py # ساخت چند فایل
ls # نمایش فایل های ساخته شده
cp php.php go.go python.py ./test # کپی کردن فایل ها در پوشه تست
cd test # ورود به پوشه تست
ls # نمایش محتویات پوشه تست
cd .. # برگشت به پوشه والد
rm -r test php.php go.go python.py # حذف پوشه تست و فایل های ساخته شده برای کپی کردن
ls # نمایش پ.شه جاری بعد از حذف پوشه تست و فایل ها
