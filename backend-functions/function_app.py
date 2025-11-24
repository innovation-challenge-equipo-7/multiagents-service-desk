import azure.functions as func
import os
import json
import logging
import requests

app = func.FunctionApp()  

@app.route(route="proxyFunction", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def proxy_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Proxy Function received a request.")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    user_message = req_body.get("message")
    if not user_message:
        return func.HttpResponse("No message provided", status_code=400)

    # Formato que espera Prompt Flow
    payload = {"input": user_message}

    try:
        response = requests.post(
            os.environ["PROMPT_FLOW_URL"],
            headers={
                "Content-Type": "application/json",
                "api-key": os.environ["AZURE_OPENAI_KEY"]
            },
            data=json.dumps(payload)
        )
        response.raise_for_status()
        return func.HttpResponse(
            response.text,
            status_code=response.status_code,
            mimetype="application/json"
        )
    except requests.exceptions.RequestException as e:
        logging.error(str(e))
        return func.HttpResponse(f"Error contacting Prompt Flow: {str(e)}", status_code=500)


@app.route(route="proxyFunction", auth_level=func.AuthLevel.ANONYMOUS)
def proxyFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )