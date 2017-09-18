@echo off
rem django起動用bat
echo start wakeup.bat
echo pythonの起動を確認します
tasklist | find "python.exe" > NUL
if not errorlevel 1  (
    echo pythonが起動しているため終了します
    taskkill /F /IM "python.exe"
)
echo pythonを起動します
call Scripts\activate
call python account_book\manage.py runserver 0.0.0.0:8000
exit /B
