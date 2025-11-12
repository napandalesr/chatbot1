from rasa_sdk import Action
from rasa_sdk.interfaces import Tracker
from typing import Any, Text, Dict, List
import random

class ActionUtterSaludar(Action):
  def name(self) -> Text:
    return "action_utter_saludar"

  async def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    # Obtener el nombre del metadata del mensaje actual
    user_name = None
    latest_message = tracker.latest_message
    
    if latest_message and 'metadata' in latest_message:
      user_name = latest_message['metadata'].get('user_name')
    
    # Lista de respuestas posibles
    respuestas = [
      "¡Hola! 👋 Soy Neider, Ingeniero de Sistemas y Desarrollador Full Stack. ¿En qué puedo ayudarte hoy?",
      "¡Espero te encuentres bien! 😊 Soy Neider, Desarrollador Full Stack. ¿En qué puedo asistirte?",
      "¡Hola! Me da gusto saludarte. Soy Neider, especialista en desarrollo web. ¿Qué te gustaría conocer sobre mi experiencia profesional?"
    ]
    
    # Si tenemos el nombre del usuario, agregar la respuesta personalizada a las opciones
    if user_name:
      respuesta_personalizada = f"Hola {user_name}, espero te encuentres muy bien. 😊 Me llamo Neider, soy Ingeniero de Sistemas y Desarrollador Full Stack. ¿Qué te gustaría saber sobre mi perfil profesional?"
      respuestas.append(respuesta_personalizada)
    
    # Elegir aleatoriamente una respuesta
    respuesta_elegida = random.choice(respuestas)
    
    dispatcher.utter_message(text=respuesta_elegida)
    
    return []