import tkinter as tk
from tkinter import ttk

def chk_p():
    with open("p.txt", "r") as f:
        c = f.read()
        if c.strip() != '':
            w = tk.Toplevel(root)
            w.title("Urgente!")
            w.configure(bg='gray0')
            m = tk.Label(w, text="Tienes tareas pendientes!!!", padx=10, pady=10)
            m.configure(bg='gray0', fg='gray99')
            m.pack()
            w.attributes("-topmost", True)

def ord(f):
    with open(f, 'r') as r:
        ls = r.readlines()

    lalta = [line for line in ls if "Alta" in line]
    ledia = [line for line in ls if "Media" in line]
    laja = [line for line in ls if "Baja" in line]

    orl = lalta + ledia + laja

    with open(f, 'w') as r:
        r.writelines(orl)

def addt(task, entry, priority, cbbox):
    if task:
        with open("p.txt", "a") as p:
            p.write(task + "`~^_=<<&;" + priority + "\n")
        msgw = tk.Toplevel()
        msgw.title("Añadir Tarea")
        msgw.configure(bg='gray0')
        msg = tk.Label(msgw, text="Tarea añadida!", padx=100, pady=10)
        msg.configure(bg='gray0', fg='gray99')
        msg.pack()
        entry.delete(0, tk.END)
        cbbox.set('')
        ord("p.txt")
        
def addt_w():
    combostyle = ttk.Style()
    if 'combostyle' not in combostyle.theme_names():
        combostyle.theme_create('combostyle', parent='alt',
                            settings = {'TCombobox':
                                        {'configure':
                                        {'selectbackground': 'black',
                                        'fieldbackground': 'black',
                                        'background': 'HotPink1'
                                        }}}
                            )

        combostyle.theme_use('combostyle') 

    aw = tk.Toplevel(root)
    aw.title("Añadir Tarea")
    aw.geometry("300x200")
    aw.configure(bg='gray0')

    f = tk.Frame(aw)
    f.configure(bg="gray0")
    f.pack(padx=5, pady=5)

    uin_l = tk.Label(f, text="Tarea:")
    uin_l.configure(fg='gray99', bg='black')
    uin_l.pack(side=tk.LEFT)

    uin_box = tk.Entry(f, width=100)
    uin_box.configure(bg='gray0', fg='gray99')
    uin_box.pack(side=tk.LEFT, pady=5, padx=5)

    g = tk.Frame(aw)
    g.configure(bg="gray0")
    g.pack(padx=5, pady=5)

    pri = tk.Label(g, text="Prioridad:")
    pri.configure(fg='gray99', bg='black')
    pri.pack(side=tk.LEFT)

    options = ("Alta", "Media", "Baja")
    sel_o = tk.StringVar(value=options[0])
    o_menu = ttk.Combobox(g, textvariable=sel_o, values=options, state='readonly')
    o_menu.pack(side=tk.LEFT, pady=5, padx=5)

    uin_b = tk.Button(aw, text="Anadir", border=2, command=lambda: addt(uin_box.get(), uin_box, o_menu.get(), o_menu))
    uin_b.configure(bg='HotPink1', fg='gray11')
    uin_b.pack()

def u_tl(lb, file):
    lb.delete(0, tk.END)
    try:
        with open(file, "r") as p:
            tasks = p.readlines()
            for t in tasks:
                t = t.strip().replace('`~^_=<<&;', ' | ')
                lb.insert(tk.END, t)
    except FileNotFoundError:
        pass

def fint_w():
    fw = tk.Toplevel(root)
    fw.title("Terminar Tarea")
    fw.geometry("300x300")
    fw.configure(bg='gray0')

    label = tk.Label(fw, text="Selecciona la tarea que quieras terminar:", font=("Arial", 10))
    label.configure(fg='DeepPink2', bg='black')
    label.pack(pady=15)

    t_l = tk.Listbox(fw, width=40, selectmode=tk.SINGLE)
    t_l.configure(bg='black', fg='pink')
    t_l.pack(pady=10, padx=5)
    u_tl(t_l, "p.txt")

    fint_btn = tk.Button(fw, text="Terminar Tarea", border=2, command=lambda: fint(t_l))
    fint_btn.configure(bg='HotPink1', fg='gray11')
    fint_btn.pack()

def fint(t_lb):
    sel_t = t_lb.curselection()
    if sel_t:
        t_i = sel_t[0]
        t = t_lb.get(t_i)
        t_lb.delete(t_i)

        with open("p.txt", "r") as p:
            tasks = p.readlines()

        with open("p.txt", "w") as p:
            for task in tasks:
                if task.strip().replace('`~^_=<<&;', ' | ') != t:
                    p.write(task)
                else:
                    with open("f.txt", "a") as f:
                        f.write(task)

def show_p():
    sw = tk.Toplevel(root)
    sw.title("Mostrar Pendientes")
    sw.geometry("300x300")
    sw.configure(bg='gray0')

    label = tk.Label(sw, text="Tareas Pendientes:", font=("Arial", 10))
    label.configure(fg='DeepPink2', bg='black')
    label.pack(pady=15)

    t_l = tk.Listbox(sw, width=40, selectmode=tk.SINGLE)
    t_l.configure(bg='black', fg='pink')
    t_l.pack(pady=10, padx=5)
    u_tl(t_l, "p.txt")

def show_f():
    sfw = tk.Toplevel(root)
    sfw.title("Mostrar Pendientes")
    sfw.geometry("300x300")
    sfw.configure(bg='gray0')

    label = tk.Label(sfw, text="Tareas Finalizadas:", font=("Arial", 10))
    label.configure(fg='DeepPink2', bg='black')
    label.pack(pady=15)

    t_l = tk.Listbox(sfw, width=40, selectmode=tk.SINGLE)
    t_l.configure(bg='black', fg='pink')
    t_l.pack(pady=10, padx=5)
    u_tl(t_l, "f.txt")

def clear(file):
    open(file, "w")
    mw = tk.Toplevel()
    mw.title("Borrar Tareas")
    mw.configure(bg='gray0')
    m = tk.Label(mw, text="Tareas borradas exitosamente.", padx=10, pady=10)
    m.configure(bg='gray0', fg='gray99')
    m.pack()

def del_tks_w():
    delw = tk.Toplevel(root)
    delw.title("Borrar Tareas")
    delw.geometry("300x100")
    delw.configure(bg='gray0')

    f = tk.Frame(delw)
    f.configure(bg="gray0")
    f.pack(padx=5, pady=5)

    delp_btn = tk.Button(delw, text="Borrar Pendientes", border=2, command=lambda: clear("p.txt"))
    delp_btn.configure(bg='HotPink1', fg='gray11')
    delp_btn.pack(side=tk.LEFT, padx=30)

    delf_btn = tk.Button(delw, text="Borrar Finalizadas", border=2, command=lambda: clear("f.txt"))
    delf_btn.configure(bg='HotPink1', fg='gray11')
    delf_btn.pack(side=tk.LEFT)


root = tk.Tk()
root.title("Gestionador de Tareas")
root.configure(bg='gray0')
root.geometry("300x300")

title = tk.Label(text="Gestionador de Tareas", font=("Arial", 18))
title.configure(fg='DeepPink2', bg='black')
title.pack(pady=1)

stitle = tk.Label(text="Que deseas hacer?", font=("Arial", 10))
stitle.configure(bg='black', fg='DeepPink2')
stitle.pack(pady=1)

addt_btn = tk.Button(text="Añadir Tarea", border=2, command=addt_w)
addt_btn.configure(fg='DeepPink2', bg='black')
addt_btn.pack(pady=5, padx=15)

fint_btn = tk.Button(text="Terminar Tarea", border=2, command=fint_w)
fint_btn.configure(fg='DeepPink2', bg='black')
fint_btn.pack(pady=5, padx=15)

shp_btn = tk.Button(text="Mostrar Pendientes", border=2, command=show_p)
shp_btn.configure(fg='DeepPink2', bg='black')
shp_btn.pack(pady=5, padx=15)

shf_btn = tk.Button(text="Mostrar Finalizadas", border=2, command=show_f)
shf_btn.configure(fg='DeepPink2', bg='black')
shf_btn.pack(pady=5, padx=15)

deltks_btn = tk.Button(text="Borrar Tareas", border=2, command=del_tks_w)
deltks_btn.configure(fg='DeepPink2', bg='black')
deltks_btn.pack(pady=5, padx=15)

chk_p()

root.mainloop()