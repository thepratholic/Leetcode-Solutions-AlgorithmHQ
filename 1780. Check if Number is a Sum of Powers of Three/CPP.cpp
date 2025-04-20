// Contributed by Pratham Chelaramani (Student)
// LinkedIn: https://www.linkedin.com/in/thepratholic/

class Solution
{
public:
    bool checkPowersOfThree(int n)
    {
        while (n > 0)
        {
            if (n % 3 == 2) // If any digit in base-3 is '2', return false
                return false;

            n /= 3; // Move to the next digit in base-3 representation
        }
        return true; // If all digits were 0 or 1, return true
    }
};
