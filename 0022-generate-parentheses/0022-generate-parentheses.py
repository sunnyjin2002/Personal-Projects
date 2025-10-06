class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        The solution solves using the following logic:
        For each round, determine if:
        # Can a new parenthesis be started?
        # Can a parenthesis be closed?
        """
        # There are n pairs of parenthesis, a total of 2n chars.
        results = [""]
        for i in range(2*n):
            intermediate_results = []
            for combi in results:
                num_l = combi.count('(')
                num_r = combi.count(')')
                # Two possible additions: '(' or ')'
                if num_l < n:
                    intermediate_results.append(combi+'(')
                if (num_l - num_r) > 0:
                    intermediate_results.append(combi+')')
            results = intermediate_results
        return results