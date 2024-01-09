ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = 'World'  # List are mutable and ordered.
ft_tuple = (ft_tuple[0], 'France')  # Tuple aren't mutable.
ft_set.remove("tutu!")
ft_set.add("Paris")  # set are unordered.
ft_dict["Hello"] = '42Paris'  # Dictionary use key instead of index.

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
