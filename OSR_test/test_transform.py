# -*- coding: utf-8 -*-

# Customize this starter script by adding code
# to the run_script function. See the Help for
# complete information on how to create a script
# and use Script Runner.

""" Your Description of the script goes here """

# Some commonly used imports

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from math import sqrt


def run_script(iface):
    p19 = QgsPoint(500000,8600000)
    utm19 = QgsCoordinateReferenceSystem(32619, \
                                       QgsCoordinateReferenceSystem.PostgisCrsId)
    utm24 = QgsCoordinateReferenceSystem(32624, \
                                        QgsCoordinateReferenceSystem.PostgisCrsId)
    trans19_24 = QgsCoordinateTransform(utm19, utm24)
    trans24_19 = QgsCoordinateTransform(utm24, utm19)
    p24 = trans19_24.transform( p19 )
    p19_roundtrip = trans24_19.transform( p24 )
    print p19
    print p24
    print p19_roundtrip
    dist = sqrt( p19.sqrDist(p19_roundtrip) )
    print dist

    if dist > 0.001:
        ￼iface.messageBar().pushMessage("Error", "QGis kan ikke transformere Groenlandske data korrekt!", \
             level=QgsMessageBar.CRITICAL)
    else:
        iface.messageBar().pushMessage("Error", "QGis kan transformere Groenlandske data", \
             level=QgsMessageBar.INFO)