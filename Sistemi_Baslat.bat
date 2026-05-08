@echo off
echo Akilli Geri Donusum Sistemi Baslatiliyor... Lutfen bekleyin.
cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run dashboard_app.py