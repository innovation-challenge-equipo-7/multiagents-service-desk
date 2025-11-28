import os
import logging
import asyncio

from flask import Flask, request, Response, jsonify
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity

from foundry import FoundryAgentBot
from dotenv import load_dotenv
load_dotenv()

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuración de Azure Bot Service ---
APP_ID = os.environ.get("MicrosoftAppId", "")
APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
APP_TENANT_ID = os.environ.get("MicrosoftAppTenantId", "")

SETTINGS = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD, APP_TENANT_ID)
ADAPTER = BotFrameworkAdapter(SETTINGS)
BOT = FoundryAgentBot()

# --- Manejo de Errores ---
async def on_error_handler(turn_context, error):
    """Maneja los errores que ocurren durante el procesamiento de mensajes."""
    # Loguea el error
    logging.error(f"Error en el bot: {error}")
    
    # 1. Manejo Específico para el Error de Autenticación Local
    if (not APP_ID or not APP_PASSWORD or not APP_TENANT_ID) and "Unauthorized" in str(error):
        logging.info("DEBUG LOCAL: Ignorando error de autenticación esperado debido a que el ID, el password o el tenant ID no están configurados.")
        return  # Finaliza el manejo del turno sin hacer nada más
    
    # 2. Manejo de Errores de Producción/Reales: Envía un mensaje de error al usuario
    try:
        # Envía un mensaje de error genérico al usuario
        await turn_context.send_activity("¡Lo siento! Algo salió mal.")
        
        # Opcional: Envía los detalles del error al usuario (solo para desarrollo)
        await turn_context.send_activity(f"Detalles Técnicos: {error}")
        
    except Exception as e:
        logging.error(f"Excepción al intentar enviar el mensaje de error: {e}")

ADAPTER.on_turn_error = on_error_handler

# --- Inicializar Flask App ---
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Para soportar caracteres especiales en las respuestas JSON

@app.route("/", methods=["GET"])
def health_check():
    """
    Endpoint de health check que devuelve el estado del servicio.
    """
    return Response("Bot Service is Running and Healthy", status=200, mimetype="text/plain")

@app.route("/api/messages", methods=["POST"])
def messages():
    """
    Endpoint principal que maneja las peticiones de mensajes de Azure Bot Service.
    Convierte la petición de Flask al formato que espera el BotFrameworkAdapter.
    """
    if "application/json" not in request.headers.get("Content-Type", ""):
        return Response("Unsupported Media Type", status=415)
    
    try:
        # Obtener el body y el header de autorización
        body = request.json
        auth_header = request.headers.get("Authorization", "")
                
        # Deserializar la actividad
        activity = Activity.deserialize(body)
        
        # Procesar la actividad de forma asíncrona
        async def process():
            await ADAPTER.process_activity(
                activity, 
                auth_header, 
                lambda context: BOT.on_turn(context)
            )
        
        # Ejecutar la función async (asyncio.run crea un nuevo event loop)
        asyncio.run(process())
        
        return Response(status=200)
        
    except Exception as e:
        logging.error(f"Error procesando la actividad: {e}")
        return Response(str(e), status=500, mimetype="text/plain")

# Al arrancar directamente, exponer las rutas registradas y usar puerto configurable
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port, debug=True)