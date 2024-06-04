from tkinter import*
from tkinter import ttk
import random, os
from tkinter import messagebox
import tempfile
from time import strftime


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1570x1200+0+0")
        self.root.title("Billing Software")
        self.input_value = True

        # variables
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

        # Total product price & tax variables
        self.clothing_price = StringVar()
        self.lifestyle_price = StringVar()
        self.mobiles_price = StringVar()
        self.clothing_tax = StringVar()
        self.lifestyle_tax = StringVar()
        self.mobiles_tax = StringVar()

        # Customer details
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        self.c_email = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # Product categories lists
        self.Category = ['Select Option', 'Clothing', 'LifeStyle', 'Mobiles']
        self.ClothingSubCat = ['Pant', 'T-Shirt', 'Shirt']
        self.Pant = ['Levis', 'Mufti', 'Spykar']
        self.price_pant = 5000
        self.price_pantlocal = 7000
        self.price_pantmax = 8000
        self.T_shirt = ['Polo', 'Roadster', 'Jack&Jones']
        self.price_polo = 1500
        self.price_Roadster = 1800
        self.price_JackJones = 1700
        self.Shirt = ['Peter England', 'Louis Phillipe', 'Park Avenue']
        self.price_Peter = 2100
        self.price_Louis = 2700
        self.price_Park = 1740

        self.LifStyleSubCat = ['Bath Soap', 'Face Creame', 'Hair Oil']
        self.Bath_soap = ['LifeBuy', 'Lux', 'Santoor', 'Pearl']
        self.price_life = float(20)
        self.price_lux = 20
        self.price_santoor = 20
        self.price_pearl = 30
        self.Face_creame = ['Fair&Lovely', 'Ponds', 'Olay', 'Garnier']
        self.price_fair = 20
        self.price_ponds = 20
        self.price_olay = 20
        self.price_garnier = 30
        self.Hair_oil = ['Parachute', 'Jashmin', 'Bajaj']
        self.price_para = 25
        self.price_jashmin = 22
        self.price_bajaj = 30

        self.MobilesSubCat = ['Iphone', 'Sumsung', 'Xiome', 'RealMe', "One+"]
        self.Iphone = ['Iphone_X', 'Iphone_11', 'Iphone_12']
        self.price_ix = 40000
        self.price_i11 = 60000
        self.price_i12 = 85000
        self.Samsung = ['Samsung M16', 'Sumsung M12', 'Sumsung M21']
        self.price_sm16 = 16000
        self.price_sm12 = 12000
        self.price_sm21 = 18000
        self.Xiome = ['Red11', 'Redme-12', 'RedmePro']
        self.price_r11 = 11000
        self.price_r12 = 12000
        self.price_rpro = 9000
        self.RealMe = ['RealMe 12', 'RealMe 13', 'RealMe Pro']
        self.price_rel12 = 25000
        self.price_rel13 = 22000
        self.price_relpro = 30000
        self.OnePlus = ['OnePlus1', 'OnePlus2', 'OnePlus3']
        self.price_one1 = 45000
        self.price_one12 = 60000
        self.price_one3 = 45800

        # Project title
        title = Label(self.root, text="BillGenie", font=("Roboto", 30, "bold"), bg="white", fg="red")
        title.place(x=0, y=0, width=1540, height=45)

        def update_time_date(): 
            current_time = strftime('%H:%M:%S %p')
            current_date = strftime('%Y-%m-%d')
            lbl_time.config(text=current_time)
            lbl_date.config(text=current_date)
            lbl_time.after(1000, update_time_date)

        lbl_time = Label(title, font=('times new roman', 16, 'bold'), background='white', foreground='blue')
        lbl_time.place(x=0, y=(-15), width=120, height=50)
        
        lbl_date = Label(title, font=('times new roman', 16, 'bold'), background='white', foreground='blue')
        lbl_date.place(x=120, y=(-15), width=120, height=50)
        
        update_time_date()
        
        
        self.bg_color="white"

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg=self.bg_color)
        Main_Frame.place(x=0,y=100,width=1535,height=620)

        # Customer LabelFrame
        CustFrame=LabelFrame(Main_Frame,text="Customer",bg=self.bg_color,fg="red",font=("arial",12,"bold"))
        CustFrame.place(x=10,y=0,width=350,height=140)
       
        self.lblMobile=Label(CustFrame,font=('arial',12,'bold'),bg=self.bg_color,text="Mobile No.",bd=4)
        self.lblMobile.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.txtMobile=ttk.Entry(CustFrame,font=('arial',10,'bold'),textvariable=self.c_phon,width=24)
        self.txtMobile.grid(row=0,column=1,sticky=W,padx=5,pady=2)
   
        self.lblCustName=Label(CustFrame,font=('arial',12,'bold'),bg=self.bg_color,text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(CustFrame,font=('arial',10,'bold'),textvariable=self.c_name,width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(CustFrame,font=('arial',12,'bold'),bg=self.bg_color,text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(CustFrame,font=('arial',10,'bold'),textvariable=self.c_email,width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Product LabelFrame
        ProductFrame=LabelFrame(Main_Frame,text="Product",bg=self.bg_color,fg="red",font=("arial",12,"bold"))
        ProductFrame.place(x=370,y=0,width=620,height=140)

        # # search LabelFrame
        # SerachFrame=Frame(Main_Frame,bd=2,bg="white")
        # SerachFrame.place(x=1000,y=10,width=350,height=40)

        # # cbill_label=Label(SerachFrame,text="Bill Number",bg="red",fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0)
        # # cbill_txt=ttk.Entry(SerachFrame,width=12,textvariable=self.search_bill,font="arial 14").grid(row=0,column=1,padx=2)

        # bill_btn=Button(SerachFrame,text="Search",command=self.find_bill,width=14,font="arial 11 bold",bg="orangered",fg="white").grid(row=0,column=2,padx=2)


         # MiddleFrmae
        MiddleFame=Frame(Main_Frame,bd=10)
        MiddleFame.place(x=10,y=150,width=800,height=250)
        
       # imgm1 = Image.open(r"img\good.jpg")
       # imgm1 = imgm1.resize((490,350), Image.ANTIALIAS)
       # self.photoImgm1= ImageTk.PhotoImage(imgm1)
       # bg_lbl=Label(MiddleFame,image=self.photoImgm1)
       # bg_lbl.place(x=0,y=0,width=490,height=350)

       # imgm2 = Image.open(r"img\mall.jpg")
       # imgm2 = imgm2.resize((490,350), Image.ANTIALIAS)
       # self.photoImgm2= ImageTk.PhotoImage(imgm2)
       # bg_lbl=Label(MiddleFame,image=self.photoImgm2)
       # bg_lbl.place(x=490,y=0,width=490,height=350)


        # Rightlabelframe Bill Area
        RightFame=LabelFrame(Main_Frame,text="Bill Area",bd=2,bg='white',font=('arial',12,'bold'),fg="red")
        RightFame.place(x=870,y=140,width=480,height=280)
        bill_title=Label(RightFame,text="Bill Reciept",fg="blue",bg="white",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)

        scroll_y=Scrollbar(RightFame,orient=VERTICAL)
        self.textarea=Text(RightFame,yscrollcommand=scroll_y.set,bg="white",fg='blue',font=('arial',12,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        self.lblCategories=Label(ProductFrame,font=('arial',12,'bold'),bg=self.bg_color,text="Select Category.",bd=4)
        self.lblCategories.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.ComboCategories=ttk.Combobox(ProductFrame,value=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
        self.ComboCategories.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.ComboCategories.current(0)
        self.ComboCategories.bind("<<ComboboxSelected>>",self.Categories)

        self.lblSubCategory=Label(ProductFrame,font=('arial',12,'bold'),bg=self.bg_color,text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(ProductFrame,state="readonly",value=[""],font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.current(0)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_Add)
        
        self.lblproduct=Label(ProductFrame,font=('arial',12,'bold'),bg=self.bg_color,text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(ProductFrame,value=[""],textvariable=self.product,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        self.lblPrice=Label(ProductFrame,font=('arial',12,'bold'),bg=self.bg_color,text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(ProductFrame,state="readonly",textvariable=self.prices,value=[""],font=('arial',10,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        self.lblQty=Label(ProductFrame,font=('arial',12,'bold'),bg=self.bg_color,text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(ProductFrame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
  
        # BottomlabelFrmae
        BottomFame=LabelFrame(Main_Frame,text="Bill Counter",bd=2,bg='white',font=('arial',12,'bold'),fg="red")
        BottomFame.place(x=0,y=420,width=1520,height=120)

        # Total Poduct Price tax
        self.lblTotal=Label(BottomFame,font=('arial',12,'bold'),bg=self.bg_color,text="Sub Total",bd=4)
        self.lblTotal.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        
       
        self.txtTotal=ttk.Entry(BottomFame,textvariable=self.sub_total,font=('arial',10,'bold'),width=24)
        self.txtTotal.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(BottomFame,font=('arial',12,'bold'),bg=self.bg_color,text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(BottomFame,font=('arial',10,'bold'),textvariable=self.tax_input,width=24)
        self.txt_tax.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(BottomFame,font=('arial',12,'bold'),bg=self.bg_color,text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=2,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(BottomFame,font=('arial',10,'bold'),textvariable=self.total,width=24)
        self.txtAmountTotal.grid(row=2,column=3,sticky=W,padx=5,pady=2)

        # Buttons
        btnFrame=Frame(BottomFame,bd=2,bg=self.bg_color)
        btnFrame.place(x=320,y=0)

        self.btn_AddToCart=Button(btnFrame,height=2,text="Add To Cart",command=self.iaddItem,width=12,bg="orangered",fg="white",font=('arial',15,'bold'))
        self.btn_AddToCart.grid(row=0,column=0,padx=1,pady=5)

        self.btn_generate_bill=Button(btnFrame,height=2,text="Generate Bill",command=self.gen_bill,width=12,bg="orangered",fg="white",font=('arial',15,'bold'))
        self.btn_generate_bill.grid(row=0,column=1,padx=1,pady=5)

        self.btn_save=Button(btnFrame,height=2,text="Save Bill",command=self.save_bill,width=12,bg="orangered",fg="white",font=('arial',15,'bold'))
        self.btn_save.grid(row=0,column=2,padx=1,pady=5)

        self.btn_save=Button(btnFrame,height=2,text="Print",command=self.iPrint,width=12,bg="orangered",fg="white",font=('arial',15,'bold'))
        self.btn_save.grid(row=0,column=3,padx=1,pady=5)

        self.btn_Clear=Button(btnFrame,height=2,text="Clear",command=self.clear,width=12,bg="orangered",fg="white",font=('arial',15,'bold'))
        self.btn_Clear.grid(row=0,column=4,padx=1,pady=5)

        self.btn_Exit=Button(btnFrame,height=2,command=self.root.destroy,text="Exit",width=12,bg="orangered",fg="white",font=('arial',15,'bold'))
        self.btn_Exit.grid(row=0,column=5,padx=1,pady=5)

    
        self.welcome()

        self.l=[]
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        # self.bill_no.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        # self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()


    def iPrint(self):
        q=self.textarea.get("1.0","end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,"w").write(q)
        os.startfile(filename,"print")

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,f"\n Bill Number:\t{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")
        current_date = strftime('%Y-%m-%d')
        self.textarea.insert(END, f"\n Date: {current_date}") 
        current_time = strftime('%H:%M:%S %p')
        self.textarea.insert(END, f"\n Time: {current_time}")
        
        self.textarea.insert(END,"\n ==================================================")
        self.textarea.insert(END,"\n Products\t\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n ==================================================\n")

    def iaddItem(self):
        Tax=2
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror('Error',"Plaese Enter Mobile No. & Select The Product") 
        else:
            self.textarea.insert(END,f'\n {self.product.get()}\t\t\t{self.qty.get()} \t\t{self.m}')
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    
    def gen_bill(self):
        if self.product.get()=="":
                messagebox.showerror('Error',"Plaese Add To Cart Product") 
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ==================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n ==================================================\n")
        
      
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            messagebox.showinfo("Saved",f"Bill No: {self.bill_no.get()} saved Successfully")
            f1.close()

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete("1.0",END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def Categories(self,event=""):
        if self.ComboCategories.get()=="Clothing":
            self.ComboSubCategory.config(value=self.ClothingSubCat)
            self.ComboSubCategory.current(0)

        if self.ComboCategories.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.LifStyleSubCat)
            self.ComboSubCategory.current(0)

        if self.ComboCategories.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.MobilesSubCat)
            self.ComboSubCategory.current(0) 

    def Product_Add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.Pant)   
            self.ComboProduct.current(0)   
       
        if self.ComboSubCategory.get()=="T-Shirt":
            self.ComboProduct.config(value=self.T_shirt)   
            self.ComboProduct.current(0)   

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)   
            self.ComboProduct.current(0) 
  
            
        # Lifestyle
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)   
            self.ComboProduct.current(0)       

        if self.ComboSubCategory.get()=="Face Creame":
            self.ComboProduct.config(value=self.Face_creame)   
            self.ComboProduct.current(0)     
  
            
            
        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)   
            self.ComboProduct.current(0) 

        # Mobile
        if self.ComboSubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)   
            self.ComboProduct.current(0)       

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)   
            self.ComboProduct.current(0)     
        
        if self.ComboSubCategory.get()=="Xiome":
            self.ComboProduct.config(value=self.Xiome)   
            self.ComboProduct.current(0)   

        if self.ComboSubCategory.get()=="RealMe":
            self.ComboProduct.config(value=self.RealMe)   
            self.ComboProduct.current(0)   

        if self.ComboSubCategory.get()=="Oneplus":
            self.ComboProduct.config(value=self.OnePlus)   
            self.ComboProduct.current(0)   

    def price(self,event=""):
        # pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_pant)
            self.ComboPrice.current(0)
            self.qty.set(1)    


        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_pantlocal)
            self.ComboPrice.current(0)
            self.qty.set(1)    
            
      
        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_pantmax)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        # T-Shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        # Shirt
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="LifeBuy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Pearl":
            self.ComboPrice.config(value=self.price_pearl)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Fair&Lovel":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Jashmin":
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Iphone_X":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Sumsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Sumsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0) 
            self.qty.set(1)    


        if self.ComboProduct.get()=="Red11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="Redme-12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0) 
            self.qty.set(1)    
            
        if self.ComboProduct.get()=="RedmePro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0) 
            self.qty.set(1)    
            
        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="RealMe Pro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="OnePlus1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="OnePlus2":
            self.ComboPrice.config(value=self.price_one12)
            self.ComboPrice.current(0) 
            self.qty.set(1)    

        if self.ComboProduct.get()=="OnePlus3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0) 
            self.qty.set(1)    
            
def launch_tkinter_app():
    root = Tk()
    app = Bill_App(root)
    root.mainloop()

if __name__ == "__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()

