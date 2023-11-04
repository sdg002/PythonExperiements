
# About this project
Simple snippets of Python for ever day use
        
# PlotCustomFunction
This example demonstrates how to plot the results of a custom univariate function.  Example:
- Consider a function f(x)
- For values of x ranging from x=0 to x=100
- Plot the results of f(x) using Matplot lib
---

# AddNoiseToParabola
This example shows how to generate Gaussian noise for a parabola

<img src="./SimpleSnippets/images/AddNoiseToParabola2.png"  width="50%" height="50%"/>

# AddNoiseToStraightline
## Approach 1
This example demonstrates how to generate a noisy straight line by adding Gaussian noise (np.random.normal) to the results of the equation y=mx+c
<img src="./SimpleSnippets/images/AddNoiseToStraightLine.png"  width="50%" height="50%"/>
            
## Approach 2
This example we generate a point which lies on the line and then generated normally distributed random points around this point.

_How is this approach different from Approach 1?_

At every true point, we are radially generating a cluster of normally distributed random points
<img src="./SimpleSnippets/images/AddNoiseToStraightLine2.png"  width="50%" height="50%"/>

# AddNoiseToCircle

<img src="./SimpleSnippets/images/Noisy_Circle.png"  width="50%" height="50%"/>



---

# SaltAndPepperNoise
Demonstrates how to generate Salt and Pepper noise using scikit-image module

## salt_vs_pepper=0.2
<img src="SimpleSnippets/images/SaltPepper.2.png"  width="50%" height="50%"/>

## salt_vs_pepper=0.5
<img src="SimpleSnippets/images/SaltPepper.5.png"  width="50%" height="50%"/>

## salt_vs_pepper=0.8
<img src="./SimpleSnippets/images/SaltPepper.8.png" width="50%" height="50%" />

---
# SpeckleNoise
Demonstrates how to generate Speckle noise using scikit-image module

## variance=0.001
<img src="SimpleSnippets/images/Speckle0.001.png"  width="50%" height="50%"/>

## variance=0.002
<img src="SimpleSnippets/images/Speckle0.002.png"  width="50%" height="50%"/>

## variance=0.004
<img src="SimpleSnippets/images/Speckle0.004.png"  width="50%" height="50%"/>

## variance=0.006
<img src="SimpleSnippets/images/Speckle0.006.png"  width="50%" height="50%"/>

## variance=0.008
<img src="SimpleSnippets/images/Speckle0.008.png"  width="50%" height="50%"/>

---

# NumpyBlankImage
- Demonstrates how to generate a blank image using a Numpy 
- Setting one color for all the pixels
- Saving the image to disk

## Monochrome image - Numpy array has 1 channel

<img src="SimpleSnippets/images/Numpy.BlankImage.200.png"  width="50%" height="50%"/>

## Color image - Numpy array has 3 channels

<img src="SimpleSnippets/images/Numpy.ColorImage.255.255.0.png"  width="50%" height="50%"/>

---
