from pathlib import Path

APP_PATH = Path(__file__).resolve().parent.parent / "app.py"

exec(
    compile(
        APP_PATH.read_text(encoding="utf-8"),
        str(APP_PATH),
        "exec"
    ),
    {"__file__": str(APP_PATH), "__name__": "__main__"}
)