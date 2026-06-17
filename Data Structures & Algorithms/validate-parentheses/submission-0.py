class Solution:
    def isValid(self, s: str) -> bool:
        parentheses={
            '}':'{',
            ']':'[',
            ')':'('
        }
        st=[]

        for c in s:
            if c in parentheses.values():
                st.append(c)
            
            else:
                if not st or st[-1] !=parentheses[c]:
                    return False
                st.pop()
        return len(st)==0
            
        