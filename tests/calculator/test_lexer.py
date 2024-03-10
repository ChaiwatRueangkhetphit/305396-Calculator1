"""Test cases for lexical analyzer."""

# Standard library

# 3rd Party library
import pytest

# Project library
from calculator.token import Token, TokenType
from calculator.lexer import Lexer


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.NUMBER, "456"), 3),
        ("705", 1, Token(TokenType.NUMBER, "05"), 3),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
    ]
)
def test_get_number(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_number(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
    
# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("!", 0, Token(TokenType.FAC_OP, "!"), 1),
        ("5!", 1, Token(TokenType.FAC_OP, "!"), 2),
    ]
)
def test_get_fac_op(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_fac_op(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    

# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("*", 0, Token(TokenType.MUL_OP, "*"), 1),
        ("/", 0, Token(TokenType.MUL_OP, "/"), 1),
        ("%", 0, Token(TokenType.MUL_OP, "%"), 1),
        ("5*5", 0, Token(TokenType.ERROR, ""), 0),
        ("5*5", 1, Token(TokenType.MUL_OP, "*"), 2),
        ("0/2", 1, Token(TokenType.MUL_OP, "/"), 2),
        ("6%2", 1, Token(TokenType.MUL_OP, "%"), 2),
        ("*/", 0, Token(TokenType.MUL_OP, "*"), 1),
    ]
)
def test_get_mul_op(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_mul_op(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
    
# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("^", 0, Token(TokenType.POWER_OP, "^"), 1),
        ("5^5", 0, Token(TokenType.ERROR, ""), 0),
        ("2^5", 1, Token(TokenType.POWER_OP, "^"), 2),
        ("10^2", 2, Token(TokenType.POWER_OP, "^"), 3),
        ("1^2", 1, Token(TokenType.POWER_OP, "^"), 2),
        ("^465", 0, Token(TokenType.POWER_OP, "^"), 1),
    ]
)
def test_get_pow_op(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_pow_op(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    

# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("+", 0, Token(TokenType.ADD_OP, "+"), 1),
        ("+-", 1, Token(TokenType.ADD_OP, "-"), 2),
    ]
)
def test_get_add_op(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_add_op(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
    
# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("(456)", 0, Token(TokenType.LEFT_PAREN, "("), 1),
        ("()", 0, Token(TokenType.LEFT_PAREN, "("), 1),
        ("()", 1, Token(TokenType.ERROR, ""), 1),
        ("123*(456)", 0, Token(TokenType.ERROR, ""), 0),
        ("123*(456)", 4, Token(TokenType.LEFT_PAREN, "("), 5),
        ("123*(456)", 8, Token(TokenType.ERROR, ""), 8),
    ]
)
def test_get_left_paren(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_left_paren(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
    
# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("123", 0, Token(TokenType.ERROR, ""), 0),
        ("5821612", 5, Token(TokenType.ERROR, ""), 5),
        (")", 0, Token(TokenType.RIGHT_PAREN, ")"), 1),
        ("()", 1, Token(TokenType.RIGHT_PAREN, ")"), 2),
        ("()", 0, Token(TokenType.ERROR, ""), 0),
        ("(45648)(7213)", 6, Token(TokenType.RIGHT_PAREN, ")"), 7),
        ("(458)+(723)", 5, Token(TokenType.ERROR, ""), 5),
        ("458^2", 3, Token(TokenType.ERROR, ""), 3),
    ]
)
def test_get_right_paren(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_right_paren(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos