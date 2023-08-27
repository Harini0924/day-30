#FileNotFound

try:
    file =open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["key"]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("hi")
except KeyError as error_message:
    print(f"Key {error_message} doesn't exist")
else:
    content= file.read()
    print(content)
finally:
    file.close()
    print("file is closed")

#KeyError
#a_dictionary= {"key": "value"}
#value = a_dictionary["non_existent_key"]

#IdentError
#fruit_list=["Apple","Banana", "Pear"]
#fruit = fruit_list[3]

#TypeError
#text="abc"
#print(text+5)