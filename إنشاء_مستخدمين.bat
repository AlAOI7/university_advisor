@echo off
echo ===================================
echo جاري إنشاء المستخدمين التجريبيين...
echo ===================================
echo.

python manage.py shell < create_users.py

echo.
echo ===================================
echo تم الانتهاء!
echo ===================================
echo.
echo يمكنك الآن تسجيل الدخول:
echo http://127.0.0.1:8000/accounts/login/
echo.
echo البيانات:
echo   student / 123456
echo   admin / admin123
echo   test / test123
echo.
pause
