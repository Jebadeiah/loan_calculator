army_size = int(input())
army_name = ""
if army_size < 1:
    army_name = 'no army'
elif 1 <= army_size <= 9:
    army_name = 'few'
elif 10 <= army_size <= 49:
    army_name = 'pack'
elif 50 <= army_size <= 499:
    army_name = 'horde'
elif 500 <= army_size <= 999:
    army_name = 'swarm'
elif army_size >= 1000:
    army_name = 'legion'
print(army_name)
