from multiprocessing import Pool
def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f,[1,2,3,4,5]) #map means the process of dividing inputs/work equally  into the multiple cores
    for n in result:
        print(n)

#reduce means collecting all the results from different cores
