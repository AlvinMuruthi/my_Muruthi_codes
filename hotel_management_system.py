from tkinter import *

import time
import random
from datetime import date
from turtle import rt

# import image
window = Tk()
window.geometry("1000x600")
window.config(bg="red")
frame_window = LabelFrame(window, bg="grey", height=600)
frame_window.grid(row=0, column=0)
lbl_1 = Label(frame_window, text="WELCOME TO OUR HOTEL" + "SEKU_TUCK_HOTEL", bd=2, width=50, height=4, bg="green")
lbl_2 = Label(frame_window, text="USERS LOGIN", bd=3, width=24, height=4, bg="green")
lbl_3 = Label(frame_window, text="CUSTOMER", bd=3, width=24, height=4, bg="green")
lbl_4 = Label(frame_window, text="ADMIN", bd=3, width=24, height=4, bg="green")

image_label = Label(window, )

"""
    new window for customers fun
    definition of a customer
"""


def Customer_fun():
    window.quit()
    root = Toplevel()

    def price():
        roo = Tk()
        roo.geometry("500x300")
        roo.title("Price List")
        roo.config(bg="white")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=0)
        lblinfo.grid(row=0, column=0, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W,bd=0)
        lblinfo.grid(row=0, column=2, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W,bd=0)
        lblinfo.grid(row=0, column=3, sticky="w")

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Soft Drink", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=1, column=0, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=1, column=3, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="chapati", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=2, column=0, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=2, column=3, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mandazi", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=3, column=0, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=3, column=3, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="sukuma", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=4, column=0, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=4, column=3, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Ugali", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=5, column=0, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=5, column=3, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="hekes", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=6, column=0, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=6, column=3, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=7, column=3, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Meat", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=7, column=0, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=8, column=3, sticky="w")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="#ED420B", anchor=W,bd=0)
        lblinfo.grid(row=8, column=0, sticky="w")

        # exit button function
        def exit():
            roo.destroy()

        btn = Button(roo, text="Exit", bd=3, bg="White", fg="black", activebackground="red", anchor=CENTER,
                     command=exit)
        btn.grid(row=9, column=2, columnspan=3)
        roo.mainloop()

    def clear():
        text.delete(0, END)

    def quit_fun():
        root.destroy()
        window.deiconify

    def total():
        price1 = int(drink.get())
        price2 = int(mandazi.get())
        price3 = int(chapati.get())
        price4 = int(sukuma.get())
        price5 = int(ugali.get())
        price6 = int(hekes.get())
        price7 = int(meat.get())
        price8 = int(tea.get())
        # p1,p2,p3 etc means Price Per Person
        p1 = price1 * 10
        p2 = price1 * 30
        p3 = price1 * 25
        p4 = price1 * 20
        p5 = price1 * 30
        p6 = price1 * 10
        p7 = price1 * 10
        p8 = price1 * 5
        # Cost
        cost = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
        display = cost
        p1_label["text"] = display
        # Service Tax
        service_charge = cost / 20
        service_display = service_charge
        p2_label["text"] = service_display
        # Tax
        tax_charge = int(cost / 3)
        tax_display = tax_charge
        p3_label["text"] = tax_charge
        # Sub Total
        sub_total = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
        sub_display = sub_total
        p4_label["text"] = sub_display
        # Total
        total = display + service_charge + tax_charge
        total_display = total
        p5_label["text"] = total_display
        # Order Number
        num = random.randint(1000, 1000000)
        # global reference_number
        reference_number["text"] = num

    def reset():
        global total
        drink.delete(0, END)
        chapati.delete(0, END)
        mandazi.delete(0, END)
        sukuma.delete(0, END)
        ugali.delete(0, END)
        hekes.delete(0, END)
        meat.delete(0, END)
        tea.delete(0, END)
        p1_label["text"] = ""
        p2_label["text"] = ""
        p3_label["text"] = ""
        p4_label["text"] = ""
        p5_label["text"] = ""
        reference_number["text"] = ""
        # insert 0 in all entries after reset button is clicked
        drink.insert(0, 0)
        chapati.insert(0, 0)
        mandazi.insert(0, 0)
        sukuma.insert(0, 0)
        ugali.insert(0, 0)
        hekes.insert(0, 0)
        meat.insert(0, 0)
        tea.insert(0, 0)

    def clock():
        current = time.strftime("%H:%M:%S")
        label1["text"] = current
        root.after(1000, clock)

    def receipt():
        sub_window = Toplevel()
        sub_window.geometry("400x200")
        sub_window.config(bg="blue")
        sub_window.title("RECEIPT")
        lbl1 = Label(sub_window, text="THENKS FOR CHOOSING OUR SERVICE", anchor=CENTER, width=50, height=2, bd=0,
                     justify=CENTER)
        lbl1_ = Label(sub_window, text="WELCOME AGAIN", anchor=CENTER, width=50, height=2, bd=0, justify=CENTER)
        lbl1__ = Label(sub_window, text="YOUR RECEIPT", anchor=CENTER, width=50, height=2, bd=0, justify=CENTER)

        lbl1.grid(row=0, column=0, padx=2, pady=0)
        lbl1_.grid(row=1, column=0, padx=2, pady=0)
        lbl1__.grid(row=2, column=0, padx=2, pady=0)

        def quit():
            sub_window.destroy()
            root.deiconify

        btnSave = Button(sub_window, text="DONE", bd=10, width=5, height=3, justify=CENTER)
        btnPrint = Button(sub_window, text="DONE", bd=10, width=5, height=3, justify=LEFT)

        btn_done = Button(sub_window, text="DONE", bd=10, width=5, height=3, command=quit, justify=RIGHT)
        btn_done.grid(row=3, column=2)
        btnSave.grid(row=3, column=1)
        btnPrint.grid(row=3, column=0)

    # Customer window
    root = Tk()
    root.config(bg="red4")
    root.geometry("1000x700")
    root.minsize(1000, 700)
    root.maxsize(1000, 700)
    heading1 = Label(root, text="SEKU_TUCK_HOTEL", font="arial 30 bold", fg="#fc5a03")
    heading2 = Label(root, text="Hotel_Management ", font="arial 18 bold", fg="#fc5a03")       #====================== Declaring of frames==============

    frame1 = Frame(root, height="420", width="330", bd=10, bg="#ED420B", highlightthickness=1, relief=SUNKEN)
    frame1.place(x=40, y=140)
    frame2 = Frame(root, height="420", width="330", bd=10, bg="#33A9CE", highlightthickness=1, relief=SUNKEN)
    frame2.place(x=380, y=140)
    # Button Frame
    frame3 = Frame(root, height="100", width="670", bd=10, bg="#ED420B", highlightthickness=1, relief=SUNKEN)
    frame3.place(x=40, y=565)
    cal_frame = Frame(root, height="500", width="450", bd=10, highlightthickness=1, relief=SUNKEN)
    cal_frame.place(x=750, y=150)
    text_frame = Frame(root, height="100", width="100")
    text_frame.place(x=1000, y=50)

    frame_time = Frame(root, height="200", width="200", bd=10, highlightthickness=1, relief=SUNKEN)
    frame_time.place(x=100, y=50)
    # Price Frame

    p1_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
    p1_label.place(x=200, y=80)
    p2_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
    p2_label.place(x=200, y=120)
    p3_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
    p3_label.place(x=200, y=160)
    p4_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
    p4_label.place(x=200, y=200)
    p5_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
    p5_label.place(x=200, y=240)
    reference_number = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
    reference_number.place(x=200, y=40)

    # Text box to print the receipt
    text = Text(root, height=10, width=25, bd=10, font="arial 10")

    text.place(x=750, y=500)
    # Time
    label1 = Label(frame_time, font="article 30", bg="black", fg="#ED420B")
    label1.grid(row=0, column=0)
    clock()
    # Buttons
    # Frame 3
    new_window = Button(frame3, text="Price", command=price, font="arial 15 bold", bd=10)
    new_window.place(x=80, y=10)
    total_btn = Button(frame3, text="Total", command=total, font="arial 15 bold", bd=10)
    total_btn.place(x=210, y=10)
    reset_btn = Button(frame3, text="Reset", command=reset, font="arial 15 bold", bd=10)
    reset_btn.place(x=350, y=10)
    quit_btn = Button(frame3, text="LOG OUT", command=quit_fun, font="arial 15 bold", bd=5)
    quit_btn.place(x=500, y=10)
    clear = Button(root, text="Clear", command=clear, font="arial 10 bold", bd=10)
    clear.place(x=760, y=450)
    # Receipt button
    receipt_btn = Button(root, text="Receipt", font="arial 10 bold", bd=10, command=receipt)
    receipt_btn.place(x=900, y=450)

    # Payment_Entry_Created
    # Frame_2

    ref_num = Label(frame2, text="reference_number", font="arial 12 bold", bg="#33A9CE")
    reference_number = Label(frame2, text=" ", font="arial 12 bold", bg="#33A9CE")
    cost_label = Label(frame2, text="Cost", font="arial 12 bold ", bg="#33A9CE")
    service_tax = Label(frame2, text="Service Cost", font="arial 12 bold", bg="#33A9CE")
    tax = Label(frame2, text="Tax", font="arial 12 bold ", bg="#33A9CE")
    sub_total = Label(frame2, text="Sub Total", font="arial 12 bold", bg="#33A9CE")
    total = Label(frame2, text="Total", font="arial 12 bold ", bg="#33A9CE")
    """
            frame2 objects placing
    """
    ref_num.place(x=10, y=40)
    reference_number.place(x=200, y=40)
    cost_label.place(x=10, y=80)
    service_tax.place(x=10, y=120)
    tax.place(x=10, y=160)
    sub_total.place(x=10, y=200)
    total.place(x=10, y=240)

    # Food_item_Entry_Created
    # Frame1_objects
    drink = Entry(frame1, bd="3")
    chapati = Entry(frame1, bd="5")
    mandazi = Entry(frame1, bd="5")
    sukuma = Entry(frame1, bd="5")
    ugali = Entry(frame1, bd="5")
    hekes = Entry(frame1, bd="5")
    meat = Entry(frame1, bd="5")
    tea = Entry(frame1, bd="5")
    # Food_item_Entry_Close
    # Frame_1_objects
    drink.place(x=130, y=35)
    drink.insert(0, 0)  # insert 0 as default value
    chapati.place(x=130, y=80)
    chapati.insert(0, 0)  # insert 0 as default value
    mandazi.place(x=130, y=125)
    mandazi.insert(0, 0)  # insert 0 as default value
    sukuma.place(x=130, y=170)
    sukuma.insert(0, 0)  # insert 0 as default value
    ugali.place(x=130, y=215)
    ugali.insert(0, 0)  # insert 0 as default value
    hekes.place(x=130, y=260)
    hekes.insert(0, 0)  # insert 0 as default value
    meat.place(x=130, y=305)
    meat.insert(0, 0)  # insert 0 as default value
    tea.place(x=130, y=350)
    tea.insert(0, 0)  # insert 0 as default value
    # Food_item_Label_Created
    # Frame1_objects food frame
    drink_label = Label(frame1, text="Soft Drink", font="arial 12 bold ", bg="#ED420B")

    chapati_label = Label(frame1, text="Chapati", font="arial 12 bold", bg="#ED420B")
    mandazi_label = Label(frame1, text="Mandazi", font="arial 12 bold", bg="#ED420B")
    sukuma_label = Label(frame1, text="Sukuma", font="arial 12 bold", bg="#ED420B")
    ugali_label = Label(frame1, text="Ugali", font="arial 12 bold ", bg="#ED420B")
    hekes_label = Label(frame1, text="Hekes", font="arial 12 bold", bg="#ED420B")
    meat_label = Label(frame1, text="Meat", font="arial 12 bold ", bg="#ED420B")
    tea_label = Label(frame1, text="Tea", font="arial 12 bold ", bg="#ED420B")
    # Food_item_Label_Close
    drink_label.place(x=10, y=35)
    chapati_label.place(x=10, y=80)
    mandazi_label.place(x=10, y=125)
    sukuma_label.place(x=10, y=175)
    ugali_label.place(x=10, y=215)
    hekes_label.place(x=10, y=260)
    meat_label.place(x=10, y=305)
    tea_label.place(x=10, y=350)
    # -------------------------------------------------------------------------
    """"
        Calculator Module

    """
    from tkinter import messagebox

    val = ""
    A = 0
    operator = ""

    def btn_1_isclicked():
        global val
        val = val + "1"
        data.set(val)

    def btn_2_isclicked():
        global val
        val = val + "2"
        data.set(val)

    def btn_3_isclicked():
        global val
        val = val + "3"
        data.set(val)

    def btn_4_isclicked():
        global val
        val = val + "4"
        data.set(val)

    def btn_5_isclicked():
        global val
        val = val + "5"
        data.set(val)

    def btn_6_isclicked():
        global val
        val = val + "6"
        data.set(val)

    def btn_7_isclicked():
        global val
        val = val + "7"
        data.set(val)

    def btn_8_isclicked():
        global val
        val = val + "8"
        data.set(val)

    def btn_9_isclicked():
        global val
        val = val + "9"
        data.set(val)

    def btn_0_isclicked():
        global val
        val = val + "0"
        data.set(val)

    def btn_plus_isclicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "+"
        val = val + "+"
        data.set(val)

    def btn_min_isclicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "-"
        val = val + "-"
        data.set(val)

    def btn_mult_isclicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "*"
        val = val + "*"
        data.set(val)

    def btn_div_isclicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "/"
        val = val + "/"
        data.set(val)

    def btn_c_isclicked():
        global A
        global operator
        global val
        A = 0
        operator = ""
        val = ""
        data.set(val)

    def result():
        global A
        global operator
        global val
        val2 = val
        if operator == "+":
            B = int((val2.split("+")[1]))
            C = A + B
            data.set(C)
            val = str(C)
        elif operator == "-":
            B = int((val2.split("-")[1]))
            C = A - B
            data.set(C)
            val = str(C)
        elif operator == "*":
            B = int((val2.split("*")[1]))
            C = A * B
            data.set(C)
            val = str(C)
        elif operator == "/":
            B = int((val2.split("/")[1]))
            if B == 0:
                messagebox.showerror("Error", "Divisible by 0 not allowed.")
                A = ""
                val = ""
                data.set(val)
            else:
                C = int(A / B)
                data.set(C)
                val = str(C)

    data = StringVar()
    lbl = Label(cal_frame, text="LABEL", anchor=SE,
                font=("Verdana", 20),
                textvariable=data,
                background="#ffffff",
                fg="#000000"
                )
    lbl.pack(expand=True, fill="both")
    btnrow1 = Frame(cal_frame, bg="#000000")
    btnrow1.pack(expand=True, fill="both")
    btnrow2 = Frame(cal_frame)
    btnrow2.pack(expand=True, fill="both")
    btnrow3 = Frame(cal_frame)
    btnrow3.pack(expand=True, fill="both")
    btnrow4 = Frame(cal_frame)
    btnrow4.pack(expand=True, fill="both")
    btn7 = Button(btnrow1, text="7", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_1_isclicked)
    btn7.pack(side=LEFT, expand=True, fill="both")
    btn8 = Button(btnrow1, text="8", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_2_isclicked)
    btn8.pack(side=LEFT, expand=True, fill="both")
    btn9 = Button(btnrow1, text="9", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_3_isclicked)
    btn9.pack(side=LEFT, expand=True, fill="both")
    btnplus = Button(btnrow1, text="+", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_plus_isclicked)
    btnplus.pack(side=LEFT, expand=True, fill="both")
    btn4 = Button(btnrow2, text="4", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_4_isclicked)
    btn4.pack(side=LEFT, expand=True, fill="both")
    btn5 = Button(btnrow2, text="5", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_5_isclicked)
    btn5.pack(side=LEFT, expand=True, fill="both")
    btn6 = Button(btnrow2, text="6", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_6_isclicked)
    btn6.pack(side=LEFT, expand=True, fill="both")
    btnminus = Button(btnrow2, text="-", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_min_isclicked)
    btnminus.pack(side=LEFT, expand=True, fill="both")
    btn1 = Button(btnrow3, text="1", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_1_isclicked)
    btn1.pack(side=LEFT, expand=True, fill="both")
    btn2 = Button(btnrow3, text="2", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_2_isclicked)
    btn2.pack(side=LEFT, expand=True, fill="both")
    btn3 = Button(btnrow3, text="3", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_3_isclicked)
    btn3.pack(side=LEFT, expand=True, fill="both")
    btnmult = Button(btnrow3, text="*", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_mult_isclicked)
    btnmult.pack(side=LEFT, expand=True, fill="both")
    btnc = Button(btnrow4, text="C", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_c_isclicked)
    btnc.pack(side=LEFT, expand=True, fill="both")
    btn0 = Button(btnrow4, text="0", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_0_isclicked)
    btn0.pack(side=LEFT, expand=True, fill="both")
    btnequal = Button(btnrow4, text="=", font=("Verdana", 22), relief=GROOVE, border=0, command=result)
    btnequal.pack(side=LEFT, expand=True, fill="both")
    btndiv = Button(btnrow4, text="/", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_div_isclicked)
    btndiv.pack(side=LEFT, expand=True, fill="both")
    heading1.place(x=350, y=10)
    heading2.place(x=400, y=80)
    root.mainloop()


"""
---------------------------------------------------------------------------------------------------
   ADMIN CODE
   Admin functionality 
   Admin graphical user interface
   -------------------------------------------------------------------------------------------------
"""


def admin_functionality():
    window.quit()
    window.iconify()
    window.deiconify()
    rt = Toplevel()
    rt.geometry("1000x800")
    rt.maxsize(1000, 800)
    rt.minsize(400, 200)
    rt.config(bg="red4")
    rt.title("ADMIN OPERATIONS")

    label1 = Label(rt, text="SEKU_TUCK_HOTEL", bd=0, width=100, height=3, bg="red", font="arial 12 bold",
                   anchor=CENTER, relief=SUNKEN)
    label2 = Label(rt, text="ADMINISTRATOR SITE", width=100, height=3, bd=0, bg="red", font="arial 12 bold",
                   relief=SUNKEN)

    label1.place(x=10, y=4)
    label2.place(x=10, y=55)

    frame0 = LabelFrame(rt, bg="green", width=50, height=100)
    frame1 = LabelFrame(rt, bg="green", width=50, height=100)
    frame3 = LabelFrame(rt, bg="green", width=100, height=100)
    time_frame = LabelFrame(rt, bg="red4", width=10, height=100)

    frame0.place(x=20, y=140)
    frame1.place(x=500, y=140)
    frame3.place(x=200, y=500)
    time_frame.place(x=11, y=6)

    # listboxes and Buttons in frame0
    list_box1 = Listbox(frame0, bg="yellow", bd=5, justify=LEFT, height=15)
    list_box1.pack(side=RIGHT, expand="true", fill="both", padx=3)
    list_box2 = Listbox(frame0, bg="yellow", bd=5, justify=RIGHT, height=15)
    list_box2.pack(side=RIGHT, expand="true", fill="both", padx=3)

    # Scale widget

    myscale = Scale(frame0, from_=1, to=15,length=250,bd=1,bg="black",activebackground="red")
    myscale.pack()

    btn_generate1 = Button(rt, text="orders", height=2, fg="black", bg="red4", font="arial 12 bold", relief=RAISED,
                           justify=LEFT)
    btn_generate2 = Button(rt, text="transactions", height=2, fg="black", bg="red4", font="arial 12 bold",
                           relief=RAISED, justify=RIGHT)
    btn_generate3 = Button(rt, text="payments", height=2, fg="black", bg="red4", font="arial 12 bold",
                           relief=RAISED, justify=LEFT)
    btn_generate4 = Button(rt, text="Tables", height=2, fg="black", bg="red4", font="arial 12 bold", relief=RAISED,
                           justify=RIGHT)
    btn_generate1.place(x=50, y=400)
    btn_generate2.place(x=200, y=400)
    btn_generate3.place(x=490, y=400)
    btn_generate4.place(x=600, y=400)

    # listboxes and textboxes in frame1
    listbx1 = Listbox(frame1, bg="yellow", bd=5, height=15)
    listbx2 = Listbox(frame1, bg="yellow", bd=5, height=15)
    listbx1.pack(side=LEFT, expand="true", fill="both", padx=3)
    listbx2.pack(side=RIGHT, expand="true", fill="both", padx=3)

    # Frame3
    listbx3 = Listbox(frame3, bd=2, bg="blue", width=100)
    listbx3.grid(row=0, column=0, columnspan=2)

    def clock():
        current = time.strftime("%H:%M:%S")
        time_label["text"] = current
        rt.after(1000, clock)

    # Time label in time_Frame
    time_label = Label(time_frame, height=2, fg="black", bg="red4", font="arial 12 bold", relief=SUNKEN)
    time_label.pack()
    clock()

    def quit():
        rt.destroy()
        window.deiconify

    btn_exit = Button(rt, text="LOG OUT", activebackground="red", bg="red", width=15, height=2, command=quit)
    btn_exit.place(x=600, y=460)

    # frames
    # 3 frames

    rt.mainloop()


# USERS BUTTONS
btn_customer = Button(frame_window, text="CUSTOMER LOGIN", bd=2, activebackground="blue", bg="yellow",
                      command=Customer_fun)
btn_admin = Button(frame_window, text="ADMIN", bd=2, activebackground="blue", bg="yellow", command=admin_functionality)

lbl_1.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="enw")
lbl_2.grid(row=1, column=0, padx=5, pady=5, sticky="enw")
lbl_3.grid(row=2, column=0, padx=5, pady=5)
lbl_4.grid(row=3, column=0, pady=5, padx=5)

btn_customer.grid(row=2, column=1, rowspan=2, columnspan=2, padx=5, pady=5)
btn_admin.grid(row=3, column=1, rowspan=2, columnspan=2, padx=5, pady=5)

window.mainloop()
