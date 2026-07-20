## Virtual environment setup and requirements installation commands
1. python3 -m venv venv

   - On macOS / Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

   - On Windows CMD:
     ```cmd
     .\venv\Scripts\activate.bat
     ```

   - On Git Bash / WSL:
     ```bash
     source venv/Scripts/activate
     ```

   If your virtual environment is named `.venv`, replace `venv` with `.venv` in the path.

2. Install package: pip install requests

3. Requirements install: pip freeze > requirements.txt