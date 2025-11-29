import azure.functions as func
import os
import logging
import json
from openai import OpenAI

app = func.FunctionApp()

def cors_response(body, status=200):
    """Helper function to return HTTP response with CORS headers"""
    return func.HttpResponse(
        body,
        status_code=status,
        mimetype="application/json",
        headers={
            "Access-Control-Allow-Origin": "*",  # Permite cualquier origen
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        },
    )

@app.function_name(name="chat")
@app.route(route="chat", methods=["POST", "OPTIONS"], auth_level=func.AuthLevel.FUNCTION)
def chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("📩 Procesando petición /chat")

    # Maneja preflight CORS
    if req.method == "OPTIONS":
        return func.HttpResponse(
            status_code=204,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
        )

    try:
        body = req.get_json()
        user_message = body.get("message", "")

        if not user_message:
            return cors_response(json.dumps({"error": "Falta el campo 'message' en el body."}), status=400)

        endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
        api_key = os.environ.get("AZURE_OPENAI_API_KEY")
        deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")

        client = OpenAI(
            base_url=f"{endpoint}/openai/v1/",
            api_key=api_key
        )

        completion = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": user_message}]
        )

        return cors_response(json.dumps({"reply": completion.choices[0].message["content"]}), status=200)

    except Exception as e:
        logging.error(f"❌ Error: {e}")
        return cors_response(json.dumps({"error": str(e)}), status=500)
