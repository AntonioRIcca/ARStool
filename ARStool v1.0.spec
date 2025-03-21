# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/anton/PycharmProjects/ARStool/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/anton/PycharmProjects/ARStool/_benchmark', '_benchmark/'), ('C:/Users/anton/PycharmProjects/ARStool/_util', '_util/'), ('C:/Users/anton/PycharmProjects/ARStool/_images', '_images/'), ('C:/Users/anton/PycharmProjects/ARStool/_temp', '_temp/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ARStool v1.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\anton\\Desktop\\ARStool_ICO.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ARStool v1.0',
)
