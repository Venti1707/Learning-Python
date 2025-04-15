# The precedence order is described in below, starting with the highest precedence at the top
# If two operators have the same precedence, the expression is evaluated from left to right

# 1) () - Parentheses
# 2) ** - Exponentiation
# 3) +x, -x, ~xm - Unary plus, unary minus, and bitwise NOT
# 4) *, /, //, % - Multiplication, division, floor division, and modulus
# 5) +, - - Addition and subtraction
# 6) <<, >> - Bitwise left and right shifts
# 7) & - Bitwise AND
# 8) ^ - Bitwise XOR
# 9) | - Bitwise OR
# 10) ==, !=, >, >=, <, <=, is, is not, in, not in - Comparisons, identity, and membership operators
# 11) not - Logical NOT
# 12) and - AND
# 13) or - OR