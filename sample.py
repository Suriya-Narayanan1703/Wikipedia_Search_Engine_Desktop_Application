import tkinter as tk
#from PIL import Image,ImageTk
import wikipedia as wk
import fpdf as f
universe = tk.Tk()
universe.geometry('1000x1000')
universe.title("kosmos")
name_var=tk.StringVar()
def history(i,p):
        if(i==0):
            print(" ")
        else:
            label4 = tk.Label(universe, text=p)
def submit():
    def download(name, result):
        pdf = f.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        print(name)
        pdf.cell(200, 10, txt=name, ln=1, align='C')
        #res1=result.split('.')
        k=2
        count = 0
        sp = " "
        dum = ""
        for i in result:
            if(i is sp):
                count+=1
                if (count <= 10):
                    dum += i
                else:
                    pdf.cell(10, 10, txt=dum, ln=k)
                    count = 0
                    dum = " "
                    k+=1
            else:
                dum += i
        #pdf.cell(10, 10, txt=result, ln=2)
        #pdf.cell(10, 10, txt=res1[1], ln=3)
        #pdf.cell(10, 10, txt=res1[2], ln=4)
        j=name+".pdf"
        pdf.output(j)
    name = name_var.get()
   # history(r,name)
    #name_label.grid(row=10, column=10)
    result = wk.summary(name, sentences=3)
    ssd = tk.Label(universe, text="Result:")
    ssd.place(x=100, y=300)
    #name_label = tk.Label(universe, text=result)
    #name_label.place(x=150, y=330)
    text = tk.Text(universe,height=10,width=100)
    text.place(x=100,y=350)
    text.insert(tk.INSERT,result)
    res=str(result)
    #name_label.grid(row=10, column=2)
    name_var.set("")
    universe.bind("<Return>",lambda eff: download(name="Suriya",result="Suriya"))
    M = tk.Button(universe, text="Download content as pdf", command=lambda:download(name,res))  # , command=login)  #
    M.place(x=100, y=530)
    def hindi():
        wk.set_lang('hi')
        result = wk.summary(name, sentences=3)
        ssd = tk.Label(universe, text="Result:")
        ssd.place(x=100, y=300)
        # name_label = tk.Label(universe, text=result)
        # name_label.place(x=150, y=330)
        text = tk.Text(universe, height=10, width=100)
        text.place(x=100, y=350)
        text.insert(tk.INSERT, result)
        res = str(result)

    def tamil():
        wk.set_lang('ta')
        result = wk.summary(name, sentences=3)
        ssd = tk.Label(universe, text="Result:")
        ssd.place(x=100, y=300)
        # name_label = tk.Label(universe, text=result)
        # name_label.place(x=150, y=330)
        text = tk.Text(universe, height=10, width=100)
        text.place(x=100, y=350)
        text.insert(tk.INSERT, result)
        res = str(result)
    def telugu():
        wk.set_lang('te')
        result = wk.summary(name, sentences=3)
        ssd = tk.Label(universe, text="Result:")
        ssd.place(x=100, y=300)
        # name_label = tk.Label(universe, text=result)
        # name_label.place(x=150, y=330)
        text = tk.Text(universe, height=10, width=100)
        text.place(x=100, y=350)
        text.insert(tk.INSERT, result)
        res = str(result)
    H = tk.Button(universe, text="Hindi", command=hindi)
    H.place(x=250, y=530)
    t = tk.Button(universe, text="Tamil", command=tamil)
    t.place(x=290, y=530)
    te = tk.Button(universe, text="Telugu", command=telugu)
    te.place(x=330, y=530)
#image1 = Image.open("D:/cosmos.png")
#test = ImageTk.PhotoImage(image1)
#label1 = tk.Label(image=test)
#label1.image = test
# Position image
#label1.place(x=50, y=0)
label4 = tk.Label(universe, text="Kosmos")
label4.place(x=150, y=250)
ent5 = tk.Entry(universe,textvariable=name_var)
n=ent5.get()
print(n)
ent5.place(x=150, y=270)
Q = tk.Button(universe, text="Browse",command=submit)  # , command=login)  #
Q.place(x=310, y=270)
#history=tk.Button(universe,text="History",command=lambda:submit(1))
#history.place(x=370,y=270)
universe.mainloop()