@echo off
echo Compiling %1.java...
javac "%1.java"
if %ERRORLEVEL% EQU 0 (
    echo Compilation successful. Running %1...
    java %1
) else (
    echo Compilation failed.
)
pause