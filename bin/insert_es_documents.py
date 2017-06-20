import mozdef_tools
mozdef_tools.include_mozdef()


from utilities.toUTC import toUTC
from elasticsearch_client import ElasticsearchClient

es_client = ElasticsearchClient(mozdef_tools.get_es_server())

documents = [
    {
        "category": "syslog",
        "processid": "0",
        "receivedtimestamp": '2017-06-19T23:01:50.720405+00:00',
        "severity": "7",
        "utctimestamp": '2017-06-19T23:01:50.720405+00:00',
        "timestamp": '2017-06-19T23:01:50.720405+00:00',
        "hostname": "syslog1.hostname.com",
        "mozdefhostname": "mozdef3.hostname.com",
        "summary": "input_userauth_request: invalid user mozdef\n",
        "eventsource": "systemslogs",
        "details": {
            "processid": "10794",
            "program": "sshd",
            "Random": 6,
            "hostname": "mozdefes.hostname.com"
        }
    }
]


for document in documents:
    es_client.save_object(index='events', doc_type='event', body=document)
