ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

ft_list[1] = 'World' # List are mutable and ordered.
ft_tuple = (ft_tuple[0], 'France') # Tuple aren't mutable, we need to create a new tuple
ft_set.remove("tutu!") 
ft_set.add("Paris") # set are unordered, we can't make sure Hello will appear before Hello.
ft_dict["Hello"] = '42Paris' #Dictionary use key instead of index, here Hello is the key.

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
