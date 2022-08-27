def frequency_analysis(string):
    d = dict()
    for key in string:
        d[key] = d.get(key, 0) + 1

    return d

def most_frequent(string):
    frequencies = frequency_analysis(string)
    frequency_list = [(freq, letter) for (letter, freq) in frequencies.items()]
    frequency_list.sort(reverse=True)
    print(frequency_list)
  

string = input("Please enter a string")
most_frequent(string)
