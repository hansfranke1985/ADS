SET QGIS_ROOT=[Replace with QGIS root installation folder]
SET PYCHARM="[Replace with PyCharm root installation folder]\bin\pycharm.bat"

call "%QGIS_ROOT%"\bin\o4w_env.bat
call "%QGIS_ROOT%"\apps\qt5\bin\qtenv2.bat

path %PATH%;%QGIS_ROOT%\apps\qgis\bin
path %PATH%;%QGIS_ROOT%\apps\qt5\bin

set QT_PLUGIN_PATH=%QGIS_ROOT%\apps\qgis\qtplugins;%QGIS_ROOT%\apps\qt5\plugins

set PYTHONPATH=%PYTHONPATH%;%QGIS_ROOT%\apps\qgis\python
set PYTHONPATH=%PYTHONPATH%;%QGIS_ROOT%\apps\Python37\Lib\site-packages

set QGIS_PREFIX_PATH=%QGIS_ROOT%\apps\qgis


start "PyCharm aware of QGIS" /B %PYCHARM% %*
