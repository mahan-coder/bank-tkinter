from tkinter import *
from tkinter import ttk
import json
import string

#222831               
#393E46
#00ADB5
#EEEEEE

#F9ED69
#F08A5D
#B83B5E
#6A2C70

#000000
#1A4D2E
#FF9F29
#FAF3E3


window = Tk()
window.resizable(False,False)

def chek_save():
    global name
    global last_name
    global credit
    global password
    global phone_number
    x =1
    valid_numbers=['1','2','3','4','5','6','7','8','9','0']
    can_pass = True
    name = entry_name.get()
    last_name = entry_last.get()
    credit = entry_cerdit.get()
    password = entry_password.get()
    phone_number = entry_phone.get()
    
    
    for i in password :
        if i not in valid_numbers or  len(password)!=4:
            can_pass = False
            entry_password.delete(0,END)
            global eror8
            eror8= Label(window,background='#222831',text='Invalid Password ',fg='#ff726f',font=('Arial',11))
            eror8.place(x=465,y=375)
            break
        else:
            try:
                eror8.destroy()
                can_pass = True
            except NameError:
                can_pass = True
                pass
            
            
        
    
    
    
    
    for i in last_name :
        if i not in string.ascii_lowercase and i not in string.ascii_uppercase or len(last_name)<3 :
            can_pass =False
            entry_last.delete(0,END)
            global eror6
            eror6 = Label(window,background='#222831',text='Invalid Last Name ',fg='#ff726f',font=('Arial',11))
            eror6.place(x=465,y=175)
            break
        else:
            try:
                eror6.destroy()
                can_pass = True
            except NameError:
                can_pass = True
                pass
            
   
    
    
    
    
    
    
    for i in credit :
        if i not in valid_numbers or len(credit) != 16 :
            can_pass = False
            entry_cerdit.delete(0,END)
            global eror4
            eror4= Label(window,background='#222831',text='Invalid credit number ',fg='#ff726f',font=('Arial',11))
            eror4.place(x=465,y=275)
            break
        else:
            try:
                eror4.destroy()
                can_pass =True
            except NameError:
                can_pass = True
                pass
    
    
    
    for i in name :
        if i not in string.ascii_lowercase and i not in string.ascii_uppercase or len(name)<3 :
            can_pass = False
            entry_name.delete(0,END)
            global eror5
            eror5 = Label(window,background='#222831',text='Invalid Name ',fg='#ff726f',font=('Arial',11))
            eror5.place(x=465,y=75)
            break
        else:
            try:
                eror5.destroy()
                can_pass = True
            except NameError:
                can_pass = True
                pass
            
    
        
    for i in phone_number :
        if i not in valid_numbers or phone_number.startswith('0')== False or phone_number[1]!='9'or len(phone_number)!=11:
            can_pass = False
            entry_phone.delete(0,END)
            global eror3
            eror3= Label(window,background='#222831',text='Invalid phone number ',fg='#ff726f',font=('Arial',11))
            eror3.place(x=465,y=475)
            break
        else:
            try:
                eror3.destroy()
            except NameError:
                can_pass = True
                pass
    
    
    if phone_number.startswith('0')== False or phone_number[1]!='9'or len(phone_number)!=11 or  len(credit) > 16 or len(credit)<16 or len(name)<3 or  len(password)!=4 or len(last_name)<3 or can_pass == False :
        pass
    else:
        # with open('data.json','w') as file :
        #     id_1 = json.dumps(diction,indent=4)
        #     file.write(id_1)
        #     file.close()
        user_1 = {}
        user_1['name'] = name
        user_1['last_name'] = last_name
        user_1['cerdit number'] = credit
        user_1['phone number'] = phone_number
        user_1['password'] = password
        user_1['budget'] = 100_000_000
    
        new_window=Toplevel(window)
        new_window.title('main')
        new_window.geometry('2000x2000')
        new_window.configure(bg='#F6F5F5' )
        new_window.iconbitmap(f'icons/bank (1).ico')


        def chekker():
            global pass_label
            global cerdit_label
            global new_pass_label
            global new_cerdit_label
            a=chek_var1.get()
            b=chek_var2.get()

            if a == 'yes':
                pass_label.destroy()
                new_pass_label = Label(new_window,background='#1687A7',text='Password : ****',fg='#E3FDFD',border=1,font=('Arial',15))
                new_pass_label.place(x=15,y=270)
            if a == 'no':
                new_pass_label.destroy()
                pass_label = Label(new_window,background='#1687A7',text=f'Password {password}',fg='#E3FDFD',border=1,font=('Arial',15))
                pass_label.place(x=15,y=270)
                
            if b == 'yes':
                cerdit_label.destroy()
                new_cerdit_label = Label(new_window,background='#1687A7',text='Credit : ***************',fg='#E3FDFD',border=1,font=('Arial',15))
                new_cerdit_label.place(x=15,y=200)
            if b == 'no':
                new_cerdit_label.destroy()
                cerdit_label = Label(new_window,background='#1687A7',text=f'Credit : {credit}',fg='#E3FDFD',border=1,font=('Arial',15))
                cerdit_label.place(x=15,y=200)
                

        label_7 = Label(new_window,background='#1687A7',width=40,height=35)
        label_7.place(x=2,y=4)
                
        label_8 = Label(new_window,background='#1687A7',width=40,height=10)
        label_8.place(x=2,y=540)

        label_9 = Label(new_window,background='#1687A7',width=70,height=50)
        label_9.place(x=293,y=4)

        label_10 = Label(new_window,background='#1687A7',width=79,height=50)
        label_10.place(x=795,y=4)

        info_label = Label(new_window,background='#1687A7',text='YOUR INFORMATION',fg='#E3FDFD',border=1,font=('Arial',16))
        info_label.place(x=40,y=4)

        name_label = Label(new_window,background='#1687A7',text=f'Name :  {name}',fg='#E3FDFD',border=1,font=('Arial',15))
        name_label.place(x=15,y=60)

        last_name_label = Label(new_window,background='#1687A7',text=f'Last Name : {last_name}',fg='#E3FDFD',border=1,font=('Arial',15))
        last_name_label.place(x=15,y=130)
        global cerdit_label
        cerdit_label = Label(new_window,background='#1687A7',text=f'Cerdit : {credit}',fg='#E3FDFD',border=1,font=('Arial',15))
        cerdit_label.place(x=15,y=200)
        
        global pass_label
        pass_label = Label(new_window,background='#1687A7',text=f'Password :  {password}',fg='#E3FDFD',border=1,font=('Arial',15))
        pass_label.place(x=15,y=270)

        phone_label = Label(new_window,background='#1687A7',text=f'Phone : {phone_number}',fg='#E3FDFD',border=1,font=('Arial',15))
        phone_label.place(x=15,y=340)

        chek_var1 = StringVar(new_window,value='')
        chek_1 = Checkbutton(new_window,text='Hide Password',background='#1687A7',fg='#E3FDFD',border=1,font=('Arial',15),variable=chek_var1,onvalue='yes',offvalue='no',command=chekker)
        chek_1.deselect()
        chek_1.place(x=15,y=410)

        chek_var2 = StringVar(new_window,value='')
        chek_2 = Checkbutton(new_window,text='Hide Credit',background='#1687A7',fg='#E3FDFD',border=1,font=('Arial',15),variable=chek_var2,onvalue='yes',offvalue='no',command=chekker)
        chek_2.deselect()
        chek_2.place(x=15,y=480)

        dummy_1 = {}
        dummy_1['name'] = 'mahan'
        dummy_1['last_name'] = 'ansari'
        dummy_1['cerdit number'] = '3333333333333333'
        dummy_1['phone number'] = '09111111111'
        dummy_1['password'] = '7777'
        dummy_1['budget'] = 100

        dummy_2 = {}
        dummy_2['name'] = 'dummy2'
        dummy_2['last_name'] = 'Bot'
        dummy_2['cerdit number'] = '2222222222222222'
        dummy_2['phone number'] = '09000000000'
        dummy_2['password'] = '6666'
        dummy_2['budget'] = 500_000
        
        

        label_11 = Label(new_window,text='Your Budget is',background='#1687A7',width=20,fg='#E3FDFD',font=('Arial',25))
        label_11.place(x=350,y=4)

        global label_12
        label_12 = Label(new_window,text=f'{user_1["budget"]}$',background='#1687A7',width=16,fg='#E3FDFD',font=('Arial',28))
        label_12.place(x=360,y=170)
                
        label_13 = Label(new_window,background='#1687A7',text=f'Dear {user_1["name"]} :',width=10,fg='#E3FDFD',font=('Arial',17))
        label_13.place(x=300,y=100)

        label_14 = Label(new_window,background='#1687A7',text=f'Your Inventory Is :',width=15,fg='#E3FDFD',font=('Arial',17))
        label_14.place(x=293,y=130)

        label_13 = Label(new_window,background='#276678',width=70,height=26)
        label_13.place(x=293,y=300)

        label_15 = Label(new_window,background='#276678',text=f'Availabel Acounts ',width=15,fg='#E3FDFD',font=('Arial',22))
        label_15.place(x=420,y=310)

        label_16 = Label(new_window,background='#276678',text=f'dummy1 ',width=15,fg='#E3FDFD',font=('Arial',22))
        label_16.place(x=420,y=360)

        label_17 = Label(new_window,background='#276678',text=f'dummy2 ',width=15,fg='#E3FDFD',font=('Arial',22))
        label_17.place(x=420,y=410)

        label_18 = Label(new_window,background='#276678',text=f'Contact : 02144321090 ',width=20,fg='#E3FDFD',font=('Arial',22))
        label_18.place(x=385,y=640)

        label_19 = Label(new_window,background='#276678',text=f'Email : Mbank@gmail.com  ',width=21,fg='#E3FDFD',font=('Arial',22))
        label_19.place(x=385,y=580)

        # label_20 = Label(new_window,background='#777777',width=70,height=1)
        # label_20.place(x=293,y=500)

        label_21 = Label(new_window,background='#1687A7',text=f'Transfer',width=21,fg='#E3FDFD',font=('Arial',22))
        label_21.place(x=920,y=4)

        label_22 = Label(new_window,background='#1687A7',text=f'Password :',width=9,fg='#E3FDFD',font=('Arial',15))
        label_22.place(x=800,y=70)

        label_23 = Label(new_window,background='#1687A7',text=f'To(name) :',width=9,fg='#E3FDFD',font=('Arial',15))
        label_23.place(x=800,y=140)

        label_24 = Label(new_window,background='#1687A7',text=f'Price :',width=9,fg='#E3FDFD',font=('Arial',16))
        label_24.place(x=800,y=210)

        label_24 = Label(new_window,background='#1687A7',text=f'Credit :',width=9,fg='#E3FDFD',font=('Arial',16))
        label_24.place(x=800,y=280)

        entry_password2 = Entry(new_window,background='#E8F3D6',relief='flat',fg='black',width=25,font=('Arial',16))
        entry_password2.place(x=910,y=70,height=34)

        entry_to = Entry(new_window,background='#E8F3D6',relief='flat',fg='black',width=25,font=('Arial',16))
        entry_to.place(x=910,y=140,height=34)

        entry_price = Entry(new_window,background='#E8F3D6',relief='flat',fg='black',width=25,font=('Arial',16))
        entry_price.place(x=910,y=210,height=34)

        entry_credit2 = Entry(new_window,background='#E8F3D6',relief='flat',fg='black',width=25,font=('Arial',16))
        entry_credit2.place(x=910,y=280,height=34)

        def transfer():
            global label_12
            ent_pass=entry_password2.get()
            ent_price=entry_price.get()
            ent_to=entry_to.get()
            ent_credit=entry_credit2.get()
            
            
            
            if ent_pass == user_1['password'] and int(ent_price) < user_1['budget']:
                if ent_to =='dummy1' and ent_credit=='3333333333333333':
                    user_1['budget']-=int(ent_price)
                    dummy_1['budget']+=int(ent_price)
                    entry_password2.delete(0,END)
                    entry_price.delete(0,END)
                    entry_to.delete(0,END)
                    entry_credit2.delete(0,END)
                    label_12.destroy()
                    label_12 = Label(new_window,text=f'{user_1["budget"]}$',background='#1687A7',width=16,fg='#E3FDFD',font=('Arial',28))
                    label_12.place(x=360,y=170)
                    
                    entry_credit2.insert(0,'sucssefull')
                    entry_password2.insert(0,'sucssefull')
                    entry_price.insert(0,'sucssefull')
                    entry_to.insert(0,'sucssefull')
                elif ent_to=='dummy2' and ent_credit == '2222222222222222':
                    user_1['budget']-=int(ent_price)
                    dummy_2['budget']+=int(ent_price)
                    entry_password2.delete(0,END)
                    entry_price.delete(0,END)
                    entry_to.delete(0,END)
                    entry_credit2.delete(0,END)
                    label_12.destroy()
                    label_12 = Label(new_window,text=f'{user_1["budget"]}$',background='#1687A7',width=16,fg='#E3FDFD',font=('Arial',28))
                    label_12.place(x=360,y=170)
                    
                    entry_credit2.insert(0,'sucssefull')
                    entry_password2.insert(0,'sucssefull')
                    entry_price.insert(0,'sucssefull')
                    entry_to.insert(0,'sucssefull')
            
                    
                    
                    
                    
            if ent_pass != user_1['password']:
                entry_password2.delete(0,END)
                entry_password2.insert(0,'Invalid')
            try:
                if int(ent_price) > user_1['budget']:
                    ent_price = entry_price.get()
                    if ent_price != 'sucssefull':
                        entry_price.delete(0,END)
                        entry_price.insert(0,'Invalid')
            except ValueError :
                    entry_price.delete(0,END)
                    entry_price.insert(0,'Invalid')
            if ent_to =='dummy1':
                if ent_credit != '3333333333333333':
                    entry_credit2.delete(0,END)
                    entry_credit2.insert(0,'Invalid')
                    
            elif ent_to =='dummy2':
                if ent_credit != '2222222222222222':
                    entry_credit2.delete(0,END)
                    entry_credit2.insert(0,'Invalid')
                    
                    
            else:
                    entry_credit2.delete(0,END)
                    entry_to.delete(0,END)
                    entry_credit2.insert(0,'Invalid')
                    entry_to.insert(0,'Invalid')
                    
            
                    
                    
                    
                    
                    
                    

            
                

        button_transfer = Button(new_window,text='Transfer',width=25,background='#68B984',relief='flat',font=('Arial',16),fg='#E3FDFD',command=transfer)
        button_transfer.place(x=910,y=350,height=73)

#999999,#777777,#555555,#333333,#111111










        new_window.mainloop()
        


       
       
        
    



window.geometry('606x800')
# window.resizable(False,False)
window.title('my bank')


label_1 = Label(window,background='#222831',width=1200,height=100)
label_1.place(x=0,y=0)




label_2 = Label(window,background='#222831',width=90,height=90)
label_2.place(x=6,y=21)

label_3 = Label(window,background='#222831',text='Wellcom to Mbank',font=('Arial',20),fg='#EEEEEE')
label_3.place(x=200,y=21)

label_4 = Label(window,bg='#222831',text='Name :',font=('Arial',15),fg='#00ADB5')
label_4.place(x=20,y=72)

label_5 = Label(window,bg='#222831',text='Last Name :',font=('Arial',15),fg='#00ADB5')
label_5.place(x=20,y=172)

label_6 = Label(window,bg='#222831',text='Credit Number :',font=('Arial',15),fg='#00ADB5')
label_6.place(x=20,y=272)

label_6 = Label(window,bg='#222831',text='Password :',font=('Arial',15),fg='#00ADB5')
label_6.place(x=20,y=372)

label_6 = Label(window,bg='#222831',text='Phone Number :',font=('Arial',15),fg='#00ADB5')
label_6.place(x=20,y=472)

entry_name = Entry(window,bg='#393E46',fg='#EEEEEE',width=45,relief='flat')
entry_name.place(x=180,y=70,height=35)

entry_last = Entry(window,bg='#393E46',fg='#EEEEEE',width=45,relief='flat')
entry_last.place(x=180,y=170,height=35)

entry_cerdit = Entry(window,bg='#393E46',fg='#EEEEEE',width=45,relief='flat')
entry_cerdit.place(x=180,y=270,height=35)

entry_password = Entry(window,bg='#393E46',fg='#EEEEEE',width=45,relief='flat')
entry_password.place(x=180,y=370,height=35)

entry_phone = Entry(window,bg='#393E46',fg='#EEEEEE',width=45,relief='flat')
entry_phone.place(x=180,y=470,height=35)

button_1 = Button(window,text='Sign In',bg='#00ADB5',fg='#EEEEEE',width=16,height=1,relief='flat',font=('Arial',20),activebackground='#1687A7',activeforeground='#EEEEEE',command=chek_save)
button_1.place(x=186,y=545)
# print(button_1.winfo_exists())
# entry_4 = Entry(window,bg='#393E46',fg='#EEEEEE',width=45,relief='flat')
# entry_4.place(x=180,y=120,height=35)

# entry_5 = Entry(window,bg='#393E46',fg='#EEEEEE',width=45,relief='flat')
# entry_5.place(x=180,y=120,height=35)








window.mainloop()