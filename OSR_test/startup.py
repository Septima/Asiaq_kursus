# -*- coding: utf-8 -*-

from qgis.utils import qgsfunction, iface
from qgis.core import *
from qgis.gui  import *
from math import sqrt
from PyQt4.QtGui import QMessageBox

def check_osr_use_etmerc():
    p19 = QgsPoint(500000,8600000)
    utm19 = QgsCoordinateReferenceSystem(32619, \
                                       QgsCoordinateReferenceSystem.PostgisCrsId)
    utm24 = QgsCoordinateReferenceSystem(32624, \
                                        QgsCoordinateReferenceSystem.PostgisCrsId)
    trans19_24 = QgsCoordinateTransform(utm19, utm24)
    trans24_19 = QgsCoordinateTransform(utm24, utm19)
    p24 = trans19_24.transform( p19 )
    p19_roundtrip = trans24_19.transform( p24 )
    dist = sqrt( p19.sqrDist(p19_roundtrip) )

    if dist > 0.0001:
      msg = u"Denne QGis kan IKKE transformere Grønlandske data korrekt!"
      iface.messageBar().pushMessage("Transformation", msg, \
             level=QgsMessageBar.CRITICAL)
      QMessageBox.critical(None, "Advarsel", msg)
    else:
      msg = u"Denne QGis kan transformere Grønlandske data"
      iface.messageBar().pushMessage("Transformation", msg, \
             level=QgsMessageBar.INFO)
      QMessageBox.information(None, "Transformation", msg)

# Run method
check_osr_use_etmerc()