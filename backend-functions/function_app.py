import azure.functions as func
import os
import logging
from openai import AzureOpenAI

app = func.FunctionApp()

@app.function_name(name="chat")
@app.route(route="chat", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("📩 Procesando petición /chat")

    try:
        body = req.get_json()
        user_message = body.get("message", "")

        if not user_message:
            return func.HttpResponse(
                "Falta el campo 'message' en el body.",
                status_code=400
            )

        endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
        api_key = os.environ.get("AZURE_OPENAI_API_KEY")
        deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")

        # client = OpenAI(
        #     base_url=f"{endpoint}/openai/v1/",
        #     api_key=api_key
        # )
        client = AzureOpenAI(
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            api_version="2024-08-01-preview"
        )

        completion = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": user_message}]
        )

        return func.HttpResponse(
            completion.choices[0].message["content"],
            status_code=200
        )

    except Exception as e:
        logging.error(f"❌ Error: {e}")
        return func.HttpResponse(str(e), status_code=500)
