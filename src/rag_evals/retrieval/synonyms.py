"""Domain synonym dictionary for academic and administrative terms."""
from typing import List, Dict

_SYNONYMS: Dict[str, List[str]] = {
    "exam": ["examination", "test", "assessment"],
    "attendance": ["presence", "participation"],
    "grade": ["mark", "score", "cgpa"],
    "syllabus": ["curriculum", "course plan"],
    "professor": ["faculty", "instructor"],
}

class SynonymExpander:
    """Expands query tokens using domain vocabulary mapping."""
    def expand(self, query: str) -> List[str]:
        words = query.lower().split()
        expansions = []
        for w in words:
            if w in _SYNONYMS:
                for syn in _SYNONYMS[w]:
                    expansions.append(query.lower().replace(w, syn))
        return expansions or [query]
