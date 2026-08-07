# Python Virtual Environment Setup - Cross-Platform Guide

## Setup Instructions

### First Time Setup (All Platforms)

1. **Create virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**

   **Windows (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   **Windows (Command Prompt):**
   ```bash
   .venv\Scripts\activate.bat
   ```
   
   **Windows (Using helper script):**
   ```bash
   .\activate.bat
   ```

   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   # or use the helper script
   ./activate.sh
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Deactivate when done:**
   ```bash
   deactivate
   ```

## Troubleshooting

### Windows Issues

**Error: "The module could not be loaded"**
- Use the `.bat` file instead: `.venv\Scripts\activate.bat`
- Or use the helper: `.\activate.bat`
- If PowerShell policy issues persist, try running: `Set-ExecutionPolicy -ExecutionPolicy RemoteS signed -Scope CurrentUser`

**Error: "Permission denied"**
- Remove and recreate the venv:
  ```powershell
  Remove-Item -Path .\.venv -Recurse -Force
  python -m venv .venv
  ```

### macOS/Linux Issues

If activation fails, ensure execute permissions:
```bash
chmod +x activate.sh
./activate.sh
```

## Important Notes

- The `.venv/` directory is **NOT** tracked in git (see `.gitignore`)
- Each developer/machine creates its own local virtual environment
- All Python packages are installed in your local venv via `pip install -r requirements.txt`
