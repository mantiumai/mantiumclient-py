"""General Client Utility Functions"""

from engine_id_values import default_ai_engines


def get_engine_id(engine_name: str) -> str:
    """Get Engine ID value from engine_id_values."""

    engine_id = next(engine for engine in default_ai_engines if engine['name'] == engine_name)
    return engine_id if engine_id else None
