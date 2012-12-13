import datetime
import time
import re
import sqlalchemy as sa
from sqlalchemy import orm

def _parse_javadate(timeval):
    try:
        return datetime.datetime.fromtimestamp(int(str(timeval)[:-3]))
    except:
        return None

def _format_datetime(dt, fmt=None):
    if(not dt):
        return "None"
    else:
        if(fmt):
            return dt.strftime(fmt)
        else:
            return dt.ctime()

class Location(object):
    @property
    def time(self):
        return _parse_javadate(self._time)

    @property
    def ssid(self):
        return str(orm.object_session(self).query(Network).filter_by(bssid=self.bssid).one().ssid)

    @property
    def formatted_time(self):
        return _format_datetime(self.time)

    def __str__(self):
        "%(lat)f,%(lon)f" % {"lat": self.lat, "lon": self.lon}

    def __repr__(self):
        return "<Location(bssid=%(bssid)s,ssid='%(ssid)s',lat=%(lat)f,lon=%(lon)f,accuracy=%(accuracy)d,altitude=%(altitude)s,time='%(time)s')>" % {"bssid": self.bssid, "ssid": self.ssid, "lat": self.lat, "lon": self.lon, "accuracy": self.accuracy, "altitude": self.altitude, "time": self.formatted_time}

class Network(object):
    @property
    def lasttime(self):
        return _parse_javadate(self._lasttime)

    @property
    def formatted_lasttime(self):
        return _format_datetime(self.lasttime)

    @property
    def lastcoords(self):
        return {"latitude": self.lastlat, "longitude": self.lastlon}

    @property
    def locations(self):
        try:
            return orm.object_session(self).query(Location).filter_by(bssid=self.bssid).all()
        except:
            return []

    @property
    def capabilities(self):
        return re.findall(r"\[(.*?)\]", str(self._capabilities))

    def __str__(self):
        return "%(ssid)s (%(bssid)s)" % {"ssid": self.ssid, "bssid": self.bssid}

    def __repr__(self):
        return "<Network(bssid='%(bssid)s',ssid='%(ssid)s',capabilities='%(capabilities)s')>" % {"bssid": self.bssid, "ssid": self.ssid, "capabilities": str(self._capabilities)}
