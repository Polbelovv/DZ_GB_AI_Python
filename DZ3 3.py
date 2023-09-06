#DZ3 3

MAX_WEIGTH = 8_000
things = ['cup', 'spoon', 'plate', 'knife', 'sleeping bag', 'tent',
          'fleece hoody', 'swimming suit', 'boots', 'raincoat']
weights = [400, 78, 310, 77, 1_520, 3_800, 760, 180, 1_250, 670]

my_dict = {}
for num, thing in enumerate(things):
    my_dict[thing] = weights[num]

weight = 0
things_in = []
for key, value in my_dict.items():
    weight += value
    if weight <= MAX_WEIGTH:
        things_in.append(key)
    else:
        weight -= value
print(things_in)
