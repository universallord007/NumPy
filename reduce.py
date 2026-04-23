import numpy as np

def ufunc_reduce(ufct, *vectors):
   vs = np.ix_(*vectors)
   r = ufct.identity
   for v in vs:
       r = ufct(r, v)
   return r

def main():
    a = np.arange(12).reshape(3, 4)
    print(a)
    print(ufunc_reduce(np.add, a[0], a[1], a[2]))
    print(ufunc_reduce(np.multiply, a[0], a[1], a[2]))



if __name__ == "__main__":
    main()