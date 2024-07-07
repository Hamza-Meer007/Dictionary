# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['talking.py'],
    pathex=[],
    binaries=[],
    datas=[        
            ('./assets/bg.png','assets'),
            ('./assets/clear.png','assets'),
            ('./assets/mic.png','assets'),
            ('./assets/microphone.png','assets'),
            ('./assets/exit.png','assets'),
            ('./assets/search.png','assets'),
            ('./assets/dic.ico','assets'),
            ('./assets/data.json','assets')
],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='talking',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
