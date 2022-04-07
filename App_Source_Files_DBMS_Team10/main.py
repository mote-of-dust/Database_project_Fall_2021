from tkinter import *
import tkinter.ttk
from utils.SQLUtil import SqlUtil

# setting a base/initial sql query string
search_str = 'select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, ' \
             'setrarity.rName from card, setrarity, typegen where card.SRAK = setrarity.SRAK and card.TAK = ' \
             'typegen.TAK; '

# initializing a Tkinter object, which created our basic frame.
base = Tk()
base.title("Gotta catch 'em all!")
base.geometry("410x300")


# function for inserting a new card.
def new_card():
    popup = Toplevel()
    popup.geometry("500x300")

    clicked = IntVar()
    clicked.set(1)
    set_clicked = IntVar()
    set_clicked.set(1)
    type_clicked = StringVar()
    type_clicked.set('Psychic')
    rar_clicked = StringVar()
    rar_clicked.set("Common")

    def get_TAK(clicked_var, type_var):
        TAK = 0
        if clicked_var == 1:
            if type_var == 'Water':
                TAK = 1
            elif type_var == 'Fire':
                TAK = 2
            elif type_var == 'Fighting':
                TAK = 3
            elif type_var == 'Colorless':
                TAK = 4
            elif type_var == 'Lightning':
                TAK = 5
            elif type_var == 'Grass':
                TAK = 6
            elif type_var == 'Psychic':
                TAK = 7
        elif clicked_var == 2:
            if type_var == 'Darkness':
                TAK = 8
            elif type_var == 'Water':
                TAK = 9
            elif type_var == 'Fire':
                TAK = 10
            elif type_var == 'Fighting':
                TAK = 11
            elif type_var == 'Colorless':
                TAK = 12
            elif type_var == 'Lightning':
                TAK = 13
            elif type_var == 'Metal':
                TAK = 14
            elif type_var == 'Grass':
                TAK = 15
            else:
                TAK = 16
        return TAK

    def get_SRAK(set_var, rar_var):
        SRAK = 0
        if set_var == 1:
            if rar_var == 'Common':
                SRAK = 1
            elif rar_var == 'Uncommon':
                SRAK = 2
            elif rar_var == 'Rare':
                SRAK = 3
        elif set_var == 8:
            if rar_var == 'Common':
                SRAK = 4
            elif rar_var == 'Uncommon':
                SRAK = 5
            elif rar_var == 'Rare':
                SRAK = 6
        return SRAK

    def insert_func():
        global search_str

        clicked_var = clicked.get()
        set_var = set_clicked.get()
        type_var = type_clicked.get()
        name_var = name_entry.get()
        cnum_var = cnum_entry.get()
        hp_var = hp_entry.get()
        retreat_var = retreat_entry.get()
        rar_var = rar_clicked.get()

        TAK = get_TAK(clicked_var, type_var)
        SRAK = get_SRAK(set_var, rar_var)

        search_str = f"insert into Card(CardNum, SRAK, pName, TAK, HP, RetreatCost) values({cnum_var}, {SRAK}, '{name_var}', '{TAK}', {hp_var}, {retreat_var});"
        my_sql_connection.execute_insert(search_str)
        search_str = 'select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, ' \
                     'setrarity.rName from card, setrarity, typegen where card.SRAK = setrarity.SRAK and card.TAK = ' \
                     'typegen.TAK; '
        popup.destroy()

    insert_label = Label(popup, text='Insert new card')
    insert_label.place(relx=.4, rely=0)

    gen_label = Label(popup, text='Generation')
    gen_label.place(relx=0.04, rely=0.15)
    gen_drop = OptionMenu(popup, clicked, 1, 2)
    gen_drop.place(relx=0.18, rely=0.15)

    set_label = Label(popup, text='Set')
    set_label.place(relx=0.04, rely=0.35)
    set_drop = OptionMenu(popup, set_clicked, 1, 8)
    set_drop.place(relx=0.18, rely=0.35)

    cnum_label = Label(popup, text='Card number')
    cnum_label.place(relx=0.04, rely=0.55)
    cnum_entry = Entry(popup, width=10)
    cnum_entry.place(relx=0.20, rely=0.55)

    hp_label = Label(popup, text='HP')
    hp_label.place(relx=0.04, rely=0.75)
    hp_entry = Entry(popup, width=10)
    hp_entry.place(relx=0.20, rely=0.75)

    name_label = Label(popup, text='Name')
    name_label.place(relx=0.54, rely=0.15)
    name_entry = Entry(popup, width=20)
    name_entry.place(relx=0.70, rely=0.15)

    type_label = Label(popup, text='Type')
    type_label.place(relx=0.54, rely=0.35)
    type_drop = OptionMenu(popup, type_clicked, 'Psychic', 'Darkness', 'Water', 'Fire', 'Fighting', 'Colorless',
                           'Lightning', 'Metal', 'Grass')
    type_drop.place(relx=0.70, rely=0.35)

    retreat_label = Label(popup, text='Retreat Cost')
    retreat_label.place(relx=0.54, rely=0.55)
    retreat_entry = Entry(popup, width=10)
    retreat_entry.place(relx=0.70, rely=0.55)

    rar_label = Label(popup, text='Rarity')
    rar_label.place(relx=0.54, rely=0.75)
    rar_entry = OptionMenu(popup, rar_clicked, 'Common', 'Uncommon', 'Rare')
    rar_entry.place(relx=.7, rely=0.75)

    insert_but = Button(popup, text='insert card', command=insert_func)
    insert_but.place(relx=.43, rely=.9)

    popup.mainloop()


# function for deleting a card.
def delete_card():
    popup = Toplevel()
    popup.geometry("300x200")

    set_clicked = IntVar()
    set_clicked.set(1)

    def delete_push():
        global search_str

        set_var = set_clicked.get()
        cnum_var = card_entry.get()

        search_str = f"delete from Card where SRAK in (select SRAK from setrarity where setnum = {set_var}) and cardNum={cnum_var}"
        my_sql_connection.execute_insert(search_str)
        search_str = 'select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, ' \
                     'setrarity.rName from card, setrarity, typegen where card.SRAK = setrarity.SRAK and card.TAK = ' \
                     'typegen.TAK; '
        popup.destroy()

    delete_label = Label(popup, text="Delete a card")
    delete_label.place(relx=.36, rely=0)

    set_num = Label(popup, text='Set')
    set_num.place(relx=0.32, rely=0.16)
    set_drop = OptionMenu(popup, set_clicked, 1, 8)
    set_drop.place(relx=0.44, rely=0.15)

    card_num = Label(popup, text='Card number')
    card_num.place(relx=0.15, rely=0.35)
    card_entry = Entry(popup, width=8)
    card_entry.place(relx=0.44, rely=0.35)

    delete_but = Button(popup, text='Delete!', width=10, command=delete_push)
    delete_but.place(relx=.36, rely=.8)

    popup.mainloop()


# creating a menubar for inserting and deleting
menubar = Menu(base)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Card", command=new_card)
filemenu.add_command(label="Delete Card", command=delete_card)
menubar.add_cascade(label="Edit", menu=filemenu)

# creating entry box to search for specific pokemon
entry_box = Entry(base, width=45)
entry_box.grid(row=0, column=0, columnspan=4, padx=15)

# button to be able to select by rarity
rarity_but = Button(base, text='Rarity', width=5, command=lambda: rarity_push())
rarity_but.grid(row=1, column=0)

# button to be able to select by Type
type_but = Button(base, text='Type', width=5, command=lambda: type_push())
type_but.grid(row=2, column=0)

# button to be able to select by card set
cardset_but = Button(base, text='Set', width=5, command=lambda: set_push())
cardset_but.grid(row=3, column=0)

# button to be able to select by Generation
generation_but = Button(base, text='Generation', width=10, command=lambda: gen_push())
generation_but.grid(row=4, column=0)

# button to be able to restrict search to pokemon specified in entry box
entry_but = Button(base, text='Search by name', command=lambda: search_push())
entry_but.grid(row=0, column=4)

# Creating initialized labelFrame before you select any button
frame = LabelFrame(base, text="How would you like to search?")
frame.grid(row=1, column=2, rowspan=4, columnspan=3)
initial_label = Label(frame, text='Select a button to the left to narrow your search!', pady=103)
initial_label.grid(row=0, column=0)

# Creating an instance of the SqlUtil class from the utils package
my_sql_connection = SqlUtil()

query_var = my_sql_connection.execute_query(search_str)
print(query_var)

search_but = Button(0, text='search database', command=lambda: test_method(query_var))
search_but.grid(row=5, column=4)


# A method to take in a result query and represent it in a table form on a new popup frame.
def test_method(query_var1):
    root = Tk()

    print(search_str)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    columns = ('Pokemon', 'setNum', 'CardNum', 'Type', 'HP', 'Retreat Cost', 'Rarity')
    table_tree = tkinter.ttk.Treeview(root, columns=columns, show='headings', yscrollcommand=scrollbar.set)
    table_tree.heading('Pokemon', text='Pokemon')
    table_tree.heading('setNum', text='SetNum')
    table_tree.heading('CardNum', text='CardNum')
    table_tree.heading('Type', text='Type')
    table_tree.heading('HP', text='HP')
    table_tree.heading('Retreat Cost', text='Retreat Cost')
    table_tree.heading('Rarity', text='Rarity')

    for item in query_var1:
        table_tree.insert('', tkinter.END, values=item)

    table_tree.pack()
    scrollbar.config(command=table_tree.yview)

    root.mainloop()


# creating method that rarity button will initiate upon clicking
def gen_push():
    global frame
    global search_str

    # A method which takes in a value from the radio button, and searches the database by that selection
    def clicked(gen_value):
        global search_str
        global query_var

        search_str = str(gen_value)
        print(search_str)
        query_var = my_sql_connection.execute_query(search_str)
        search_str = 'select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, ' \
                     'setrarity.rName from card, setrarity, typegen where card.SRAK = setrarity.SRAK and card.TAK = ' \
                     'typegen.TAK; '

    # initializing a string variable which will change depending on which radio button is selected.
    gen_value = StringVar()
    gen_value.set(None)

    # destroys and recreated the frame with new selections to choose from
    frame.destroy()
    frame = LabelFrame(base, text="How would you like to search?", pady=88, padx=84)
    frame.grid(row=1, column=2, rowspan=4, columnspan=3)

    # Radio buttons a user can select to narrow their search of the database
    gen_one_card = Radiobutton(frame, text='Generation 1', variable=gen_value, value="select card.pName, "
                                                                                     "setrarity.setNum, card.CardNum, "
                                                                                     "typegen.TypeName, card.HP, "
                                                                                     "card.retreatCost, "
                                                                                     "setrarity.rName from card, "
                                                                                     "setrarity, typegen where "
                                                                                     "card.TAK in (select TAK from "
                                                                                     "typeGen where genNum = 1) and "
                                                                                     "card.SRAK = setrarity.SRAK and "
                                                                                     "card.TAK = typegen.TAK;",
                               command=lambda: clicked(gen_value.get()))
    gen_one_card.pack()
    gen_two_card = Radiobutton(frame, text='Generation 2', variable=gen_value, value="select card.pName, "
                                                                                     "setrarity.setNum, card.CardNum, "
                                                                                     "typegen.TypeName, card.HP, "
                                                                                     "card.retreatCost, "
                                                                                     "setrarity.rName from card, "
                                                                                     "setrarity, typegen where "
                                                                                     "card.TAK in (select TAK from "
                                                                                     "typeGen where genNum = 2) and "
                                                                                     "card.SRAK = setrarity.SRAK and "
                                                                                     "card.TAK = typegen.TAK;",
                               command=lambda: clicked(gen_value.get()))
    gen_two_card.pack()


# creating method that rarity button will initiate upon clicking
def rarity_push():
    global frame
    global search_str

    # A method which takes in a value from the radio button, and searches the database by that selection
    def clicked(rar_value):
        global search_str
        global query_var

        search_str = str(rar_value)
        print(search_str)
        query_var = my_sql_connection.execute_query(search_str)
        search_str = 'select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, ' \
                     'setrarity.rName from card, setrarity, typegen where card.SRAK = setrarity.SRAK and card.TAK = ' \
                     'typegen.TAK; '

    # initializing a string variable which will change depending on which radio button is selected.
    rar_value = StringVar()
    rar_value.set(None)

    # destroys and recreated the frame with new selections to choose from
    frame.destroy()
    frame = LabelFrame(base, text="How would you like to search?", pady=75, padx=84)
    frame.grid(row=1, column=2, rowspan=4, columnspan=3)

    # Radio buttons a user can select to narrow their search of the database
    common_card = Radiobutton(frame, text='Common', variable=rar_value, value="select card.pName, setrarity.setNum, "
                                                                              "card.CardNum, typegen.TypeName, "
                                                                              "card.HP, card.retreatCost, "
                                                                              "setrarity.rName from card, setrarity, "
                                                                              "typegen where card.SRAK in (select "
                                                                              "SRAK from setrarity where rName = "
                                                                              "'Common') and card.SRAK = "
                                                                              "setrarity.SRAK and card.TAK = "
                                                                              "typegen.TAK;",
                              command=lambda: clicked(rar_value.get()))
    common_card.pack()
    uncommon_card = Radiobutton(frame, text='Uncommon', variable=rar_value,
                                value="select card.pName, setrarity.setNum, "
                                      "card.CardNum, typegen.TypeName, "
                                      "card.HP, card.retreatCost, "
                                      "setrarity.rName from card, setrarity, "
                                      "typegen where card.SRAK in (select "
                                      "SRAK from setrarity where rName = "
                                      "'Uncommon') and card.SRAK = "
                                      "setrarity.SRAK and card.TAK = "
                                      "typegen.TAK;",
                                command=lambda: clicked(rar_value.get()))
    uncommon_card.pack()
    rare_card = Radiobutton(frame, text='Rare', variable=rar_value, value="select card.pName, setrarity.setNum, "
                                                                          "card.CardNum, typegen.TypeName, "
                                                                          "card.HP, card.retreatCost, "
                                                                          "setrarity.rName from card, setrarity, "
                                                                          "typegen where card.SRAK in (select "
                                                                          "SRAK from setrarity where rName = "
                                                                          "'Rare') and card.SRAK = "
                                                                          "setrarity.SRAK and card.TAK = "
                                                                          "typegen.TAK;",
                            command=lambda: clicked(rar_value.get()))
    rare_card.pack()


# creating method that setNum button will initiate upon clicking
def set_push():
    global frame
    global search_str

    # A method which takes in a value from the radio button, and searches the database by that selection
    def clicked(set_value):
        global search_str
        global query_var

        search_str = str(set_value)
        print(search_str)
        query_var = my_sql_connection.execute_query(search_str)
        search_str = 'select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, ' \
                     'setrarity.rName from card, setrarity, typegen where card.SRAK = setrarity.SRAK and card.TAK = ' \
                     'typegen.TAK; '

    # initializing a string variable which will change depending on which radio button is selected.
    set_value = StringVar()
    set_value.set(None)

    # destroys and recreated the frame with new selections to choose from
    frame.destroy()
    frame = LabelFrame(base, text="How would you like to search?", pady=88, padx=84)
    frame.grid(row=1, column=2, rowspan=4, columnspan=3)

    # Radio buttons a user can select to narrow their search of the database
    base_card = Radiobutton(frame, text='Base set', variable=set_value, value="select card.pName, setrarity.setNum, "
                                                                              "card.CardNum, typegen.TypeName, "
                                                                              "card.HP, card.retreatCost, "
                                                                              "setrarity.rName from card, setrarity, "
                                                                              "typegen where card.SRAK in (select "
                                                                              "SRAK from setrarity where setNum = 1) "
                                                                              "and card.SRAK = setrarity.SRAK and "
                                                                              "card.TAK = typegen.TAK;",
                            command=lambda: clicked(set_value.get()))
    base_card.pack()
    neo_gen_card = Radiobutton(frame, text='Neo genesis', variable=set_value,
                               value="select card.pName, setrarity.setNum, "
                                     "card.CardNum, typegen.TypeName, "
                                     "card.HP, card.retreatCost, "
                                     "setrarity.rName from card, setrarity, "
                                     "typegen where card.SRAK in (select "
                                     "SRAK from setrarity where setNum = 8) "
                                     "and card.SRAK = setrarity.SRAK and "
                                     "card.TAK = typegen.TAK;",
                               command=lambda: clicked(set_value.get()))
    neo_gen_card.pack()


# creating method that setNum button will initiate upon clicking
def type_push():
    global frame
    global search_str

    # A method which takes in a value from the radio button, and searches the database by that selection
    def clicked(type_value):
        global search_str
        global query_var

        search_str = str(type_value)
        print(search_str)
        query_var = my_sql_connection.execute_query(search_str)
        search_str = 'select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, ' \
                     'setrarity.rName from card, setrarity, typegen where card.SRAK = setrarity.SRAK and card.TAK = ' \
                     'typegen.TAK; '

    # initializing a string variable which will change depending on which radio button is selected.
    type_value = StringVar()
    type_value.set(None)

    # destroys and recreated the frame with new selections to choose from
    frame.destroy()
    frame = LabelFrame(base, text="How would you like to search?", padx=81)
    frame.grid(row=1, column=2, rowspan=4, columnspan=3)

    # Radio buttons a user can select to narrow their search of the database
    normal_card = Radiobutton(frame, text='Normal type', variable=type_value,
                              value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                    "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                    "in (select TAK from typegen where typeName = 'Colorless') and card.SRAK = "
                                    "setrarity.SRAK and card.TAK = typegen.TAK;",
                              command=lambda: clicked(type_value.get()))
    normal_card.pack()
    dark_card = Radiobutton(frame, text='Dark type', variable=type_value,
                            value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                  "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                  "in (select TAK from typegen where typeName = 'Darkness') and card.SRAK = "
                                  "setrarity.SRAK and card.TAK = typegen.TAK;",
                            command=lambda: clicked(type_value.get()))
    dark_card.pack()
    fighting_card = Radiobutton(frame, text='Fighting type', variable=type_value,
                                value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                      "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                      "in (select TAK from typegen where typeName = 'Fighting') and card.SRAK = "
                                      "setrarity.SRAK and card.TAK = typegen.TAK;",
                                command=lambda: clicked(type_value.get()))
    fighting_card.pack()
    fire_card = Radiobutton(frame, text='Fire type', variable=type_value,
                            value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                  "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                  "in (select TAK from typegen where typeName = 'Fire') and card.SRAK = "
                                  "setrarity.SRAK and card.TAK = typegen.TAK;",
                            command=lambda: clicked(type_value.get()))
    fire_card.pack()
    grass_card = Radiobutton(frame, text='Grass type', variable=type_value,
                             value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                   "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                   "in (select TAK from typegen where typeName = 'Grass') and card.SRAK = "
                                   "setrarity.SRAK and card.TAK = typegen.TAK;",
                             command=lambda: clicked(type_value.get()))
    grass_card.pack()
    electric_card = Radiobutton(frame, text='Electric type', variable=type_value,
                                value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                      "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                      "in (select TAK from typegen where typeName = 'Lightning') and card.SRAK = "
                                      "setrarity.SRAK and card.TAK = typegen.TAK;",
                                command=lambda: clicked(type_value.get()))
    electric_card.pack()
    psychic_card = Radiobutton(frame, text='Psychic type', variable=type_value,
                               value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                     "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                     "in (select TAK from typegen where typeName = 'Psychic') and card.SRAK = "
                                     "setrarity.SRAK and card.TAK = typegen.TAK;",
                               command=lambda: clicked(type_value.get()))
    psychic_card.pack()
    steel_card = Radiobutton(frame, text='Steel type', variable=type_value,
                             value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                   "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                   "in (select TAK from typegen where typeName = 'Metal') and card.SRAK = "
                                   "setrarity.SRAK and card.TAK = typegen.TAK;",
                             command=lambda: clicked(type_value.get()))
    steel_card.pack()
    water_card = Radiobutton(frame, text='Water type', variable=type_value,
                             value="select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, "
                                   "card.retreatCost, setrarity.rName from card, setrarity, typegen where card.TAK "
                                   "in (select TAK from typegen where typeName = 'Water') and card.SRAK = "
                                   "setrarity.SRAK and card.TAK = typegen.TAK;",
                             command=lambda: clicked(type_value.get()))
    water_card.pack()


# A method which creates a new search string based off of what you typed in the EntryBox
def new_search_str(temp_var):
    new_str = f"select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, " \
              f"setrarity.rName from card, setrarity, typegen where card.pName like '{temp_var}%' and  card.SRAK = " \
              f"setrarity.SRAK and card.TAK = typegen.TAK; "
    return new_str


# A method to search for cards based on a string you typed in the EntryBox
def search_push():
    global search_str
    global query_var

    temp_var = entry_box.get()
    search_str = new_search_str(temp_var)
    query_var = my_sql_connection.execute_query(search_str)
    test_method(query_var)


base.config(menu=menubar)
base.mainloop()
