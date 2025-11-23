"""Common types and ID generation for models."""

import random
import string
from datetime import datetime


def generate_id(prefix: str) -> str:
    """Generate a unique ID with format: {prefix}_{timestamp}_{random}.
    
    Args:
        prefix: Entity type prefix ('n' for note, 't' for task, 'c' for course)
        
    Returns:
        Unique ID string (e.g., "n_20251123_103045_a7c")
        
    Example:
        >>> id = generate_id("n")
        >>> id.startswith("n_")
        True
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    random_suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=3))
    return f"{prefix}_{timestamp}_{random_suffix}"
