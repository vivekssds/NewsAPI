from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json, redis
from flask import Flask, jsonify
from cassandra.query import ordered_dict_factory
import collections
from cassandra.cqlengine import connection

auth_provider = PlainTextAuthProvider(username='vivek_s', password='VS_MiKeyDev')
# # ,cassandra-node2.midevcld.spglobal.com,cassandra-node3.midevcld.spglobal.com,cassandra-node4.midevcld.spglobal.com,cassandra-node5.midevcld.spglobal.com,cassandra-node6.midevcld.spglobal.com'
#
cluster = Cluster(contact_points=['cassandra-node1.midevcld.spglobal.com', 'cassandra-node2.midevcld.spglobal.com',
                                  'cassandra-node3.midevcld.spglobal.com'
    ,'cassandra-node4.midevcld.spglobal.com', 'cassandra-node5.midevcld.spglobal.com',
                                  'cassandra-node6.midevcld.spglobal.com', 'cassandra-node7.midevcld.spglobal.com'],
                  port=9042, auth_provider=auth_provider)

session = cluster.connect('keyspace1')

#
# cluster=connection.setup(hosts=['cassandra-node1.midevcld.spglobal.com','cassandra-node2.midevcld.spglobal.com','cassandra-node3.midevcld.spglobal.com'
#                                ,'cassandra-node4.midevcld.spglobal.com','cassandra-node5.midevcld.spglobal.com','cassandra-node6.midevcld.spglobal.com','cassandra-node7.midevcld.spglobal.com'], default_keyspace='news',
#                  protocol_version=3)
#
# connection.set
# session = cluster.connect('news')
# rows = session.execute('select * from newsfeedaggconsumerzone_tbl;')
#
# for row in rows:
#     print(row)

# cassandra-node1.midev:9042  telnet cassandra-node1.midev 9042
# cluster = Cluster(['127.0.0.1'],port=9042)
# redis_client = redis.Redis(host="127.0.0.1", port=6379, db=0)
# j=redis_client.get("news")

# d=j.decode('UTF-8')
# print((list(d)))

# reply = json.loads(r.json().get('doc', '$')[0])

#
# session = cluster.connect('news')
# # # session.row_factory = ordered_dict_factory
# session.execute('USE news')
# print("Reading data simply..")
# rows = session.execute('select * from newsfeedaggconsumerzone_tbl;')
# print(rows)
# objects_list = []
# for row in rows:
#     d = collections.OrderedDict()
#     d["articleid"] =row[0]
#     d["headline"] = row[3]
#     d["newscategory"] = row[4]
#     d["newspublishedtime"] = row[5]
#     d["newssubcategory"] = row[6]
#     objects_list.append(d)
# j=jsonify(objects_list)
# redis_client.set("news", j)
