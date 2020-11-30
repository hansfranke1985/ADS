SET QGIS_ROOT=C:\Program Files\QGIS 3.14
SET QGISNAME=qgis
SET QTNAME=Qt5
SET QGIS=%QGIS_ROOT%\apps\%QGISNAME%
SET QT=%QGIS_ROOT%\apps\%QTNAME%
SET QGIS_PREFIX_PATH=%QGIS%
SET PYCHARM="C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.3\bin\pycharm64.exe"

CALL "%QGIS_ROOT%"\bin\o4w_env.bat
CALL "%QT%"\bin\qtenv2.bat

path %PATH%;%QGIS%\bin
path %PATH%;%QT%\bin

SET QT_PLUGIN_PATH=%QGIS%\qtplugins;%QT%\plugins

SET PYTHONPATH=%PYTHONPATH%;%QGIS%\python
SET PYTHONPATH=%PYTHONPATH%;%QGIS_ROOT%\apps\Python37\lib\site-packages


start "PyCharm aware of QGIS" /B %PYCHARM% %*