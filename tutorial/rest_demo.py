import requests


class EsSearchDemoRequester():
    url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
    data = '''{
  "query": {
    "bool": {
      "must": [
        {
          "text": {
            "record.document": "SOME_JOURNAL"
          }
        },
        {
          "text": {
            "record.articleTitle": "farmers"
          }
        }
      ],
      "must_not": [],
      "should": []
    }
  },
  "from": 0,
  "size": 50,
  "sort": [],
  "facets": {}
}'''


requester = EsSearchDemoRequester();
response = requests.post(requester.url, data=requester.data)
