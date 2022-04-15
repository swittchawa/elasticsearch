from elasticsearch import Elasticsearch

# initialise elasticsearch client
es = Elasticsearch("http://localhost:9200")

# setting: one node
# mapping properties are not required
request_body = {
    "settings" : {
        "number_of_shards": 1,
        "number_of_replicas": 1
    },
    'mappings': {
        'properties': {
            'process': {'type': 'text'},
            'date': {'format': 'yyyy-MM-dd', 'type': 'date'},
            'processing_time': {'type': 'double'},
            'records': {'type': 'integer'},
            'msg': {'type': 'text'}
        }}
}

print("Creating 'example_index' index...")
es.indices.create(index = 'etl_monitoring', body = request_body)