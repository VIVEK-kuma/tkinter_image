#Demo Filter
from tkinter import *
import cv2
import numpy as np
from PIL import Image,ImageTk
from tkinter import filedialog

root=Tk()
root.geometry("610x650")

#root.filename=filedialog.askdirectory()


def action(color,alpha,beta):

    image1=cv2.imread('lena.png')
    image1=cv2.resize(image1,(600,500))
    if(alpha==0 and beta==0):
        image1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
        saved_image=image1.copy()
        image1=ImageTk.PhotoImage(Image.fromarray(image1))
    else:
        image1=image1[:,:,::-1]
        saved_image=image1.copy()
        image1=desireImage(image1,color,alpha,beta)
    
    Button(root,text="Save",bg="blue",font='Helvetica 18 bold', padx=40 ,pady=20 ,command=lambda:save_image(saved_image,color,alpha,beta)).grid(row=2,column=0,columnspan=3)
    image_label=Label(root,image=image1)
    image_label.image1=image1
    image_label.grid(row=0,columnspan=9)
    #print(photo)
    #cv2.imshow("New Windows",photo)
    #photo=photo[:,:,::-1]
    #photo=cv2.resize(photo,(300,300))
    #photo=cv2.addWeighted(photo,alpha,cv2.zeros(photo.shape,photo.dtype),beta,0)
    #img=ImageTk.PhotoImage(image=Image.fromarray(photo))
    """
    image_label=Label(root,image=photo)
    k=np.asanyarray(photo)
    print(k)
    image_label.photo=photo
    image_label.grid(row=0,column=1)
    """
    #canvas=Canvas(root,width=300,height=300)
    #canvas.grid(row=0,column=1)
    #canvas.create_image(20,20, anchor="nw", image=img)
    """
    img=photo
    img=cv2.imread("lena.png")
    image_label=Label(root,image=img)
    image_label.img=img
    print(image_label)
    image_label.grid(row=0)
    #cv2.destroyAllWindows()
    #img=cv2.imread('lena.png')
    #@cv2.imshow('New Windows',img)
    #print(type(photo))
    """

def save_image(img,color,alpha,beta):
    if(alpha==0 and beta==0):
        cv2.imwrite("grayImage.png",img)
    else:
        temp_img=np.zeros(img.shape,img.dtype)
        temp_img[:,:,0]=color[0]
        temp_img[:,:,1]=color[1]
        temp_img[:,:,2]=color[2]
        img=cv2.addWeighted(img,alpha,temp_img,beta,0)
        img=img[:,:,::-1]
        cv2.imwrite(str(alpha)+str(beta)+'.png',img)

def clear_image(temp):
    image_label=Label(root,image=temp)
    image_label.temp=temp
    image_label.grid(row=0,columnspan=9)


#print(my_image)
#converting opencv image to pillow image
"""
img=cv2.imread('lena.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
im_pil=Image.fromarray(img)
print("Opencv to Pil conversion",im_pil.size)
im_np=np.asarray(im_pil)
print("Opencv array is",im_np)
"""


my_image=Image.open("lena.png").convert('RGB')  
opencv_image=np.array(my_image)
new_image=opencv_image.copy()
new_image=cv2.resize(new_image,(600,500))
new_image=ImageTk.PhotoImage(Image.fromarray(new_image))
image_label=Label(root,image=new_image)
image_label.new_image=new_image
image_label.grid(row=0,columnspan=9)



temp=cv2.cvtColor(opencv_image,cv2.COLOR_BGR2GRAY)
temp=cv2.resize(temp,(50,50))
opencv_image=cv2.resize(opencv_image,(50,50))
img=opencv_image.copy()

def desireImage(img,color,alpha,beta):
    temp_img=np.zeros(img.shape,img.dtype)
    temp_img[:,:,0]=color[0]
    temp_img[:,:,1]=color[1]
    temp_img[:,:,2]=color[2]
    img=cv2.addWeighted(img,alpha,temp_img,beta,0)

    image = Image.fromarray(img, 'RGB')
    img=ImageTk.PhotoImage(image)
    return img




#print(img)
mainImage1=desireImage(img,(144, 12, 63),1,.4)
img=opencv_image.copy()
mainImage2=desireImage(img,(33, 47, 60),1,.4)
img=opencv_image.copy()
mainImage3=desireImage(img,(0,0,255),1,.4)
img=opencv_image.copy()
mainImage4=desireImage(img,(0,255,0),1,.4)
img=opencv_image.copy()
mainImage5=desireImage(img,(255, 0, 0),1,.4)
img=opencv_image.copy()
mainImage6=ImageTk.PhotoImage(Image.fromarray(temp))
img=opencv_image.copy()
mainImage7=desireImage(img,(0,0,0),1.3,.4)
img=opencv_image.copy()
mainImage8=desireImage(img,(0,0,0),.5,1)
img=opencv_image.copy()
mainImage9=desireImage(img,(31, 97, 141),1,.4)
img=opencv_image.copy()
onesImage=cv2.resize(img,(300,300))
whiteImage=desireImage(np.ones((500,600,3),img.dtype)*230,(255, 255, 255),1,.5)


#image3=cv2.addWeighted(img,.5,np.zeros(img.shape,img.dtype),.2,0)
#image4=cv2.addWeighted(img,1.3,np.zeros(img.shape,img.dtype),.4,0)

#Pil image to pyimage
#img=ImageTk.PhotoImage(mainImage1)
#print(img)
#print(mainImage1)

#img_label2=Label(image=mainImage)
Button(root,image=mainImage1,padx=40 ,pady=20 ,command=lambda:action((144, 12, 63),1,.4)).grid(row=1,column=0)
Button(root,image=mainImage2,padx=40 ,pady=20 ,command=lambda:action((33, 47, 60),1,.4)).grid(row=1,column=1)
Button(root,image=mainImage3,padx=40 ,pady=20 ,command=lambda:action((0,0,255),1,.4)).grid(row=1,column=2)
Button(root,image=mainImage4,padx=40 ,pady=20 ,command=lambda:action((0,255,0),1,.4)).grid(row=1,column=3)
Button(root,image=mainImage5,padx=40 ,pady=20 ,command=lambda:action((255, 0, 0),1,.4)).grid(row=1,column=4)
Button(root,image=mainImage6,padx=40 ,pady=20 ,command=lambda:action((0, 0, 0),0,0)).grid(row=1,column=5)
Button(root,image=mainImage7,padx=40 ,pady=20 ,command=lambda:action((0,0,0),1.3,.4)).grid(row=1,column=6)
Button(root,image=mainImage8,padx=40 ,pady=20 ,command=lambda:action((0,0,0),.5,1)).grid(row=1,column=7)
Button(root,image=mainImage9,padx=40 ,pady=20 ,command=lambda:action((31, 97, 141),1,.4)).grid(row=1,column=8)
Button(root,text="Clear", bg="green", font='Helvetica 18 bold' ,padx=40 ,pady=20 ,command=lambda:clear_image(whiteImage)).grid(row=2,column=3,columnspan=3)
Button(root,text="Exit", font='Helvetica 18 bold' ,bg="red" ,padx=40 ,pady=20 ,command=root.destroy).grid(row=2,column=6,columnspan=3)


root.mainloop()
