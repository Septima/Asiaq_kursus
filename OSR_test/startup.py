# -*- coding: utf-8 -*-
"""
Purpose:    To test and report QGIS capability of transforming correctly
            to and from UTM-projection for coordinates far outside the UTM zone.
Author:     asger@septima.dk
Copyright:  Septima p/s 2014
License:    You are free to use this software as you please as long as this notice
            and the list of authors is preserved.
"""

from qgis.utils import qgsfunction, iface
from qgis.core import *
from qgis.gui  import *
from math import sqrt
from PyQt4.QtGui import QMessageBox

def check_osr_use_etmerc():
  """Transforms a point from UTM19 to UTM24 and back. Then checks error.
     Shows a message box with the result"""
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