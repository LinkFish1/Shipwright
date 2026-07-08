@echo off
cd /d e:\Shipwright-wind-waker-style-cel-shading
cmake --build build/x64 --config Release --target soh > build_log6.txt 2>&1
echo BUILD_EXIT_CODE=%ERRORLEVEL% >> build_log6.txt
