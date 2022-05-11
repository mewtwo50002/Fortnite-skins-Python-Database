from tkinter import Tk, simpledialog, messagebox


def read_from_file():
    with open('Skins.txt') as file:
        for line in file:
            line.rstrip('/n')
            name, rarity = line.split('/')
            the_skin[name] = rarity


def write_to_file(skin_name, skin_rarity):
    with open('Skins.txt', 'a') as file:
        file.write('/n' + skin_name + '/' + skin_rarity)


print('Ask the Database - Fortnite skins')
root = Tk()
root.withdraw
the_skin = {}
while True:
    query_name = simpledialog.askstring('Name', "The name of the skin")

    if query_name in the_skin:
        result = the_skin[query_name]
        messagebox.showinfo('Answer',
                            'The Rarity of' + query_name + 'is' + result + '!')
    else:
        new_rarity = simpledialog.askstring(
            'Teach Me',
            'I don\'t know '+ 'What is the rarity of ' + query_name + '?')
        the_skin[query_name] = new_rarity
        write_to_file(query_name, new_rarity)

root.mainloop()
