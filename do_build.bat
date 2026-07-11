@echo off
setlocal
for /f "tokens=1-3 delims=/: " %%a in ("%date% %time%") do set TS=%%a%%b%%c
set LOG=e:\Shipwright-wind-waker-style-cel-shading\buildres_%TS%.log
taskkill /im msbuild.exe /f >nul 2>&1
taskkill /im cl.exe /f >nul 2>&1
timeout /t 2 >nul 2>&1
echo BUILD_START > "%LOG%"
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x64 >> "%LOG%" 2>&1
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\MSBuild\Current\Bin\MSBuild.exe" "e:\Shipwright-wind-waker-style-cel-shading\soh\soh.sln" /p:Configuration=Release /p:Platform=x64 /m /nologo /verbosity:minimal >> "%LOG%" 2>&1
echo MSBUILD_EXIT_%ERRORLEVEL% >> "%LOG%"
