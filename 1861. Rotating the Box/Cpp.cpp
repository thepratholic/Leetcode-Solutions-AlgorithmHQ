Contributed by : Sundaram Agnihotri (student)
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 
1. Simulate Gravity
  a  : Iterate through each row of the matrix from right to left.
   b : Use a pointer (empty) to track the rightmost position where a stone (#) can fall.
  c : If an obstacle (*) is encountered, update the empty pointer to the left of the obstacle.
  d : Move stones (#) to the empty position and mark their original spot as empty (.).
  
2. Rotate the Matrix 90° Clockwise

#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int r = box.size(), c = box[0].size();
        vector<vector<char>> finalBox(c, vector<char>(r));

        // Adjust the box with gravity
        for (int i = 0; i < r; i++) {
            int empty = c - 1;
            for (int j = c - 1; j >= 0; --j) {
                if (box[i][j] == '*') {
                    empty = j - 1;
                } else if (box[i][j] == '#') {
                    box[i][j] = '.';
                    box[i][empty--] = '#';
                }
            }
        }

        // Rotate the box 90 degrees clockwise
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                finalBox[j][r - i - 1] = box[i][j];
            }
        }

        return finalBox;
    }
};

