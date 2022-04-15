from elasticsearch import Elasticsearch

# initialise elasticsearch client
es = Elasticsearch("http://localhost:9200")

def index_first_run():
    # create logs for etl process run 1
    extract_json_1 = {
        'process': 'extract',
        'status': 'success',
        'date': '2022-04-13',
        'processing_time': 5,
        'records': 5000,
        'run': 1
    }

    transform_json_1 = {
        'process': 'transform',
        'status': 'success',
        'date': '2022-04-13',
        'processing_time': 5,
        'records': 5000,
        'run': 1
    }

    load_json_1 = {
        'process': 'load',
        'status': 'success',
        'date': '2022-04-13',
        'processing_time': 5,
        'records': 5000,
        'run': 1
    }

    # write them to the index
    es.index(index = 'etl_monitoring', document=extract_json_1)
    es.index(index = 'etl_monitoring', document=transform_json_1)
    response = es.index(index = 'etl_monitoring', document=load_json_1)
    print(response)

def index_second_run():
    # create logs for etl process run 2
    extract_json_2 = {
        'process': 'extract',
        'status': 'success',
        'date': '2022-04-14',
        'processing_time': 10,
        'records': 10000,
        'run': 2
    }

    transform_json_2 = {
        'process': 'transform',
        'status': 'success',
        'date': '2022-04-14',
        'processing_time': 10,
        'records': 10000,
        'run': 2
    }

    load_json_2 = {
        'process': 'load',
        'status': 'success',
        'date': '2022-04-14',
        'processing_time': 10,
        'records': 9999,
        'run': 2
    }

    error_json_2 = {
        'process': 'load',
        'status': 'error',
        'date': '2022-04-14',
        'processing_time': 5,
        'records': 1,
        'run': 2,
        'msg': 'this is what happened'
    }

    # write them to the index
    es.index(index = 'etl_monitoring', document=extract_json_2)
    es.index(index = 'etl_monitoring', document=transform_json_2)
    es.index(index = 'etl_monitoring', document=load_json_2)
    response = es.index(index = 'etl_monitoring', document=error_json_2)
    print(response)

index_first_run()
index_second_run()

