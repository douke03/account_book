@echo off
rem django�N���pbat
echo start wakeup.bat
echo python�̋N�����m�F���܂�
tasklist | find "python.exe" > NUL
if not errorlevel 1  (
    echo python���N�����Ă��邽�ߏI�����܂�
    taskkill /F /IM "python.exe"
)
echo python���N�����܂�
call Scripts\activate
call python account_book\manage.py runserver 0.0.0.0:8000
exit /B
