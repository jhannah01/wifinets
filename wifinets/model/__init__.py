import os
import sqlite3
import sqlalchemy as sa
from sqlalchemy.dialects.sqlite import INTEGER, FLOAT
from sqlalchemy import orm

from .tables import *

class DBManager(object):
    session = None
    metadata = None
    engine = None
    network_table = None
    location_table = None

    def __init__(self, dbfile):
        if(not os.path.exists(dbfile)):
            Exception("No such database file: '%s'" % dbfile)
        
        self.engine = sa.create_engine("sqlite:///%s" % dbfile,
                connect_args={'detect_types': sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES},
                native_datetime=True)
        
        self.metadata = sa.MetaData(bind=self.engine, reflect=True)
        self.session = orm.scoped_session(orm.sessionmaker(bind=self.engine))
        
        self.network_table = sa.Table("network", self.metadata,
                #sa.Column("lasttime", INTEGER),
                autoload=True, extend_existing=True)

        self.location_table = sa.Table("location", self.metadata,
                #sa.Column("time", INTEGER),
                autoload=True, extend_existing=True)

        orm.mapper(Location, self.location_table,
                properties={"_time": self.location_table.c.time})

        orm.mapper(Network, self.network_table,
                properties={"_lasttime": self.network_table.c.lasttime,
                    "_capabilities": self.network_table.c.capabilities})
