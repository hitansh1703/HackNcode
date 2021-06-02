test_str = "missippi"

all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

sorted_values = sorted(all_freq.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in all_freq.keys():
        if all_freq[k] == i:
            sorted_dict[k] = all_freq[k]
            break



#    for k in all_freq.value():
#        if all_freq[k+1] >= all_freq[k]:
#            T = all_freq[k]
#            all_freq[k]=all_freq[k+1]
#            all_freq[k+1]= T
#            break
print ("Count of all characters  :\n "+  str(sorted_dict))
