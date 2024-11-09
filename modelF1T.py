# Mikail Usman 
# Aestic AI
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#------- DATA CLEAN UP -------
annotations = pd.read_csv(r'C:\Users\m20mi\Documents\Work\Aestic\annotations.csv')
imgSize = (224, 224) #Desired Height and Width

if __name__ == '__main__':
    print('Testing Anaconda')
    imgURL = f"Aestic\Data\{annotations.iloc[0, 0]}" # [rol, col]
    print()
    print(imgURL)
    img = mpimg.imread(imgURL)
    imgplot = plt.imshow(img)
    plt.show()

