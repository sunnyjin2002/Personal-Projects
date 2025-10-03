class Solution:
    combinations = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
                    '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
                    '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
    def letterCombinations(self, digits: str) -> List[str]:
        result = [''] #initial value so loop 2 will run b/c size != 0.
        #For each digit, append possible_chars to the end.
        for i in range(len(digits)):
            # Possible append candidates for this digit
            possible_chars = self.combinations[digits[i]]
            new_result = [] #Store new results of this iteration.

            # For each of the intermediate strings in result, add possible_chars after them.
            for j in range(len(result)):
                current_combi = result[j] # the j-th combination in result.
                # Add all possible_chars to the end of result[j]
                for k in range(len(possible_chars)):
                    new_result.append(current_combi + possible_chars[k])
            result = new_result #Overwrite intermediate result, for next round or for output.
        
        #The empty string input "" has to result in [] not [""].
        if result == ['']:
            result = []
        return result