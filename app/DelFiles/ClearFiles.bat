clear
rem VladVons@gmail.com
rem Win2008R2

DEL /F /S /Q "%Windir%\Temp\"
DEL /F /S /Q c:\$Recycle.Bin\
DEL /F /S /Q "c:\Users\All Users\Medoc\Medoc\TEMP\"
DEL /F /S /Q "C:\Users\All Users\Medoc\Medoc_2SRV\TEMP\"
DEL /F /S /Q D:\1Cv77\Oster\*.cdx


SET CurDir=%cd%
rem cd %HOMEPATH%\..
cd %USERPROFILE%\..

for /d %%D in (*) do echo "%%D"

for /d %%D in (*) do DEL /F /S /Q "%%D\Downloads\"

for /d %%D in (*) do DEL /F /S /Q "%%D\Local Settings\Temp\"

for /d %%D in (*) do DEL /F /S /Q "%%D\AppData\1C\1Cv8\"
for /d %%D in (*) do DEL /F /S /Q "%%D\AppData\Local\1C\1Cv8\"
for /d %%D in (*) do DEL /F /S /Q "%%D\AppData\Roaming\1C\1Cv8\"

for /d %%D in (*) do DEL /F /S /Q "%%D\AppData\Local\Mozilla\"

for /d %%D in (*) do DEL /F /S /Q "%%D\AppData\Local\Microsoft\Windows\WebCache\"
for /d %%D in (*) do DEL /F /S /Q "%%D\AppData\Local\Microsoft\Windows\WER\"
for /d %%D in (*) do DEL /F /S /Q "%%D\AppData\Roaming\Foxit Software\"

cd %CurDir%



rem  --- Delete older than N days
rem set Exec="cmd /c del /q @PATH"
rem FORFILES /p "c:\Program Files\TradeAgent_logs" /s /m *.* /d -7 /C %Exec%
rem FORFILES /p "c:\Program Files\TradeAgent\scripts\out" /s /m *.* /d -7 /C %Exec%

net stop wuauserv 
DEL /F /S /Q "%Windir%\SoftwareDistribution\Download\"
net start wuauserv

powercfg -H off

reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Csc\Parameters /v FormatDatabase /t REG_DWORD /d 1 /f

sdelete64.exe -z c: 
rem sdelete64.exe -z d: 
