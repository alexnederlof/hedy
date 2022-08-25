# This file is the specification for packaging hedy
# To make a package, run `pyinstaller app.spec -y`
# On Mac, you can run the executable from dist/Hedy/Hedy
# Or open the actually packaged app
block_cipher = None

a = Analysis(
  ['desktop.py'],
  pathex = [],
  binaries = [],
  datas = [
    ('content','content'),
    ('image','image'),
    ('static','static'),
    ('templates','templates'),
    ('translations','translations'),
    ('grammars','grammars'),
    ('grammars-Total','grammars-Total'),
    ('grammars-transformed','grammars-transformed'),
  ],
  hiddenimports = ['configparser'],
  hookspath = [],
  hooksconfig = {},
  runtime_hooks = [],
  excludes = [],
  win_no_prefer_redirects = False,
  win_private_assemblies = False,
  cipher = block_cipher,
  noarchive = False
)
pyz = PYZ(a.pure, a.zipped_data, cipher = block_cipher)

exe = EXE(
  pyz,
  a.scripts,
  [],
  exclude_binaries = True,
  name = 'Hedy',
  debug = False,
  bootloader_ignore_signals = False,
  strip = False,
  upx = True,
  console = False,
  disable_windowed_traceback = False,
  argv_emulation = False,
  target_arch = None,
  codesign_identity = None,
  entitlements_file = None
)
coll = COLLECT(
  exe,
  a.binaries,
  a.zipfiles,
  a.datas,
  strip = False,
  upx = True,
  upx_exclude = [],
  name = 'Hedy'
)
app = BUNDLE(
  coll,
  name = 'Hedy.app',
  icon = 'static/images/Hedy-logo.png',
  bundle_identifier = None
)
