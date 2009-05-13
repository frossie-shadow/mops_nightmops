from DayMOPSObject import DayMOPSObject
import numpy



# Constants
STABLE_STATUS = {'STABLE':      'Y',
                 'UNSTABLE':    'N''}


class Orbit(DayMOPSObject):
    def __init__(self, 
                 q, 
                 e, 
                 i, 
                 node, 
                 argPeri, 
                 timePeri, 
                 epoch, 
                 src=[],
                 orbFitResidual=None,
                 orbFitChi2=None,
                 classification=None,
                 stablePass=STABLE_STATUS['UNSTABLE'],
                 moid1=None,
                 moid2=None,
                 moidLong1=None,
                 moidLong2=None):
        """
        q (AU)
        e
        i (deg)
        node (deg)
        argPeri (deg)
        timePeri (TAI MJD)
        epoch: orbit epoch (TAI MJD)
        src: 21 element array (covariance matrix in diagonal form).
        """
        self._q = q
        self._e = e
        self._i = i
        self._node = node
        self._argPeri = argPeri
        self._timePeri = timePeri
        self._epoch = epoch
        self.setSrc(src)
        
        self._orbFitResidual = orbFitResidual
        self._orbFitChi2 = orbFitChi2
        self._classification = classification
        self._stablePass = stablePass
        self._moid1 = moid1
        self._moid2 = moid2
        self._moidLong1 = moidLong1
        self._moidLong2 = moidLong2
        return


    def setSrc(self, src):
        """
        If all elements of the covariance list are not None, then cast that
        list into a numpy.array. Return the casted array or None in case the
        covariance is invalid (i.e. has null elements).
        """
        self._src = []
        if(not None in src):
            self._src = numpy.array([float(e) for e in src])
        return



