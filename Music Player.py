from tkinter import * #import built-in libraries
import os,threading #import built-in libraries
import pygame, eyed3 #import 3rd party libraries
from PIL import ImageTk, Image  #import 3rd party libraries
from threading import Thread
osw = os.getcwd()
new_list = osw.split('\\')
var = new_list[0]+'/'+new_list[1]+'/'+new_list[2]+'/Music'
osd = var

print(osd)
if os.path.exists('IMG')==False:
    os.mkdir('IMG')
    
allsongtracks = []
alltracks = []
indexa = 0
lt = ''
ltt = ''

class MusicPlayer:

  def __init__(self,root):
    self.root = root
    self.root.title("Kelly Music Player")
    self.root.geometry("1080x565")
    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()
    self.stat = StringVar()
  
    trackframe = LabelFrame(self.root,text="Song Track",font=("arial",15,"bold"),bg="#8F00FF",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=800,height=100)
    songtrack = Label(trackframe,textvariable=self.track,font=("arial",24,"bold"),bg="#8F00FF",fg="#B0FC38").pack(side=LEFT,fill=BOTH)#(row=0,column=0,padx=20,pady=10)
   # trackstatus = Label(trackframe,textvariable=self.status,font=("arial",24,"bold"),bg="#8F00FF",fg="#B0FC38").grid(row=0,column=1,padx=10,pady=5)
    
    #trackImg = Label(self.root,text="Song Image",font=("arial",15,"bold"),bg="#8F00FF",fg="white",bd=5,relief=GROOVE)
    #trackImg.place(x=1,y=100,width=800,height=300)
   # Seeker = Label(self.root,text="Seek BAR",font=("arial",15,"bold"),bg="#8F00FF",fg="white",bd=5,relief=GROOVE)
    #Seeker.place(x=2,y=300,width=700,height=100)


    buttonframe = LabelFrame(self.root,text="Control Panel",font=("arial",15,"bold"),bg="#8F00FF",fg="white",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=400,width=800,height=100)
    playbtn = Button(buttonframe,text="PREV",command=self.prevsong,width=6,height=1,font=("arial",16,"bold"),fg="navyblue",bg="#B0FC38").grid(row=0,column=0,padx=10,pady=5)
    playbtn = Button(buttonframe,textvariable=self.stat,command=self.playsong,width=6,height=1,font=("arial",16,"bold"),fg="navyblue",bg="#B0FC38").grid(row=0,column=1,padx=10,pady=5)
    playbtn = Button(buttonframe,text="NEXT",command=self.nextsong,width=6,height=1,font=("arial",16,"bold"),fg="navyblue",bg="#B0FC38").grid(row=0,column=3,padx=10,pady=5)
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("arial",16,"bold"),fg="navyblue",bg="#B0FC38").grid(row=0,column=4,padx=10,pady=5)

    songsframe = LabelFrame(self.root,text="Song Playlist",font=("arial",15,"bold"),bg="#8F00FF",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=800,y=0,width=500,height=500)
    scroll_y = Scrollbar(songsframe,orient=VERTICAL)
    self.playlist = Listbox(songsframe,yscrollcommand=scroll_y.set,selectbackground="#B0FC38",selectmode=SINGLE,font=("arial",12,"bold"),bg="#CF9FFF",fg="navyblue",bd=5,relief=GROOVE)
    self.playlist.bind('<<ListboxSelect>>', self.onselect)

    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH,ipady=500)
   
    #songtracks = glob.glob ('**/*.mp3', recursive=True) 
    #print(songtracks)
    global lt
    global ltt
    #lt = len(songtracks)
    #print(len(songtracks))
    audio = []
    title = []
    
    for data in os.walk(osd):  #here to start searching
        dir_path, folders, files = data

        for f in files:
            if f.lower().endswith('.mp3'):
            #print(f)
                allsongtracks.append(os.path.join(dir_path, f))

    '''for track in songtracks:
      allsongtracks.append(track)'''
    #allsongtracks.sort()  
    ltt = int(len(allsongtracks))
    
    #print(ltt)
    lt = ltt
    for i in range(ltt):
        audio = eyed3.load(allsongtracks[i])
    
       #album = audio.tag.album
       #artist = audio.tag.artist
     
        try:
            tags = audio.tag
            title = audio.tag.title
            
            #Art = audio.tag.images
        except Exception as e:
            
          d = e
        finally:
          if title == None:
            title2 = allsongtracks[i]
            title2 = title2.split('\\')
            title2 = title2[-1]
            #title2 = title2.split('.')
            #title =  title2[-1]
            #print(title2)
            alltracks.append(title2)
            
            self.playlist.insert(END,title2)
          else:
            
            #print(title)
            alltracks.append(title)
            
            self.playlist.insert(END,title)
       
  lts = alltracks
  print(len(lts))
         
  def prevsong(self):
    global indexa
    global lt
    if indexa == 0:
      work = 'do nothing'
    else:
      indexa = indexa-1
      now = allsongtracks[indexa]
      show = alltracks[indexa]
      self.track.set(show)
      self.status.set("-Playing")
      pygame.mixer.music.load(now)
      pygame.mixer.music.play()
      self.playlist.selection_clear(0, END)
      self.playlist.select_set(indexa)
      self.stat.set("PAUSE") 
      '''img2 = Image.open('IMG/'+str(indexa)+'.jpg')
      picture = ImageTk.PhotoImage(img2)
      trackImg.configure(image=picture)
      trackImg.image = picture '''
      
  def nextsong(self):
    global indexa
    global lt
    if indexa == lt-1:
      work = 'do nothing'
    else:
      indexa = indexa+1
      now = allsongtracks[indexa]
      show = alltracks[indexa]
      self.track.set(show)
      self.status.set("-Playing")
      pygame.mixer.music.load(now)
      pygame.mixer.music.play()
      self.playlist.selection_clear(0, END)
      self.playlist.select_set(indexa)
      self.stat.set("PAUSE") 
      '''img2 = Image.open('IMG/'+str(indexa)+'.jpg')
      picture = ImageTk.PhotoImage(img2)
      trackImg.configure(image=picture)
      trackImg.image = picture '''
      
  def onselect(self,t):
    # Note here that Tkinter passes an event object to onselect
    global indexa
    w = t.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    indexa = index
    #print('You selected item %d: "%s"' % (index, value
    pygame.mixer.music.load(allsongtracks[indexa])
    pygame.mixer.music.play()
    #Music.status.set('-Playing')
    self.track.set(alltracks[indexa])
    self.stat.set("PAUSE") 
    #nexter()
    lts = alltracks
    #print(len(alltracks))
       #album = audio.tag.album
       #artist = audio.tag.artist
    
    '''img2 = Image.open('IMG/'+str(indexa)+'.jpg')
    picture = ImageTk.PhotoImage(img2)
    trackImg.configure(image=picture)
    trackImg.image = picture'''
    
  
  def playsong(self):
    if self.status.get()=='-Paused':
        self.status.set("-Playing")
        
        pygame.mixer.music.unpause()
        self.stat.set("PAUSE")  
        #print(pygame.mixer.get_busy())
    elif self.stat.get()=="PAUSE":
        self.status.set("-Paused")
        self.stat.set("PLAY")
        pygame.mixer.music.pause()
    else:
        print(self.playlist.get(ACTIVE))
        #print(allsongtracks)
        #index = allsongtracks.index(self.playlist.get(ACTIVE))
        #print(index)
        self.track.set(alltracks[indexa])
        self.status.set("-Playing")
        self.stat.set("PAUSE")
        pygame.mixer.music.load(allsongtracks[indexa])
        pygame.mixer.music.play()
            
  def stopsong(self):
    self.stat.set("PLAY")
    #pygame.mixer.music.stop()
    pygame.mixer.music.load(allsongtracks[indexa])
    pygame.mixer.music.play()
    pygame.mixer.music.pause()
     
  def pausesong(self):
    #print(pygame.mixer.get_busy())
    self.status.set("-Paused")
    pygame.mixer.music.pause()
    #print(pygame.mixer.music.get_busy())
    
def nexter():
    global indexa
    global lt
    if indexa == lt-1:
      work = 'do nothing'
    else:
      indexa = indexa+1
      now = allsongtracks[indexa]
      show = alltracks[indexa]
      Musician.track.set(show)
      Musician.status.set("-Playing")
      pygame.mixer.music.load(now)
      pygame.mixer.music.play()
      Musician.playlist.selection_clear(0, END)
      Musician.playlist.select_set(indexa)
      
def chk():
      MUSIC_ENDED = pygame.USEREVENT
      pygame.mixer.music.set_endevent(MUSIC_ENDED)
      #print('start')
      Running = True
 
      while Running:
          for event in pygame.event.get():  
             #event = pygame.event.get()
       #while running:
             if event.type == MUSIC_ENDED:
              print('music end event')
              nexter()
             else:
              c =7
            #print('not')
            #chk()        
    
def ended():
    print ('ended')
    
root = Tk()
root.configure(background='blue')
          
Musician = MusicPlayer(root)
Musician.track.set(alltracks[indexa])
Musician.stat.set('PLAY')
img2 = Image.open('music.png')
picture = ImageTk.PhotoImage(img2)
trackImg = Label(root,image=picture,bd=10)
trackImg = Label(Musician.root,image=picture,width=300,height=300,bd=10,relief=GROOVE)
trackImg.place(x=1,y=100,width=800,height=300)

thread = threading.Thread(target=chk)
thread.start()
'''
 for i in range(ltt):
        audio = eyed3.load(allsongtracks[i])
ART = audio_file.tag.images'''
'''for images in audio.tag.images:
               
               image_file = open ("IMG/"+ str(i) + ".jpg",'wb')#.format (artist, album, images.picture_type), "wb")
               #print ("Writing image file: {0} - {1} ({2}).jpg".format (artist_name, album_name, image.picture_type))
               image_file.write (images.image_data)
               image_file.close ()'''
#print(pygame.mixer.get_busy())


#hu()
root.mainloop()
