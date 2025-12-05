from typing import List

class HaridwarKnowledge:
    def __init__(self) -> None:
        # Minimal curated facts; keep concise and verifiable.
        self.notes = {
            "ganga aarti": (
                "Ganga Aarti at Har Ki Pauri happens daily around sunset (~6–7:30 pm depending on season). "
                "Arrive 45–60 min early for a good spot. Keep footwear outside ghats; be mindful of crowds."
            ),
            "har ki pauri": (
                "Har Ki Pauri is the main ghat. Best times: early morning or around Aarti. "
                "Avoid peak Kumbh/Magh Mela crowds if you prefer quieter visits."
            ),
            "mansa devi": (
                "Mansa Devi Temple sits on Bilwa Parvat. Ropeway available near Upper Road; "
                "combo tickets often cover Chandi Devi. Peak hours: late morning to evening."
            ),
            "chandi devi": (
                "Chandi Devi Temple is on Neel Parvat with a ropeway from Chandighat. "
                "Great to pair with Mansa Devi same day using combo ropeway tickets."
            ),
            "ropeway": (
                "Ropeways operate for Mansa Devi and Chandi Devi. Queues build after 10 am. "
                "Carry water; photography rules vary. Check on-site for maintenance schedules."
            ),
            "how to reach": (
                "Nearest airport: Dehradun (DED, Jolly Grant) ~35 km. "
                "Rail: Haridwar Jn well connected to Delhi/Varanasi/Dehradun. "
                "Road: NH7 from Delhi via Meerut–Muzaffarnagar–Roorkee."
            ),
            "best time": (
                "Oct–Mar: pleasant and clearer views; Apr–Jun: warm; Jul–Sep: monsoon (be cautious near ghats). "
                "Festivals increase crowds; book stays in advance."
            ),
            "rishikesh": (
                "Nearby Rishikesh (20–25 km): Laxman Jhula/Ram Jhula, cafes, yoga, rafting (seasonal, usually Sep–Jun). "
                "Neelkanth Mahadev is a popular side trip from Rishikesh."
            ),
            "rajaji": (
                "Rajaji National Park safaris typically run Oct–Jun (check gate schedules). "
                "Best for elephants, deer, and birding. Early morning slots are popular."
            ),
            "food": (
                "Predominantly vegetarian. Try kachori-jalebi near Upper Road, chaat at local markets, "
                "and ashram thalis. Many eateries close early (~10 pm)."
            ),
            "local transport": (
                "Auto-rickshaws, e-rickshaws, and shared Vikrams are common. "
                "For Rishikesh/airport, hire taxis or use buses from the main stand."
            ),
        }

    def search(self, query: str) -> str:
        """Return short context to ground the model."""
        q = query.lower()
        hits: List[str] = []
        for key, val in self.notes.items():
            if any(k in q for k in key.split()):
                hits.append(f"- {val}")
        # Provide some generic context if nothing matched
        if not hits:
            hits = [
                "- Focus on Har Ki Pauri, Mansa Devi, Chandi Devi, and nearby Rishikesh.",
                "- Ganga Aarti around sunset; arrive early; follow temple etiquette.",
                "- Use e-rickshaws/taxis; airport is DED (Jolly Grant).",
            ]
        return "\n".join(hits)

    def get_info(self, query: str) -> str:
        """Very short direct fallback."""
        q = query.lower()
        for key, val in self.notes.items():
            if key in q:
                return val
        return "I can help with Haridwar itineraries, Ganga Aarti, temples, local transport, food, and nearby Rishikesh/Rajaji tips."