from .model import DBManager, Network, Location

class WifiMap(object):
    selectors = {"network": ["ssid", "bssid"], "location": ["lat", "lon", "bssid"]}

    dbmgr = None

    def __init__(self, dbfile):
        self.dbmgr = DBManager(dbfile)

    def _get_query(self, table, name, query_filter={}):
        query = self.dbmgr.session.query(table)

        if(not query_filter):
            return query

        for selector in query_filter:
            if(selector not in self.selectors[name]):
                raise Exception("Invalid %(name)s query selector: '%(selector)s'. Must be one of the following: '%(valid_selectors)s'" % {"name": name, "selector": selector, "valid_selectors": "', '".join(self.selectors[name])})
        
        return query.filter_by(**query_filter)

    def get_network(self, query_filter={}):
        return self._get_query(Network, "network", query_filter)

    def get_location(self, query_filter={}):
        return self._get_query(Location, "location", query_filter)

