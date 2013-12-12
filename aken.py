from tkinter.ttk import *
from tkinter import *
from map import *
from lahing import *


class Kaart(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master=None,bg="black")
        self.bind_all("<Key>",self.press)
        self.pack()
        self.createwidgets()
        self.newmap()

    def refpot(self):
        self.photohe=PhotoImage(file=get_pic(str(hero.pot)))
        self.Heal=Button(self,bg="black",relief=FLAT,image=self.photohe,command=self.heal).grid(column=13,row=6,sticky=(N,S,W,E))

    def refwep(self):
        self.photowep=PhotoImage(file=get_pic(str(hero.W.pic)))
        self.wepinf=Label(self,bg="black",fg="red",font=("Matura MT Script Capitals",9),text=hero.W.name+"\n damage- "+str(hero.W.mindam)+"-"+str(hero.W.maxdam)+"\n"+"critical chance: "+str(int(hero.W.crit*100))+"%").grid(column=12,row=5,columnspan=2,sticky=(N,S,W,E))
        self.wep=Label(self,bg="black",image=self.photowep).grid(column=11,row=5,sticky=(N,S,W,E))

    def refarm(self):
        self.photoarm=PhotoImage(file=get_pic(str(hero.A.pic)))
        self.arminf=Label(self,bg="black",fg="red",font=("Matura MT Script Capitals",9),text=hero.A.name+"\n defence- "+str(hero.A.defence)).grid(column=12,row=4,columnspan=2,sticky=(N,S,W,E))
        self.arm=Label(self,bg="black",image=self.photoarm).grid(column=11,row=4,sticky=(N,S,W,E))

    def refelud(self):
        self.elud=Label(self,bg="black",fg="red",text=(hero.hp,"/100"),font=("Matura MT Script Capitals",9)).grid(row=1,column=11,sticky=(N,W,S,E))
        self.eludebar=Progressbar(self,value=hero.hp).grid(row=1,column=12,columnspan=2,sticky=(N,W,S,E))
        if hero.hp<=0:
            global message
            message="YOU DIED"
            self.quit()

    def refmon(self):
        self.mName=Label(self,bg="black",fg="Red",text=hero.M.name,font=("Matura MT Script Capitals",12)).grid(column=11,row=2,columnspan=3,sticky=(N,S,W,E))
        if hero.M.name!=' ':
            self.melud=Label(self,bg="black",fg="Red",text=(hero.M.hp,"/100"),font=("Matura MT Script Capitals",9)).grid(row=3,column=11,sticky=(N,S,W,E))
            self.meludebar=Progressbar(self,value=hero.M.hp).grid(row=3,column=12,columnspan=2,sticky=(N,W,S,E))
        else:
            self.melud=Label(self,bg="black",fg="Red",text=(""),font=("Matura MT Script Capitals",9)).grid(row=3,column=11,sticky=(N,S,W,E))
            # must taust
            # self.meludebar=Label(self,bg="black",image=self.photoblank).grid(column=12,row=3,sticky=(N,S,W,E))
    def press(self,e):
        key = e.keysym
        if not hero.battle:
            if key == "Left":
                self.left()
            elif key == "Right":
                self.right()
            elif key == "Up":
                self.up()
            elif key == "Down":
                self.down()
        if key == "Escape":
            self.quit()
        if hero.battle:
            if key == "q":
                self.attack()
            elif key == "w":
                self.defend()
        if key == "e":
            self.heal()
    def newmap(self):
        self.Kaart=[]
        Kangelane,Map=out()
        for row in range(7):
            Row=[]
            for element in range(7):
                Row.append(Label(self,bg="black",image=Map[Kangelane[0]+row-3][Kangelane[1]+element-3]).grid(column=element+1,row=row+2,sticky=(N,S,W,E)))
            self.Kaart.append(Row)
        self.Kaart[5][5]=Label(self,bg="black",image=self.photokangelane).grid(column=4,row=5,sticky=(N,S,W,E))
    def refmap(self):
        Kangelane,Map=out()
        for row in range(7):
            for element in range(7):
                self.Kaart[row][element]=Label(self,bg="black",image=Map[Kangelane[0]+row-3][Kangelane[1]+element-3]).grid(column=element+1,row=row+2,sticky=(N,S,W,E))
        self.Kaart[5][5]=Label(self,bg="black",image=self.photokangelane).grid(column=4,row=5,sticky=(N,S,W,E))
    def createwidgets(self):

        self.photokangelane=PhotoImage(file=get_pic(hero.gender))
#        self.kaardil=["T",PhotoImage(file=get_pic("T")),"B",PhotoImage(file=get_pic("B")),
#                      "H",PhotoImage(file=get_pic("H")),"M",PhotoImage(file=get_pic("M")),
#                      "#",PhotoImage(file=get_pic("#")),".",PhotoImage(file=get_pic("."))]
        self.photoblank=PhotoImage(file=get_pic(" "))
        self.photor=PhotoImage(file=get_pic("R"))
        self.photoq=PhotoImage(file=get_pic("Q"))
        self.photol=PhotoImage(file=get_pic("L"))
        self.photou=PhotoImage(file=get_pic("U"))
        self.photod=PhotoImage(file=get_pic("D"))
        self.photohe=PhotoImage(file=get_pic(str(hero.pot)))
        self.photoat=PhotoImage(file=get_pic("attack"))
        self.photode=PhotoImage(file=get_pic("defence"))
        self.photowep=PhotoImage(file=get_pic(hero.W.pic))
        self.photoarm=PhotoImage(file=get_pic(hero.A.pic))
        self.photohead=PhotoImage(file=get_pic("head"))
        self.photofoot=PhotoImage(file=get_pic("foot"))
        self.photovasak=PhotoImage(file=get_pic("vasak"))
        self.photoparem=PhotoImage(file=get_pic("parem"))
        style=Style()
        style.configure("SD",background="black")

        self.head=Label(self,bg="black",image=self.photohead).grid(column=0,row=0,columnspan=9,rowspan=2,sticky=(N,S,W,E))
        self.eludebar=Progressbar(self,value=hero.hp).grid(row=1,column=12,columnspan=2,sticky=(N,W,S,E))
        self.foot=Label(self,bg="black",image=self.photofoot).grid(column=0,row=9,columnspan=9,sticky=(N,S,W,E))
        self.vasak=Label(self,bg="black",image=self.photovasak).grid(column=0,row=2,rowspan=7,sticky=(N,S,W,E))
        self.parem=Label(self,bg="black",image=self.photoparem).grid(column=8,row=2,rowspan=7,sticky=(N,S,W,E))
        self.Title=Label(self,bg="black",fg="Red",text="Something Dungeon",font=("Matura MT Script Capitals",20)).grid(column=0,row=0,columnspan=10,sticky=(N,S,W,E))
        self.Name=Label(self,bg="black",fg="Red",text=hero.name,font=("Matura MT Script Capitals",12)).grid(column=11,row=0,columnspan=3,sticky=(N,S,W,E))
        self.wep=Label(self,bg="black",image=self.photowep).grid(column=11,row=5,sticky=(N,S,W,E))
        self.arm=Label(self,bg="black",image=self.photoarm).grid(column=11,row=4,sticky=(N,S,W,E))
        self.wepinf=Label(self,bg="black",fg="red",font=("Matura MT Script Capitals",9),text=hero.W.name+"\n damage- "+str(hero.W.mindam)+"-"+str(hero.W.maxdam)+"\n"+"critical chance: "+str(int(hero.W.crit*100))+"%").grid(column=12,row=5,columnspan=2,sticky=(N,S,W,E))
        self.arminf=Label(self,bg="black",fg="red",font=("Matura MT Script Capitals",9),text=hero.A.name+"\n defence- "+str(hero.A.defence)).grid(column=12,row=4,columnspan=2,sticky=(N,S,W,E))
        self.blank1=Label(self,bg="black",image=self.photoblank).grid(column=11,row=9,sticky=(N,S,W,E))
        self.blank2=Label(self,bg="black",image=self.photoblank).grid(column=11,row=7,sticky=(N,S,W,E))
        self.blank3=Label(self,bg="black",image=self.photoblank).grid(column=13,row=7,sticky=(N,S,W,E))
        self.Right=Button(self,bg="black",image=self.photor,relief=FLAT,command=self.right,width=50,height=50).grid(column=13,row=8,sticky=(N,S,W,E))
        self.Quit=Button(self,bg="black",relief=FLAT,image=self.photoq, command=self.QUIT,width=50,height=50).grid(column=13,row=9,sticky=(N,S,W,E))
        self.Left=Button(self,bg="black",relief=FLAT,image=self.photol,command=self.left,width=50,height=50).grid(column=11,row=8,sticky=(N,S,W,E))
        self.Up=Button(self,bg="black",relief=FLAT,image=self.photou,command=self.up,width=50,height=50).grid(column=12,row=7,sticky=(N,S,W,E))
        self.Down=Button(self,bg="black",relief=FLAT,image=self.photod,command=self.down,width=50,height=50).grid(column=12,row=9,sticky=(N,S,W,E))
        self.Defend=Button(self,bg="black",relief=FLAT,image=self.photode,command=self.defend).grid(column=12,row=6,sticky=(N,S,W,E))
        self.Attack=Button(self,bg="black",relief=FLAT,image=self.photoat,command=self.attack).grid(column=11,row=6,sticky=(N,S,W,E))
        self.Heal=Button(self,bg="black",relief=FLAT,image=self.photohe,command=self.heal).grid(column=13,row=6,sticky=(N,S,W,E))
        self.elud=Label(self,bg="black",fg="red",text=(hero.hp,"/100"),font=("Matura MT Script Capitals",9)).grid(row=1,column=11,sticky=(N,W,S,E))
        #self.meludebar=Progressbar(self,value=hero.M.hp).grid(row=3,column=12,columnspan=2,sticky=(N,W,S,E))

    def up(self):
        e=UP()
        if e=="p" and hero.pot!=5:
            hero.uuspot()
            self.refpot()
            delfrommap(-1,0)
            UP()
        elif e in stuff:
            if stuff[e][0]=='armor':
                hero.uusarmor(stuff[e][1])
                self.refarm()
                delfrommap(-1,0)
                UP()
            elif stuff[e][0]=='weapon':
                hero.uusrelv(stuff[e][1])
                self.refwep()
                delfrommap(-1,0)
                UP()
            elif stuff[e][0]=='monster':
                hero.uuskoletis(stuff[e][1])
                hero.battle=True
                hero.mloc=(-1,0)
                self.refmon()#lahing...
        self.refmap()
    def down(self):
        e=DOWN()
        if e=="p" and hero.pot!=5:
            hero.uuspot()
            self.refpot()
            delfrommap(1,0)
            DOWN()
        elif e in stuff:
            if stuff[e][0]=='armor':
                hero.uusarmor(stuff[e][1])
                self.refarm()
                delfrommap(1,0)
                DOWN()
            if stuff[e][0]=='weapon':
                hero.uusrelv(stuff[e][1])
                self.refwep()
                delfrommap(1,0)
                DOWN()
            if stuff[e][0]=='monster':
                hero.uuskoletis(stuff[e][1])
                hero.battle=True
                hero.mloc=(1,0)
                self.refmon()
                #kunagi DOWN()
        self.refmap()

    def right(self):
        e=RIGHT()
        if e=="p" and hero.pot!=5:
            hero.uuspot()
            self.refpot()
            delfrommap(0,1)
            RIGHT()
        elif e in stuff:
            if stuff[e][0]=='armor':
                hero.uusarmor(stuff[e][1])
                self.refarm()
                delfrommap(0,1)
                RIGHT()
            if stuff[e][0]=='weapon':
                hero.uusrelv(stuff[e][1])
                self.refwep()
                delfrommap(0,1)
                RIGHT()
            if stuff[e][0]=='monster':
                hero.uuskoletis(stuff[e][1])
                hero.battle=True
                hero.mloc=(0,1)
                self.refmon()
        self.refmap()

    def left(self):
        e=LEFT()
        if e=="p" and hero.pot!=5:
            hero.uuspot()
            self.refpot()
            delfrommap(0,-1)
            LEFT()
        elif e in stuff:
            if stuff[e][0]=='armor':
                hero.uusarmor(stuff[e][1])
                self.refarm()
                delfrommap(0,-1)
                LEFT()
            if stuff[e][0]=='weapon':
                hero.uusrelv(stuff[e][1])
                self.refwep()
                delfrommap(0,-1)
                LEFT()
            if stuff[e][0]=='monster':
                hero.uuskoletis(stuff[e][1])
                hero.battle=True
                hero.mloc=(0,-1)
                self.refmon()
        self.refmap()

    def attack(self):
        if hero.battle:
            lahing('a',hero)
            self.refelud()
            self.refmon()
            if hero.battle=="end":
                global message
                message="You have WON"
                self.quit()
            if not hero.battle:
                self.meludase=Label(self,bg="black").grid(row=3,column=11,columnspan=3,sticky=(N,W,S,E))
                if hero.mloc[0]==0:
                    if hero.mloc[1]==1:
                        self.right()
                    else:
                        self.left()
                elif hero.mloc[0]==-1:
                    self.up()
                else:
                    self.down()
    def defend(self):
        if hero.battle:
            lahing('d',hero)
            self.refelud()
            self.refmon()
            if not hero.battle:
                self.meludease=Label(self,bg="black").grid(row=3,column=11,columnspan=3,sticky=(N,W,S,E))
                if hero.mloc[0]==0:
                    if hero.mloc[1]==1:
                        self.right()
                    else:
                        self.left()
                elif hero.mloc[0]==-1:
                    self.up()
                else:
                    self.down()
    def heal(self):
        hero.Heal()
        self.refpot()
        self.refelud()

    def QUIT(self):
        global message
        message="You have left the game"
        self.quit()

class Tiitel(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master=None,bg="black")
        self.bind_all("<Key>",self.press)
        self.pack()
        self.ok=False
        self.createwidgets()
    def createwidgets(self):
        self.photohead=PhotoImage(file=get_pic("head"))
        self.head=Label(self,bg="black",image=self.photohead).grid(column=0,row=0,columnspan=2,rowspan=2,sticky=(N,S,W,E))
        self.nimekast=Label(self,text="Name:",fg="red",bg="black",font=("Matura MT Script Capitals",12)).grid(column=0,row=2,sticky=(N,S,W,E))
        self.nimi=StringVar()
        Entry(self,textvariable=self.nimi,fg="red",bg="black",font=("Matura MT Script Capitals",12)).grid(column=1,row=2,sticky=(N,S,W,E))
        self.sex=StringVar()
        Radiobutton(self,text="Female",variable=self.sex,value="fem",fg="red",bg="black",font=("Matura MT Script Capitals",12)).grid(column=0,row=3,sticky=(N,S,W,E))
        Radiobutton(self,text="Male",variable=self.sex,value="male",fg="red",bg="black",font=("Matura MT Script Capitals",12)).grid(column=1,row=3,sticky=(N,S,W,E))
        self.mapnr=StringVar()
        Radiobutton(self,text="Map nr. 1",variable=self.mapnr,value="map1.txt",fg="red",bg="black",font=("Matura MT Script Capitals",12)).grid(column=0,row=4,sticky=(N,S,W,E))
        Radiobutton(self,text="Map nr. 2",variable=self.mapnr,value="map2.txt",fg="red",bg="black",font=("Matura MT Script Capitals",12)).grid(column=1,row=4,sticky=(N,S,W,E))
        self.cont=Button(self,text="CONTINUE",command=self.check,fg="red",bg="black",font=("Matura MT Script Capitals",9)).grid(column=0,row=5,sticky=(N,S,W,E))
        self.juhis=Label(self,bg="black",fg="Red",text='''How to play:
Controls:
move arrows, attack Q, defend W, heal E.
Health pots heal 50hp.
If you defend then you can attack with
more force (depending on your defence) next time.
If you run into a monster then you can't run away before you kill it.
If you die, the game ends.''',font=("Matura MT Script Capitals",10)).grid(column=0,row=6,columnspan=2,sticky=(N,S,W,E))
    def press(self,e):
        key = e.keysym
        if key=="Return":
            self.check()
    def check(self):
        if self.sex.get()!="" and self.mapnr.get()!="":
            global hero
            if self.nimi.get()=="Mihkel":
                loo_kaart("maps.txt")
            else:
                loo_kaart(self.mapnr.get())
            hero=char(self.nimi.get(),self.sex.get())
            self.quit()
class end(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master=None,bg="black")
        self.createwidgets()

    def createwidgets(self):
        self.inf=Label(text=message,fg="red",bg="black",font=("Matura MT Script Capitals",12)).grid(row=0,column=0,columnspan=2,sticky=(N,S,W,E))
        self.esc=Button(text="QUIT",fg="red",bg="black",font=("Matura MT Script Capitals",12),command=self.ESC).grid(row=1,column=0,sticky=(N,S,W,E))
        self.re=Button(text="REPLAY",fg="red",bg="black",font=("Matura MT Script Capitals",12),command=self.re).grid(row=1,column=1,sticky=(N,S,W,E))
    def ESC(self):
        self.quit()
        global play
        play=False
    def re(self):
        self.quit()
play=True
while play==True:
    root=Tk()
    root.title("Something Dungeon")
    aken1=Tiitel(root)
    aken1.mainloop()
    aken1.destroy()
    aken2=Kaart(root)
    aken2.mainloop()
    aken2.destroy()
    aken3=end(root)
    aken3.mainloop()
    aken3.destroy()
    root.destroy()
