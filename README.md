# smart-expense-tracker
CLI to analyze expenses from CSV

## How to run
```powershell
python -m src.tracker --input .\data\sample_expenses.csv --month 2026-01
python -m src.tracker --input .\data\sample_expenses.csv --month 2026-01 --export .\reports\report_2026-01.csv

5) **Guardar**
- Notepad: `Ctrl + S`
- Si te pide guardar como, asegúrate que se llame `README.md` y no `README.md.txt`

---

## B) Hacer Commit y Push con Git GUI
1) Abre **Git GUI** (ya lo tienes).
2) En la izquierda, en **Unstaged Changes**, debes ver `README.md` (si no sale, pulsa **Rescan**).
3) Pulsa **Stage Changed** (para pasar los cambios a la zona verde).
4) En **Commit Message**, escribe exactamente:

**Add usage instructions**

5) Pulsa **Commit**
6) Pulsa **Push**

✅ Con eso se sube a GitHub.

---

## C) Si “Push” falla y te pide login
A veces Git GUI abre una ventanita o te pide credenciales:
- Si te pide usuario/contraseña: **NO uses la contraseña normal** de GitHub.
- Tienes que usar un **Personal Access Token (PAT)** como contraseña.

Si te pasa eso, dime qué mensaje exacto te sale al hacer **Push** y te digo qué opción tocar (según el error).
