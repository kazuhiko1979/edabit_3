"""
Chess Pieces
Create a function that takes the name of a chess piece, its position and a target position. The function should return True if the piece can move to the target and False if it can't.

The possible inputs are "Pawn", "Knight", "Bishop", "Rook", "Queen" and "King".

Examples
can_move("Rook", "A8", "H8") ➞ True

can_move("Bishop", "A7", "G1") ➞ True

can_move("Queen", "C4", "D6") ➞ False
Notes
Do not include pawn capture moves and en passant.
Do not include castling.
Remember to include pawns' two-square move on the second rank!
Look for patterns in the movement of the pieces."""

def can_move(piece, current, target):
  
  def convert_alpha2number(position):
    if len(position) == 2:
      column, row = position[0], position[1]
      if column in "ABCDEFGH" and row in "12345678":
        column = ord(column) - ord('A') + 1
        return column, int(row)
    raise ValueError("Invalid position: must be within 'A1' to 'H8'")
  

  start_col, start_row = convert_alpha2number(current)
  end_col, end_row = convert_alpha2number(target)
  col_diff = abs(end_col - start_col)
  row_diff = abs(end_row - start_row)
    
  if piece == "Pawn":
    if start_col != end_col:
      return False
    else: 
      return (end_row == start_row + 1) or (start_row == 2 and end_row == 4) or \
            (end_row == start_row - 1) or (start_row == 7 and end_row == 5)
          
  elif piece == "Knight":
    return (col_diff == 2 and row_diff) or (col_diff == 1 and row_diff == 2)
  
  elif piece == "Bishop":
    return col_diff == row_diff
  
  elif piece == "Rook":
    return start_col == end_col or start_row == end_row
  
  elif piece == "Queen":
    return col_diff == row_diff or start_col == end_col or start_row == end_row
  
  elif piece == "King":
    return col_diff <= 1 and row_diff <= 1
  
  else:
    return ValueError("Invalid piece name. Supported pieces are: 'Pawn', 'Knight', 'Bishop', 'Rook', 'Queen', 'King'")
  
  
    
print(can_move("Pawn", "A5", "A6")) # True)
print(can_move("Pawn", "G2", "G4")) # True)
print(can_move("Pawn", "C6", "D7")) # False)
print(can_move("Knight", "F5", "E3")) # True)
print(can_move("Knight", "F6", "E5")) # False)
print(can_move("Bishop", "B4", "E7")) # True)
print(can_move("Bishop", "B6", "F5")) # False)
print(can_move("Rook", "A8", "H8")) # True)
print(can_move("Rook", "A8", "H7")) # False)
print(can_move("Queen", "A8", "H1")) # True)
print(can_move("Queen", "A6", "H4")) # False)
print(can_move("King", "C4", "D5")) # True)
print(can_move("King", "B7", "B5")) # False)
  