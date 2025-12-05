import os
from typing import Optional
import anthropic

HARIDWAR_SYSTEM = """You are a concise, friendly local travel assistant for Haridwar and nearby places in Uttarakhand (e.g., Rishikesh, Rajaji National Park, Neelkanth, Devprayag).
- Focus on itineraries, temple timings/etiquette, Ganga Aarti at Har Ki Pauri, local transport, food, seasons, safety, and realistic travel times.
- Prefer short, structured answers with bullet points and day-wise itineraries when asked.
- If a question is off-topic, gently steer back to Haridwar travel.
- Do not mention internal systems, providers, or APIs.
"""

class ClaudeClient:
    def __init__(self) -> None:
        api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY (or CLAUDE_API_KEY) not set")
        self.client = anthropic.Anthropic(api_key=api_key)

    def send_message(self, user_message: str, context: Optional[str] = None) -> Optional[str]:
        try:
            system = HARIDWAR_SYSTEM
            if context:
                system = f"{HARIDWAR_SYSTEM}\nUse this local context if relevant:\n{context}\n"

            resp = self.client.messages.create(
                model="claude-3-5-sonnet-latest",
                max_tokens=800,
                temperature=0.3,
                system=system,
                messages=[{"role": "user", "content": user_message}],
            )
            if resp and resp.content and len(resp.content) > 0:
                # anthropic SDK returns content blocks with .text
                return getattr(resp.content[0], "text", None) or str(resp.content[0])
            return None
        except Exception:
            return None
