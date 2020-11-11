SET QGIS_ROOT=C:\OSGeo4W64
SET PYCHARM="C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.3\bin\pycharm.bat"

call "%QGIS_ROOT%"\bin\o4w_env.bat
call "%QGIS_ROOT%"\apps\qt5\bin\qtenv2.bat


path %PATH%;%QGIS_ROOT%\apps\qgis\bin
path %PATH%;%QGIS_ROOT%\apps\qt5\bin

set QT_PLUGIN_PATH=%QGIS_ROOT%\apps\qgis\qtplugins;%QGIS_ROOT%\apps\qt5\plugins

set PYTHONPATH=%PYTHONPATH%;%QGIS_ROOT%\apps\qgis\python
set PYTHONPATH=%PYTHONPATH%;%QGIS_ROOT%\C:\Users\hansf\anaconda3

set QGIS_PREFIX_PATH=%QGIS_ROOT%\apps\qgis


start "PyCharm aware of QGIS" /B %PYCHARM% %*
