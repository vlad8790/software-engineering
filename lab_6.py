def main(**kwargs):
   for i,j in kwargs.items():
       print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(x=[1,2,3,6,7],y=[3,3,0,7,5],z=[2,3,0,5,7])