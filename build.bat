if exist "hotstrings.exe" (
	del /Q "hotstrings.exe"
)
pyinstaller --onefile --noconsole --icon=normal_icon.ico hotstrings.py
move /Y "dist\hotstrings.exe" .
rmdir /S /Q "dist"
rmdir /S /Q "build"
del /Q "hotstrings.spec"