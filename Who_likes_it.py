#Task: Who likes it?
#You probably know the "like" system from Facebook and other pages. 
#People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.



def likes(names):
    list_lenght = len(names)
    if list_lenght == 0:
        print('no one likes this')
    elif list_lenght == 1:
        print(names[0], 'likes this')
    elif list_lenght == 2:
        print(names[0], 'and', names[1], 'likes this')
    elif list_lenght == 3:
        print(names[0], names[1], 'and', names[2], 'likes this')
    elif list_lenght >= 4:
        print(print(names[0], names[1], 'and', list_lenght-2, 'other likes this'))
