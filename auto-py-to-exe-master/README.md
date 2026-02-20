
## Video
If you need something visual to help you get started, [I made a video for the original release of this project](https://youtu.be/OZSZHmWSOeM); some things may be different but the same concepts still apply.

## Python 2.7 Support
As of [PyInstaller v4.0](https://github.com/pyinstaller/pyinstaller/releases/tag/v4.0) released on Aug 9 2020, Python 2.7 is no longer supported; although you can still use this tool with Python 2.7 by installing an older version of PyInstaller. [PyInstaller v3.6](https://github.com/pyinstaller/pyinstaller/releases/tag/v3.6) was the last version that supported Python 2.7; to install this, first uninstall any existing versions of PyInstaller and then execute `python -m pip install pyinstaller==3.6`.

## Testing
Tests are located in `tests/` and are run using pytest:

```
$ pip install pytest
$ pip install -e .
$ pytest
```

