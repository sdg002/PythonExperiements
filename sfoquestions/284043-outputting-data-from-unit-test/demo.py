import logging
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        Sum of a and b (int or float)
    """
    logging.info(f"Adding {a} and {b}")
    retval = a + b
    logging.info(f"Result of addition: {retval}")
    return retval