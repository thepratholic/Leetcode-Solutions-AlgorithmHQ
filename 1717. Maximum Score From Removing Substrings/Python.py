# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


class Solution:
    def maximumGain(self, original_string: str, x: int, y: int) -> int:
        # Helper function to remove target_pair from the string and return updated string + gained score
        def remove_pair(s: str, first: str, second: str, pair_score: int) -> tuple[str, int]:
            stack = []
            total_score = 0

            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()  # Remove the matched first character
                    total_score += pair_score
                else:
                    stack.append(ch)

            # Return the remaining string and total score gained
            return ''.join(stack), total_score

        total_points = 0

        # Prioritize the pair with higher score
        if x >= y:
            # Remove "ab" first
            after_ab_removal, ab_points = remove_pair(original_string, 'a', 'b', x)
            after_ba_removal, ba_points = remove_pair(after_ab_removal, 'b', 'a', y)
        else:
            # Remove "ba" first
            after_ba_removal, ba_points = remove_pair(original_string, 'b', 'a', y)
            after_ab_removal, ab_points = remove_pair(after_ba_removal, 'a', 'b', x)

        total_points = ab_points + ba_points
        return total_points
