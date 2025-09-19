# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Spreadsheet:

    def __init__(self, rows: int):
        # Create a grid with given number of rows and 26 columns (A–Z)
        # Each cell is initialized with 0
        self.grid = [[0] * 26 for _ in range(rows)]


    def setCell(self, cell: str, value: int) -> None:
        # Convert cell label like "A1" into grid indices
        col = ord(cell[0]) - ord('A')   # 'A' → 0, 'B' → 1, ..., 'Z' → 25
        row = int(cell[1:])             # Extract row number from string (e.g. "A12" → 12)
        row -= 1                        # Convert to 0-based index

        # Set the cell's value in grid
        self.grid[row][col] = value


    def resetCell(self, cell: str) -> None:
        # Same as setCell, but reset value to 0
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        row -= 1

        self.grid[row][col] = 0
        

    def getValue(self, formula: str) -> int:
        # Formula format: starts with '=' and has terms separated by '+'
        # Example: "=A1+B2+5"
        parts = formula[1:].split("+")
        total = 0

        for part in parts:
            if part[0].isalpha():   # If part is a cell reference like "B3"
                col = ord(part[0]) - ord('A')
                row = int(part[1:])
                row -= 1
                total += self.grid[row][col]
            else:                   # If part is a plain number
                total += int(part)

        return total


# # Example usage:
# obj = Spreadsheet(5)   
# obj.setCell("A1", 10)         
# obj.setCell("B2", 20)         
# print(obj.getValue("=A1+5"))  
# print(obj.getValue("=A1+B2"))
# obj.resetCell("A1")           
# print(obj.getValue("=A1+B2"))
