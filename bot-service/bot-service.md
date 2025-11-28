Este proyecto implementa un bot de conversación utilizando Python y el Bot Framework SDK para actuar como middleware entre el canal de chat (como Web Chat o Bot Emulator) y un agente de Azure AI Foundry.

## Tecnologías Clave
- Lenguaje: Python
- Servidor: Flask (simple y directo, compatible con Azure App Service)
- Bot Framework: botbuilder-core (con integración manual de Flask)
- Plataforma IA: Azure AI Foundry (a través del SDK azure-ai-agents)
- Autenticación: Azure AD/Managed Identity (para acceder a Foundry)

## Funcionalidades
- Conexión Bot Framework: Inicializa el BotFrameworkHttpAdapter para recibir mensajes del Bot Connector (POST a /api/messages).
- Despliegue: Configurado para desplegarse en Azure App Service, manejando la autenticación de forma segura a través de variables de entorno (MicrosoftAppId, MicrosoftAppPassword, AZURE_AI_FOUNDRY_...).


## Uso y Configuración
El proyecto requiere las siguientes variables de entorno para funcionar:

| Variable | Propósito |
| --- | :---: |
MicrosoftAppId	| ID de la aplicación registrada para el Bot Service.
MicrosoftAppPassword  |	Secreto del cliente para autenticación con el Bot Connector.
MicrosoftAppTenantId  |	TenantID del cliente para autenticación con el Bot Connector.
AZURE_AI_FOUNDRY_PROJECT_ENDPOINT |	Endpoint base de tu proyecto en Azure AI Foundry.
AZURE_AI_FOUNDRY_AGENT_ID |	ID del agente específico a ejecutar.
AZURE_TENANT_ID	| Identifica el inquilino o directorio de Azure AD (Entra ID) al que pertenece la aplicación. Es el ámbito de autenticación. Sin este ID, Azure no sabe en qué cuenta buscar las credenciales.
AZURE_CLIENT_ID	I  |	Identifica tu aplicación registrada en Microsoft Entra ID. Es el "nombre de usuario" o la identidad de la aplicación que está solicitando acceso. Este ID te da la capacidad de acceder a los recursos.
AZURE_CLIENT_SECRET	| La contraseña o el secreto generado para la aplicación registrada (AZURE_CLIENT_ID). Esta clave es necesaria para probar la identidad y obtener un token de acceso.

**Para ejecutar localmente, asegúrate de tener el entorno de Python configurado y usa el Bot Framework Emulator.**

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Configura las variables de entorno en un archivo `.env` o en tu sistema.

## Ejecutar servidor local

Simplemente ejecuta:
```bash
flask run
```

3. Abre el Emulator Bot Framework y configura el endpoint a `http://localhost:5000/api/messages`.


> **Nota**: En Local no es necesario que añadas las configuraciones del BOT Service, puedes dejar los campos MicrosoftAppTenantId, MicrosoftAppId y MicrosoftAppPassword vacíos.