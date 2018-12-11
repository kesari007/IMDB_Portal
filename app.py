try:
	import Tkinter as tk
except:
	import tkinter as tk
import imdb_gui
root=tk.Tk()
s=tk.StringVar(root)
def info():
	root1=tk.Tk()
	root1.title("Movie : "+s.get())
	l=imdb_gui.info_movie(s.get())
	if(not(l)):
		tk.Label(root1, text="\t").grid(column=0)
		tk.Label(root1, text="\t").grid(column=2)
		tk.Label(root1, text="\n").grid(row=0)
		tk.Label(root1, text="\n").grid(row=2)
		w=tk.Label(root1, text=str("No such movie titled '" + s.get() + "' found"))
		w.grid(column=1, row=1)
		root1.mainloop()
		return
	l[3]+=" minutes"
	tk.Label(root1, text="\t").grid(column=0)
	tk.Label(root1, text="\t").grid(column=3)
	tk.Label(root1, text="MOVIE DESCRIPTION", font=("times", 20)).grid(row=0, column=1, columnspan=2)
	tk.Label(root1, text="\n").grid(row=1)
	tk.Label(root1, text="TITLE : ", justify='right').grid(row=2, column=1)
	tk.Label(root1, text="IMDB RATING : ", justify='right').grid(row=3, column=1)
	tk.Label(root1, text="RELEASED ON : ", justify='right').grid(row=4, column=1)
	tk.Label(root1, text="DURATION : ", justify='right').grid(row=5, column=1)
	tk.Label(root1, text="GENRE : ", justify='right').grid(row=6, column=1)
	tk.Label(root1, text="PLOT : ", justify='right').grid(row=7, column=1)
	tk.Label(root1, text=l[0]).grid(row=2, column=2)
	tk.Label(root1, text=l[1]).grid(row=3, column=2)
	tk.Label(root1, text=l[2]).grid(row=4, column=2)
	tk.Label(root1, text=l[3]).grid(row=5, column=2)
	tk.Label(root1, text=l[4]).grid(row=6, column=2)
	tk.Message(root1, text=l[5]).grid(row=7, column=2)
	tk.Label(root1, text="\n").grid(row=8)
	root1.mainloop()

def c1():
	w=tk.Label(root, text="Name of the Movie : ")
	w.grid(row=7, column=1)
	w=tk.Entry(root, textvariable=s)
	w.grid(row=7, column=2)
	w.bind("<Return>", info)
	w.focus()
	w1=tk.Button(root, text="Submit", command=info)
	w1.grid(row=7, column=3)

def top():
	root1=tk.Tk()
	root1.title("Top Rated Movies")
	l=imdb_gui.top_movies(int(s.get()))
	tk.Label(root1, text="\t").grid(column=0)
	tk.Label(root1, text="\t").grid(column=3)
	tk.Label(root1, text="THE "+s.get()+" TOP RATED MOVIES ARE :", font=("times", 20)).grid(row=0, column=1, columnspan=2)
	tk.Label(root1, text="\n").grid(row=1)
	tk.Label(root1, text="TITLE", font=('Courier', 15)).grid(row=2, column=1)
	tk.Label(root1, text="IMDB RATING", font=('Courier', 15)).grid(row=2, column=2)
	j=0
	for i in l:
		tk.Label(root1, text=i[0]).grid(row=j+3, column=1)
		tk.Label(root1, text=i[1]).grid(row=j+3, column=2)
		j+=1
	tk.Label(root1, text="\n").grid(row=j+3)
	root1.mainloop()

def c2():
	w=tk.Label(root, text="Enter n to display n top movies : ")
	w.grid(row=11, column=1)
	w=tk.Entry(root, textvariable=s)
	w.grid(row=11, column=2)
	w1=tk.Button(root, text="Submit", command=top)
	w1.grid(row=11, column=3)

def fold():
	root1=tk.Tk()
	root1.title("Renaming of Folders")
	l=imdb_gui.folder(s.get())
	tk.Label(root1, text="\t").grid(column=0)
	tk.Label(root1, text="\t").grid(column=4)
	tk.Label(root1, text="\n").grid(row=1)
	j=0
	tk.Label(root1, text="SHOWING RESULTS FOR THE PATH : "+s.get(), font=('times', 20)).grid(row=0, column=1, columnspan=3)
	for i in l:
		if(i[:4]=="AABB"):
			tk.Label(root1, text=i[4:]).grid(row=j+2, column=1)
			tk.Label(root1, text=":").grid(row=j+2, column=2)
			tk.Label(root1, text="No Such Movie Exists*").grid(row=j+2, column=3)
		else:
			tk.Label(root1, text=i).grid(row=j+2, column=1)
			tk.Label(root1, text=":").grid(row=j+2, column=2)
			tk.Label(root1, text="Renaming Done...").grid(row=j+2, column=3)
		j+=1
	tk.Label(root1, text="\n").grid(row=j+2)
	tk.Label(root1, text="*Please read the instructions again", font=('Courier', 10)).grid(row=j+3, column=3)
	root1.mainloop()

def c3():
	w=tk.Message(root, text="Enter the Complete Path of the Directory where the movies are present", justify='center')
	w.grid(row=15, column=1)
	w=tk.Entry(root, textvariable=s)
	w.grid(row=15, column=2)
	w1=tk.Button(root, text="Submit", command=fold)
	w1.grid(row=15, column=3)



root.title("IMDB Portal")
tk.Label(root, text="\n").grid(row=1, column=0)
tk.Label(root, text="\n").grid(row=6, column=0)
tk.Label(root, text="\n").grid(row=8, column=0)
tk.Label(root, text="\n").grid(row=10, column=0)
tk.Label(root, text="\n").grid(row=12, column=0)
tk.Label(root, text="\n").grid(row=14, column=0)
tk.Label(root, text="Welcome to the IMDB Portal", font=("times",20), justify="center").grid(row=0, column=1, columnspan=3)
w=tk.Button(root, text="Search Movie Information by Title",  command=c1)
w.grid(row=5, column=1, columnspan=3)
w=tk.Button(root, text="Show Top Rated Movies", command=c2)
w.grid(row=9, column=1, columnspan=3)
w=tk.Button(root, text="Rename Folder with IMDB Rating and Year of Release added to it", command=c3)
w.grid(row=13, column=1, columnspan=3)
root.mainloop()
