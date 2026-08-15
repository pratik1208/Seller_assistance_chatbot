from langchain_core.tools import tool
from rules import CATEGORY_RULES, PROHIBITION_RULES
@tool
def get_category_rules(category: str) -> dict:
    """
    Retrieve marketplace listing requirements for a product category.
    """

    rules = CATEGORY_RULES.get(category)

    if not rules:
        return {
            "found": False,
            "category": category,
            "error": "No rules found for this category"
        }

    return {
        "found": True,
        "category": category,
        **rules
    }

def get_prohibited_words(word: str) -> list:

    words = PROHIBITION_RULES.get("prohibited_keywords")
    restricted_categories = PROHIBITION_RULES.get("restricted_categories")
    protected_brands = PROHIBITION_RULES.get("protected_brands")

    if words:
        return rf"{word} is prohibited."

    elif word in restricted_categories:
        return rf"{word} is a restricted category."

    elif word in protected_brands:
        return rf"{word} is a protected brand."

    return { "found": False, "word": word, "error": "No prohibitions found for this word" } 

    
