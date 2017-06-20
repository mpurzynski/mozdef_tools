import mozdef_tools
mozdef_tools.include_mozdef()

import json
from elasticsearch_client import ElasticsearchClient
from query_models import SearchQuery, TermMatch

es_client = ElasticsearchClient(mozdef_tools.get_es_server())

search_query = SearchQuery(days=5)
# Add a requirement to match on a specific term
search_query.add_must(TermMatch('_type', 'event'))

search_indices = ['events', 'events-previous']

results = search_query.execute(es_client, indices=search_indices)

print "Found {0} documents in {1}".format(len(results['hits']), ', '.join(search_indices))
for result in results['hits']:
    print json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
    # Print the document excluding ES 'stuff'
    # print result['_source']
