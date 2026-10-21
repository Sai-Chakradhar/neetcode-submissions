class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_1(s):
            string_1 = list(s)
            length = len(string_1)
            results=[]
            for i in s:
                results.append(string_1[length-1])
                length-=1
            
            return "".join(results)
        main_result = []
        l_1 = s.split(" ")
        for i in l_1:
            main_result.append(reverse_1(i))
        return " ".join(main_result)