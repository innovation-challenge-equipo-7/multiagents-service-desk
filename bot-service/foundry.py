import os
import asyncio
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount, Activity, ActivityTypes
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient

from dotenv import load_dotenv
load_dotenv()  

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Se obtienen de tu proyecto y agente en Azure AI Foundry
PROJECT_ENDPOINT = os.environ.get("AZURE_AI_FOUNDRY_PROJECT_ENDPOINT")
AGENT_ID = os.environ.get("AZURE_AI_FOUNDRY_AGENT_ID")

class FoundryAgentBot(ActivityHandler):
    """
    Bot que interactúa con un agente creado en Azure AI Foundry.
    Utiliza el Thread ID para mantener el historial de conversación.
    """
    def __init__(self):
        self.credential = DefaultAzureCredential()
        self.agent_client = AgentsClient(endpoint=PROJECT_ENDPOINT, credential=self.credential)
        
        # Diccionario para almacenar el Thread ID de Foundry por usuario/conversación
        self.user_threads = {}

    async def on_message_activity(self, turn_context: TurnContext):        
        # 1. Obtener/Crear Thread de Foundry
        conversation_id = turn_context.activity.conversation.id
        thread_id = self.user_threads.get(conversation_id)
        
        if not thread_id:
            new_thread = self.agent_client.threads.create()
            thread_id = new_thread.id
            self.user_threads[conversation_id] = thread_id
            await turn_context.send_activity(
                "¡Hola! Soy un agente de AI Foundry. ¿En qué te puedo ayudar?"
            )

        user_message = turn_context.activity.text
        await turn_context.send_activity(f"Enviando contenido a Foundry... '{user_message}'")

        try:
            self.agent_client.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_message
            )
        except AttributeError as e:
            raise Exception(f"Error al crear mensaje: {e}.")
            
        run = self.agent_client.runs.create(
            thread_id=thread_id,
            agent_id=AGENT_ID
        )

        while run.status not in ["completed", "failed", "cancelled", "expired"]:
            await asyncio.sleep(1) 
            
            # Obtener el estado actualizado del run usando el método 'get' del objeto 'runs'
            run = self.agent_client.runs.get(
                thread_id=thread_id,
                run_id=run.id
            )
            
        # Obtener la respuesta final del Agente
        if run.status == "completed":
            messages_result = self.agent_client.messages.list( 
                thread_id=thread_id, 
                order="desc", 
                limit=1
            )
            messages_list = list(messages_result) 
            # Obtener el contenido del mensaje
            if messages_list and messages_list[0] and messages_list[0].content:
                result_message = messages_list[0].content[0]
                result_response = result_message['text']['value']
                agent_response = result_response
            else:
                agent_response = "No se recibió respuesta del agente."
        else:
            agent_response = f"El agente no pudo completar la tarea. Estado: {run.status}. Error: {run.last_error}"

        # Responder al usuario
        await turn_context.send_activity(agent_response)

    async def on_members_added_activity(self, members_added: list[ChannelAccount], turn_context: TurnContext):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    Activity(
                        type=ActivityTypes.message, 
                        text="¡Hola! Soy un bot de AI Foundry. ¿En qué te puedo ayudar?."
                    )
                )