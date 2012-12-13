from simplekml import Kml, Types
from .model import Network, Location

class KMLConvert(object):
    _network_format = "BSSID: %(bssid)s<br/>SSID: %(ssid)s<br/>Capabilities: %(capabilities)s<br/>Frequency: %(frequency)d<br/>Last Time: %(lasttime)s"
    _location_format = "BSSID: %(bssid)s<br/>Altitude: %(altitude)d<br/>Level: %(level)d<br/>Accuracy: %(accuracy)d<br/>Time: %(time)s"
    def from_networks(self, doc_name, networks):
        kml = Kml(name=doc_name)
        for n in networks:
            p = kml.newpoint(name=str(n))
            p.coords=[(n.lastlon,n.lastlat)]
            if(not n._lasttime):
                lasttime = "<i>None</i>"
            else:
                lasttime = n.formated_lasttime
                p.timestamp.when = n.lasttime.strftime("%Y-%m-%dT%H:%M:%SZ-05:00")
            
            if(not n.frequency):
                frequency = "<i>None</i>"
            else:
                frequency = "%s MHz" % n.frequency

            p.description = self._network_format % {"bssid": n.bssid, "ssid": (n.ssid or "<i>None</i>"), "capabilities": n.capabilities, "frequency": frequency, "lasttime": lasttime}

        return kml

    def from_locations(self, doc_name, track_name, locations):
        when = {}
        for l in locations:
            try:
                if(l.bssid not in when):
                    when[l.bssid]=[]
                when[l.bssid].append({"time": l.time.strftime("%Y-%m-%dT%H:%M:%SZ-05:00"), "coords": (l.lon,l.lat)})
            except:
                continue

        kml = Kml(name=doc_name)
        doc = kml.newdocument(name=track_name)
         
