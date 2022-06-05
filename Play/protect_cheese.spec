# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['protect_cheese.py'],
             pathex=['adding.py', 'bullet.py', 'button.py', 'cat.py', 'game_functions.py', 'game_stats.py', 'mouse.py', 'scoreboard.py', 'settings.py', 'Z:\\study\\PycharmFiles\\Pygame\\Protect Cheese'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='protect_cheese',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='cat.ico')
