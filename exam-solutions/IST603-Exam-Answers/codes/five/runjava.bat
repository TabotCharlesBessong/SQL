@echo off
if "%~1"=="" (
    echo Usage: runjava ^<filename_without_extension^>
    echo Example: runjava Test
    goto :eof
)

echo Compiling %1.java...
javac "%1.java"

if errorlevel 1 (
    echo Compilation failed!
    goto :eof
)

echo Compilation successful. Running %1...
java "%1"

if errorlevel 1 (
    echo Execution failed!
) else (
    echo Program completed successfully.
)