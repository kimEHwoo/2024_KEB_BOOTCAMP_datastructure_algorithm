# def factorial(number) -> int:
#     '''
#     factorial by repetition
#     :param number: number (int)
#     :return: factorial result (int)
import mymath
import time

if __name__ == "__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {mymath.nCr(n, r)}")
    # f = int(input())
    # print(mymath.factorial(f))