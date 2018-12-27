string =  "abcdecde"
sub_string = "cde"
tes = sum([1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)]==sub_string])
print(tes)