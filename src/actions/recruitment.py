from rasa_sdk import Action
from .data import TECNOLOGIAS
from rasa_sdk.events import SlotSet
from rasa_sdk.interfaces import Tracker
from typing import Any, Text, Dict, List

class ActionResponderExperienciaTecnologia(Action):
  def name(self) -> Text:
    return "action_responder_experiencia_tecnologia"
  
  async def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    tecnologia = tracker.get_slot("tecnologia")

    # DEBUG
    print(f"DEBUG - Slot tecnologia: '{tecnologia}'")
    print(f"DEBUG - Entidades encontradas: {tracker.latest_message.get('entities', [])}")
    print(f"DEBUG - Keys en TECNOLOGIAS: {list(TECNOLOGIAS.keys())}")
    print(f"DEBUG - ¿Está en TECNOLOGIAS?: {tecnologia.lower() in TECNOLOGIAS}")
    
    if not tecnologia:
      response = "¿Sobre qué tecnología te gustaría conocer mi experiencia? Tengo experiencia en Javascript/Typescript, React/Next, Node/Nestjs, Docker, SGBD, entre otras."
    elif tecnologia.lower() in TECNOLOGIAS:
      tech_data = TECNOLOGIAS[tecnologia.lower()]
      response = f"**Sobre mi experiencia en {tecnologia.title()}:**\n\n" \
                f"• Experiencia: {tech_data['experiencia']}\n" \
                f"• Proyectos: {tech_data['proyectos']}" 
    else:
      tecnologias_sugeridas  = ["Node.js", "JavaScript", "React", "Docker"]
      response = f"¿{tecnologia}? Tengo experiencia en tecnologías relacionadas como {', '.join(tecnologias_sugeridas)}. ¿En cuál de estas te interesa que profundice?"
    dispatcher.utter_message(text=response)
    return [SlotSet("tecnologia", tecnologia)]

class ActionResponderHabilidadTecnologia(Action):
  def name(self) -> Text:
    return "action_responder_habilidad_tecnologia"

  async def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    tecnologia = tracker.get_slot("tecnologia")

    if not tecnologia:
      response = "¿De qué tecnología te gustaría conocer mi habilidades? Tengo conocimientos en Javascript/Typescript, React/Next, Node/Nestjs, Docker, SGBD, entre otras"
    elif tecnologia.lower() in TECNOLOGIAS:
      tech_data = TECNOLOGIAS[tecnologia.lower()]
      response = f"**Sobre mi conocimiento en {tecnologia.title()}:**\n\n" \
                f"• Nivel: {tech_data['nivel']}\n" \
                f"• Detalles técnicos: {tech_data['detalles']}"
    else:
      tecnologias_sugeridas = ["Node.js", "JavaScript", "React", "Docker"]
      response = f"¿{tecnologia}? Tengo conocimientos en tecnologías relacionadas como {', '.join(tecnologias_sugeridas)}. ¿En cuál de estas te interesa que profundice?"
    dispatcher.utter_message(text=response)
    return [SlotSet("tecnologia", tecnologia)]
