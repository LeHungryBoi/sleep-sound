@echo off
echo Building sleep-sound...
go build -o sleep-sound.exe
if %ERRORLEVEL% EQU 0 (
    echo Build successful!
    echo Run with: sleep-sound.exe [options]
) else (
    echo Build failed!
)
