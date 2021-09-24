from setuptools import setup

APP_NAME = 'CyberDonut'
APP = ['main.py']
DATA_FILES = ['cyberdonut.png']
OPTIONS = {
 'iconfile':'cyberdonut.icns',
 'argv_emulation': True,
 'packages': ['certifi'],
 'plist': {
     'CFBundleName': 'CyberDonut',
     'CFBundleVersion': 'First Beta'
 }
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)