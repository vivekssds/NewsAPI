
from connection import loadconnection
from DAL.ReadThroughcache import readthroughcache

class redisconnector:
    def redisrefreshcache(app,timetolive):
        redis_client = loadconnection.setredisconnection()
        redis_client.flushall()
        readthroughcache()
