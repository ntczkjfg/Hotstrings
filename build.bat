if exist "hotstrings.exe" (
	del /Q "hotstrings.exe"
)
if exist "hotstrings.json" (
	del /Q "hotstrings.json"
)
if exist "log.txt" (
	del /Q "log.txt"
)
if exist "src\__pycache__" (
	rmdir /S /Q "src\__pycache__"
)
pyinstaller --add-data "assets\images\normal.ico;." --add-data "assets\images\paused.ico;." --add-data "src\hotstrings.json;." --onefile --noconsole --icon="assets\images\normal.ico" "src\hotstrings.py"
move /Y "dist\hotstrings.exe" .
ren "hotstrings.exe" "Hotstrings.exe"
rmdir /S /Q "dist"
rmdir /S /Q "build"
del /Q "hotstrings.spec"