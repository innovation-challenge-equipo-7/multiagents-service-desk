import azure.functions as func
import os
import json
import logging
from openai import AzureOpenAI

app = func.FunctionApp()

def cors_response(body, status=200):
    """Helper to return JSON with CORS headers"""
    return func.HttpResponse(
        body,
        status_code=status,
        mimetype="application/json",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        },
    )

@app.function_name(name="chat")
@app.route(route="chat", methods=["POST", "OPTIONS"], auth_level=func.AuthLevel.FUNCTION)
def chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("📩 Processing /chat request")

    # Handle OPTIONS (CORS preflight)
    if req.method == "OPTIONS":
        return cors_response("")

    try:
        body = req.get_json()
        user_message = body.get("message")

        if not user_message:
            return cors_response(
                json.dumps({"error": "Missing 'message' field"}),
                status=400
            )

        # Azure OpenAI Client
        client = AzureOpenAI(
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            api_version="2024-08-01-preview"
        )

        # Chat Completion
        completion = client.chat.completions.create(
            model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
            messages=[{"role": "user", "content": user_message}]
        )

        reply = completion.choices[0].message.content

        return cors_response(
            json.dumps({"reply": reply}, ensure_ascii=False),
            status=200
        )

    except Exception as e:
        logging.error(f"❌ ERROR en /chat: {e}")
        return cors_response(
            json.dumps({"error": str(e)}, ensure_ascii=False),
            status=500
        )
