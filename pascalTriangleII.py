class sol:
    def pascalTriangleII(self,numRows):
        row=[1]
        for i in range(numRows):
            row=[1]+[row[i]+row[i+1] for i in range(len(row)-1)]+[1]
        return row
p1=sol()
print(p1.pascalTriangleII(4))
