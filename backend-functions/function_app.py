import azure.functions as func
import os
import json
import logging
import requests

app = func.FunctionApp()

# === CHAT (POST) ===
import azure.functions as func
import os
import json
import logging
import requests

app = func.FunctionApp()

# === CHAT (POST) ===
@app.route(route="chat", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def chat_proxy(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Chat proxy called.")

    # ================================
    # LEER JSON DE MANERA SEGURA
    # ================================
    try:
        req_body = req.get_json()
    except Exception as e:
        logging.error(f"JSON error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "El cuerpo de la petición debe ser JSON válido."}),
            status_code=400,
            mimetype="application/json"
        )

    # ================================
    # VALIDAR MENSAJE
    # ================================
    user_message = req_body.get("message")
    if not user_message:
        return func.HttpResponse(
            json.dumps({"error": "Falta el campo 'message'."}),
            status_code=400,
            mimetype="application/json"
        )

    logging.info(f"User message: {user_message}")

    # ================================
    # VARIABLES DE ENTORNO
    # ================================
    azure_url = os.environ.get("PROMPT_FLOW_URL")
    azure_key = os.environ.get("AZURE_OPENAI_KEY")

    logging.info(f"PROMPT_FLOW_URL={'OK' if azure_url else 'MISSING'}")
    logging.info(f"AZURE_OPENAI_KEY={'OK' if azure_key else 'MISSING'}")

    # ================================
    # MODO MOCK (cuando aún NO tienes Azure)
    # ================================
    if not azure_url or not azure_key:
        logging.warning("Modo MOCK activado — Azure no configurado.")
        return func.HttpResponse(
            json.dumps({
                "reply": f"(MOCK) Hola, recibí tu mensaje: {user_message}"
            }),
            mimetype="application/json"
        )

    # ================================
    # MODO AZURE
    # ================================
    try:
        payload = {"input": user_message}

        response = requests.post(
            azure_url,
            headers={
                "Content-Type": "application/json",
                "api-key": azure_key
            },
            data=json.dumps(payload),
            timeout=10
        )

        # Si Azure devuelve error → devolverlo claro
        if response.status_code >= 400:
            logging.error(f"Azure error: {response.text}")
            return func.HttpResponse(
                json.dumps({
                    "error": "Error al conectar con Azure.",
                    "details": response.text
                }),
                status_code=response.status_code,
                mimetype="application/json"
            )

        return func.HttpResponse(
            response.text,
            status_code=200,
            mimetype="application/json"
        )

    except requests.exceptions.Timeout:
        logging.error("Timeout al conectar con Azure.")
        return func.HttpResponse(
            json.dumps({"error": "Timeout al conectar con Azure."}),
            status_code=504,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Exception connecting to Azure: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "Error interno al conectar con Azure."}),
            status_code=502,
            mimetype="application/json"
        )


# === DASHBOARD (GET) ===
@app.route(route="dashboard/stats", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def dashboard_stats(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Dashboard stats requested.")

    sample_data = {
        "totalTickets": 25,
        "openTickets": 8,
        "closedToday": 5
    }

    return func.HttpResponse(
        json.dumps(sample_data),
        mimetype="application/json"
    )
