"""
Simple unit test
"""
import logging

def test_basic_math():
    """Test basic mathematical operations."""
    logging.info("Testing basic math operations")
    
    assert 2 + 2 == 4
    assert 10 - 5 == 5
    assert 3 * 4 == 12
    assert 15 / 3 == 5
    
    logging.info("Basic math tests passed")

