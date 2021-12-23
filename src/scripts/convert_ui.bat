@echo off

cd src\gui

set date_du_logs=%date:~6,4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%%time:~6,2%
if not exist "logs" (MKDIR "logs")

echo [%date% - %time%] Conversion des fichiers ui : > logs\%date_du_logs%.txt
echo. >> logs\%date_du_logs%.txt
echo. >> logs\%date_du_logs%.txt

for %%f in (*.ui) do (
  echo [%date% - %time%] Conversion du fichier %%f en cours... >> logs\%date_du_logs%.txt
  pyside6-uic %%~nf.ui -o %%~nf_ui.py
  echo [%date% - %time%] Conversion du fichier %%f terminé avec succés ! >> logs\%date_du_logs%.txt
  echo. >> logs\%date_du_logs%.txt
)

echo. >> logs\%date_du_logs%.txt

echo [%date% - %time%] Conversion des fichiers ui terminés avec succés ! >> logs\%date_du_logs%.txt
