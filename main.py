import matplotlib.pyplot as mpl
import numpy as np
import dataGenerator
import algorithms

def main():
    data = np.array(dataGenerator.DataGenerator.GenerateDataSet(10, 1000))
    mpl.bar(data, [num for num in data])

    mpl.xlabel("")
    mpl.ylabel("")
    axis = mpl.gca()
    axis.set_facecolor("black")
    

    mpl.show()



if __name__ == "__main__":
    main()