@echo off
color 0a
title CRITICAL SYSTEM FAILURE - VIRUS DETECTED

:: Gọi file VBScript chạy ngầm
start "" "alarm_speak.vbs"

:: Vòng lặp hiện chữ Matrix siêu nhanh
:loop
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
start cmd /c "color 0c & echo INFECTED BY SYSTEM_ERROR_666"
goto loop
