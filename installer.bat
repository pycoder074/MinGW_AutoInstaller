@echo off
:: Check if MinGW is already installed by looking for the GCC binary
where g++ >nul 2>nul
if %errorlevel%==0 (
    echo MinGW is already installed.
    exit /b
)

:: Step 1: Download the MinGW Installer
echo Downloading MinGW...
powershell -Command "Invoke-WebRequest -Uri https://sourceforge.net/projects/mingw-w64/files/latest/download -OutFile mingw-installer.exe"

:: Step 2: Install MinGW silently
echo Installing MinGW...
mingw-installer.exe /S /D=C:\MinGW

:: Step 3: Add MinGW to system PATH
echo Adding MinGW to PATH...
setx PATH "%PATH%;C:\MinGW\bin"

:: Step 4: Verify the installation
echo Verifying MinGW installation...
where g++

:: Finished
echo MinGW installation complete!
pause
