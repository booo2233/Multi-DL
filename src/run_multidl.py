"""
Helper launcher for MultiDL when freezing with PyInstaller.
This ensures `multidl` is imported as a proper package,
so relative imports in __main__.py won’t break.
"""

import multidl.__main__

if __name__ == "__main__":
    # Call the Typer app defined in multidl/__main__.py
    multidl.__main__.app()
