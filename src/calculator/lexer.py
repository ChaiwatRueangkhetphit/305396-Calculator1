"""A simple lexical analyzer."""

# Standard library

# 3rd Party library

# Project library
from calculator.token import Token,TokenType


class Lexer:
    """A simple lexical analyzer."""
    
    def get_number(self, text, pos):
        """Extract numbrt from text starting at pos.
        
        Args:
            text (str): Text to be scanned.
            pos (int): The starting position to scan.
            
        Returns:
            token:      The extracted token
            pos:        The position after the scanning
        """
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if not text[pos].isdigit():
            return Token(TokenType.ERROR, lexeme), pos
        
        while pos < length and text[pos].isdigit():
            lexeme = lexeme + text[pos]
            pos = pos + 1
            
        return Token(TokenType.NUMBER, lexeme), pos
    
    
    def get_fac_op(self, text, pos):
        """Extract an factorial operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if text[pos] == "!":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.FAC_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos
        
        
    def get_pow_op(self, text, pos):
        """Extract an power operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if text[pos] == "^":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.POWER_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos
        
        
    def get_mul_op(self, text, pos):
        """Extract an power operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if text[pos] == "*":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == "/":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == "%":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos
    
    
    def get_add_op(self, text, pos):
        """Extract an addition operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if text[pos] == "+":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.ADD_OP, lexeme), pos
        elif text[pos] == "-":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.ADD_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos
        
        
    def get_left_paren(self, text, pos):
        """Extract an power operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if text[pos] == "(":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.LEFT_PAREN, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos
        
        
    def get_right_paren(self, text, pos):
        """Extract an power operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if text[pos] == ")":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.RIGHT_PAREN, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos
        