import azure.functions as func
import logging
import os
from azure.iot.hub import IoTHubRegistryManager

CONNECTION_STRING = os.environ["DEVICE_CONNECTION_STRING"]
DEVICE_ID = os.environ["DEVICE_ID"]


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger_pi")
def http_trigger_pi(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    count = req.params.get('count')
    if not count:
        return func.HttpResponse("Please pass aa 'count' parameter.", status_code=400)

<<<<<<< HEAD
    try:
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        message = str(count)
        registry_manager.send_c2d_message(DEVICE_ID, message)

        return func.HttpResponse(f"Sent blink command: {count}")
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
=======
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
>>>>>>> parent of bb0af0a (Update function_app.py)
