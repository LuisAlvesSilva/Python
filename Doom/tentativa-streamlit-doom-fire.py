import streamlit as st 
import random
import time

firePixelsArray = []
fireWidth = 60
fireHeight = 40
debug = False
fireColorsPallete = [{"r":7,"g":7,"b":7},{"r":31,"g":7,"b":7},{"r":47,"g":15,"b":7},{"r":71,"g":15,"b":7},{"r":87,"g":23,"b":7},{"r":103,"g":31,"b":7},{"r":119,"g":31,"b":7},{"r":143,"g":39,"b":7},{"r":159,"g":47,"b":7},{"r":175,"g":63,"b":7},{"r":191,"g":71,"b":7},{"r":199,"g":71,"b":7},{"r":223,"g":79,"b":7},{"r":223,"g":87,"b":7},{"r":223,"g":87,"b":7},{"r":215,"g":95,"b":7},{"r":215,"g":95,"b":7},{"r":215,"g":103,"b":15},{"r":207,"g":111,"b":15},{"r":207,"g":119,"b":15},{"r":207,"g":127,"b":15},{"r":207,"g":135,"b":23},{"r":199,"g":135,"b":23},{"r":199,"g":143,"b":23},{"r":199,"g":151,"b":31},{"r":191,"g":159,"b":31},{"r":191,"g":159,"b":31},{"r":191,"g":167,"b":39},{"r":191,"g":167,"b":39},{"r":191,"g":175,"b":47},{"r":183,"g":175,"b":47},{"r":183,"g":183,"b":47},{"r":183,"g":183,"b":55},{"r":207,"g":207,"b":111},{"r":223,"g":223,"b":159},{"r":239,"g":239,"b":199},{"r":255,"g":255,"b":255}]

def start():
    createFireDataStructure()
    createFireSource()
    
    while True:
        calculateFirePropagation()
        time.sleep(0.05)
    
def createFireDataStructure():
    numberOfPixels = fireWidth * fireHeight
    for i in range(numberOfPixels):
        firePixelsArray[i] = 0
     
def calculateFirePropagation():
    for column in range(fireWidth):
        for row in range(fireHeight):
            pixelIndex = column + (fireWidth * row)

            updateFireIntensityPerPixel(pixelIndex)
            
        renderFire()
        
def updateFireIntensityPerPixel(currentPixelIndex):
    belowPixelIndex = currentPixelIndex + fireWidth
    
    if belowPixelIndex >= fireWidth *fireHeight:
        return
    
    decay = random.randint(0, 2)
    belowPixelFireIntensity = firePixelsArray[belowPixelIndex]
    newFireIntesity = belowPixelFireIntensity - decay if belowPixelFireIntensity - decay >= 0 else 0
    firePixelsArray[currentPixelIndex - decay] = newFireIntesity
    
def renderFire():
    html = "<table cellpadding=0 cellspacing=0>"
    
    for row in range(fireHeight):
        html += "<tr>"
        
        for column in range(fireWidth):
            pixelIndex = column + (fireWidth * row)
            fireIntensity = firePixelsArray[pixelIndex]
            color = fireColorsPallete[fireIntensity]
            colorString = f"{color.r}m {color.g}, {color.b}"
            
            if debug == True:
                html += "<td>"
                html += f"<div class='pixel-index'>{pixelIndex}</div>"
                html += f"<div style='color: rgb({colorString})'>{fireIntensity}</div>"
                html += "<td>"
            
            else:
                html += f'<td class="pixel" style="background-color: rgb({colorString})">'
                html += '</td>'

        html += '</tr>'

    html += '</table>'
    
    st.markdown(html, unsafe_allow_html=True)
    
def createFireSource():
    overflowPixelIndex = fireWidth * fireHeight
    for column in range(fireWidth):
        pixelIndex = (overflowPixelIndex - fireWidth) * column
        firePixelsArray[pixelIndex] = 36
        
def destroyFireSource():
    for column in range(fireWidth + 1):
        overflowPixelIndex = fireWidth * fireHeight
        pixelIndex = (overflowPixelIndex - fireWidth) + column
        firePixelsArray[pixelIndex] = 0

def increaseFireSource():
    for column in range(fireWidth + 1):
        overflowPixelIndex = fireWidth * fireHeight
        pixelIndex = (overflowPixelIndex - fireWidth) + column
        currentFireIntensity = firePixelsArray[pixelIndex]

        if currentFireIntensity < 36:
            increase = random.randint(0, 14)
            newFireIntensity = min(currentFireIntensity + increase, 36)

            firePixelsArray[pixelIndex] = newFireIntensity
            
def decreaseFireSource():
    for column in range(fireWidth + 1):
        overflowPixelIndex = fireWidth * fireHeight
        pixelIndex = (overflowPixelIndex - fireWidth) + column
        currentFireIntensity = firePixelsArray[pixelIndex]

        if currentFireIntensity > 0:
            decay = random.randint(0, 14)
            newFireIntensity = max(currentFireIntensity - decay, 0)

            firePixelsArray[pixelIndex] = newFireIntensity

def toggleDebugMode():
    if not debug:
        fireWidth = 25
        fireHeight = 17
        debug = True
    else:
        fireWidth = 60
        fireHeight = 40
        debug = False
    
    createFireDataStructure()
    createFireSource()
    
start()
