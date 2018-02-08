from elasticsearch import Elasticsearch
from datetime import datetime

import settings


def create_generator_indices_by_pattern(elastic_search, pattern):
    for index in elastic_search.indices.get(pattern + '*'):
        yield index


def get_age_of_index(index, pattern):
    today = datetime.today()
    str_index_date = index.replace(pattern, "")
    date_of_index = datetime.strptime(str_index_date, "%Y.%m.%d")
    date_diff = (today - date_of_index).days
    return date_diff


if __name__ == "__main__":
    es = Elasticsearch([settings.es_host])
    today = datetime.today()
    for index_to_delete in settings.index_names:
        for index in create_generator_indices_by_pattern(es,  index_to_delete ):
            date_diff = get_age_of_index(index, index_to_delete)
            if date_diff > settings.keep_last_n_days:
                print("DELETE ", index + " is ", date_diff, "\tdays old")
                es.indices.delete(index=index, ignore=[400, 404])
            else:
                print("KEEP   ", index + " is ", date_diff, "\tdays old")
