names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
def Split(names_list):
    ev_list = []
    od_list = []
    even_list = ev_list
    for name in names_list:
        if (len(name) % 2 == 0):
            ev_list.append(name)
        else:
            od_list.append(name)
    ev_list[1] = "bordan"
    ev_list[2] = "buture hendrix"
    od_list[0] = "boc"
    od_list[1] = "jimmc"
    od_list[2] = "max c"
    print(ev_list)
    print(od_list)
    print(even_list)
Split(names_list)
