@echo off

cd /d "%~dp0excel_convertor"

echo "%cd%"

@python "%cd%\\excel_convertor.py" %*

@pause
