names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
longest_name = ''
for name in names_list:
    if len(name)>8:
        longest_name = name
    else:
        None
print(longest_name)
