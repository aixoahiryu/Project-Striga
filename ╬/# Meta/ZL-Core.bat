cd D:\

del ZL-Core.rar
rd /Q /S ZL-Core
del C:\cygwin64\home\Administrator\.bash_history
rd /Q /S C:\cygwin64\home\Administrator\.w3m
xcopy /E /I "D:\MEGA\ZL-Core" "D:\ZL-Core"
xcopy /E /I "C:\Users\Administrator\AppData\Roaming\Notepad++\backup" "D:\ZL-Core\Note\Notepad++\backup"
copy "C:\Users\Administrator\AppData\Roaming\Notepad++\session.xml" "D:\ZL-Core\Note\Notepad++\session.xml"
xcopy /E /I "C:\cygwin64\home" "D:\ZL-Core\Cygwin\home"

"C:\Program Files\WinRAR\WinRAR.exe" a "ZL-Core.rar" "ZL-Core"
copy "ZL-Core.rar" "D:\MEGA\ZL-Core.rar"
copy "ZL-Core.rar" "D:\History\ZL %date:/=-%.rar"

cd D:\Git\ZL-Temp
rd /Q /S Commit
rd /Q /S Config
rd /Q /S Cygwin
rd /Q /S Experiment
rd /Q /S Note
rd /Q /S Toolbar
xcopy /E /I "D:\ZL-Core" "D:\Git\ZL-Temp"