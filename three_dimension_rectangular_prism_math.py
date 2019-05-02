length = float(input("Enter the length of rectangular prism "))
width = float(input("Enter the width of rectangular prism "))
height = float(input("Enter the height of rectangular prism "))
areaBottom = length * width
areaTop = length * width
areaFront = width * height
areaBack = width * height
areaLeft = length * height
areaRight = length * height
areaAll = areaBottom + areaTop + areaFront + areaBack + areaLeft + areaRight

print("The area of the 3 dimensional 6 sided rectangular prism is ", areaAll)
