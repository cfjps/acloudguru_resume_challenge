import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, doc:func.DocumentList, doccount: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    counter_json = []
    for visitor in doc:
        
        newdocs = func.DocumentList() 
        counter = visitor['visitor_count']
        counter += 1
        newproduct_dict = {
            "id": visitor['id'],
            "visitor_count": counter
        }
        newdocs.append(func.Document.from_dict(newproduct_dict))
        doccount.set(newdocs)

        visit_json = {
           "id": visitor['id'], 
           "visitor_count": visitor['visitor_count']
        }
        counter_json.append(visit_json)
            

    return func.HttpResponse(
            json.dumps(counter_json),
            status_code=200,
            mimetype="application/json"            
    )
