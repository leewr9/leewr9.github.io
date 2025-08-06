@echo off
REM 모든 하위 폴더의 .html 파일을 찾아서 djlint로 포맷

echo Searching for all .html files and formatting with djlint...

FOR /R %%F IN (*.html) DO (
    echo Formatting %%F
    djlint "%%F" --reformat
)

echo.
echo ===== djlint formatting completed =====
pause
