def drawline(layer,startx,starty,endx,endy):
    fo.write("0\n")
    fo.write("LINE\n")
    fo.write("8\n")       
    fo.write(layer + "\n")       
    fo.write("10\n")
    fo.write(str(startx) + "\n")
    fo.write("20\n")
    fo.write(str(starty) + "\n")
    fo.write("11\n")
    fo.write(str(endx) + "\n")
    fo.write("21\n")
    fo.write(str(endy) + "\n")
    
def writetext(layer,text,startx,starty):
    fo.write("0\n")
    fo.write("TEXT\n")
    fo.write("7\n")
    fo.write("arial\n")
    fo.write("8\n")       
    fo.write(layer + "\n")
    fo.write("1\n")
    fo.write(text + "\n")
    fo.write("10\n")
    fo.write(str(startx) + "\n")
    fo.write("20\n")
    fo.write(str(starty) + "\n")

def drawrectangle(layer,startx,starty,width,height):
    drawline(layer,startx,starty,startx+width,starty)
    drawline(layer,startx,starty+height,startx+width,starty+height)
    drawline(layer,startx,starty,startx,starty+height)
    drawline(layer,startx+width,starty,startx+width,starty+height)
    

def main():
    
    fo.write("0\n")
    fo.write("SECTION\n")
    fo.write("2\n")
    fo.write("ENTITIES\n")
    drawline("haha",0,0,100,0)
    drawline("haha",0,50,100,50)
    drawline("haha",0,0,0,50)
    drawline("haha",100,0,100,50)
    fo.write("2\n")
    fo.write("ENTITIES\n")
    writetext("text","Anurak","10","10")
    fo.write("2\n")
    fo.write("ENTITIES\n")
    drawrectangle("rectangle",20,30,200,100)
    fo.write("2\n")
    fo.write("ENTITIES\n")
    writetext("text2","i love you",50,70)
    writetext("text3","haha",10,20)
    fo.write("0\n")
    fo.write("ENDSEC\n")



if __name__ == "__main__":
    fo = open("test2.dxf","w")
    main()
