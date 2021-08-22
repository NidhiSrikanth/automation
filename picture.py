import cv2
import time
import random
import dropbox

current_time= time.time()

def snapshot():
    number= random.randint(0,100)
    picture= cv2.VideoCapture(0)
    result= True

    while(result):
       
        ret,frame= picture.read()
        image_name= "picture"+ str(number)+ ".png"
        cv2.imwrite(image_name,frame)
        result= False
    
    picture.release()
    cv2.destroyAllWindows()
    return image_name
    print("snapshot taken")

def uploadfile(image_name):
    access_token= "LFspWM4mOCUAAAAAAAAAAQQYoqtSS_yjgt3jFDCKqvMxxTddWc59_SN2igt4H8Sy"
    source= image_name
    destination= "/test/"+image_name
    dbx= dropbox.Dropbox(access_token)
    file=open(source,"rb")
    dbx.files_upload(file.read(),destination,mode=dropbox.files.WriteMode.overwrite)
    print("file uploaded")

def main():
    while(True):
        if((time.time()- current_time)>= 5):
            name= snapshot()
            uploadfile(name)

main()