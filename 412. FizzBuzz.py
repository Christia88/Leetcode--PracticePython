class Solution(object):
    def fizzBuzz(self, n):
        a=[]
        for i in range(1,n+1):
            if i%15==0:
                a.append("FizzBuzz")
            elif i%3==0:
                a.append("Fizz")
            elif i%5==0:
                a.append("Buzz")
            else:
                g=str(i)
                a.append(g)

        return a
