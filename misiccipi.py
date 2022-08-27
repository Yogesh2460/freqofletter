"""test_str = "Mississippi"

# using dict.get() to get count
# of each element in string
res = {}

for keys in test_str:
    res[keys] = res.get(keys, 0) + 1

# printing result
res.values()
"""

def frequency_analysis(string):
    d = dict()
    for key in string:
        d[key] = d.get(key, 0) + 1

    return d

def letters_in_order_of_frequency(string):
    frequencies = frequency_analysis(string)
    # frequencies is of bounded size because number of letters is bounded by the dictionary, not the input size
    frequency_list = [(freq, letter) for (letter, freq) in frequencies.items()]
    frequency_list.sort(reverse=True)
    print(frequency_list)
    #return [letter for freq, letter in frequency_list]

string = input()
print (letters_in_order_of_frequency(string))
