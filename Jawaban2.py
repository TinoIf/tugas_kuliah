class Jawaban2 :
    def __init__(self, n : int) -> None:
        self.n = n

    def cetakPola(self) -> None:
        angka = 1
        angka2 =1
        for i in range(1, self.n + 1):
            for j in range(1,self.n + 1):
                if (i == 1):
                    print(angka, end =" ")
                    angka+=1 
                elif(i == self.n):
                    print(angka2, end =" ") 
                    angka2+=1
                elif (j == 1):
                    print("@", end =" ")  
                elif (j == self.n):
                    print("$",end =" ")
                else:
                    print(" ",end = " ")
            print()