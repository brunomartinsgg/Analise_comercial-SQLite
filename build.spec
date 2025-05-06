# -*- mode: python -*-
from PyInstaller.utils.hooks import collect_data_files
import os

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        *collect_data_files('pandas'),
        ('Projeto_Marianne_SQLITE.db', '.'),  # Certifique-se de que o banco de dados está no diretório correto
        ('assets/images/*', 'assets/images'),
        ('assets/images/logos/*', 'assets/images/logos'),
        ('assets/icons/*', 'assets/icons')
    ],
    hiddenimports=[
        'pandas', 'numpy',
        'pytz', 'dateutil', 'matplotlib',
        'matplotlib.pyplot',
        'tkinter', 'locale'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='RelatorioVendas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,  # Definindo como False para não abrir o console
    icon=os.path.join('assets', 'icons', 'icone.ico') if os.path.exists(os.path.join('assets', 'icons', 'icone.ico')) else None
)

