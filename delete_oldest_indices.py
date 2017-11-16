from elasticsearch import Elasticsearch
from datetime import datetime

import settings

if __name__ == "__main__":
    es = Elasticsearch([settings.es_host])
    today = datetime.today()

    for index in es.indices.get(settings.index_name + '*'):
        str_index_date = index.replace(settings.index_name, "")
        dateOfIndex = datetime.strptime(str_index_date, "%Y.%m.%d")
        dateDiff = (today - dateOfIndex).days
        if dateDiff > settings.keep_last_n_days:
            print("DELETE ", index + " is ", (dateDiff), " days old")
            es.indices.delete(index=index, ignore=[400, 404])
        else:
            print("KEEP   ", index + " is ", (dateDiff), " days old")