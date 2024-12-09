class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for row in range(1,numRows+1):
            ans.append(self.generate_row(row))
        return ans
    @staticmethod
    def generate_row(row):
        ans=1
        ansRow=[1]
        for col in range(1,row):
            ans*=(row-col)
            ans//=col
            ansRow.append(ans)
        return ansRow
