import cv2
import reader

def main():
   name_list = reader.achievers_name
   #print(name_list)
   for i,n in enumerate(name_list):
      template = cv2.imread('certificate-template.jpg')
      cv2.putText(template,n,(1022,765),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,4.5,(0,0,0,0),2,cv2.LINE_AA) 
      cv2.imwrite(f'Your-path/Generated_Certificate/{n}.jpg',template) #Replace Your-path with your desired path 
      print('Processing Certificate{}/{}'.format(i+1,len(name_list)))
if __name__ == '__main__':
   main()



