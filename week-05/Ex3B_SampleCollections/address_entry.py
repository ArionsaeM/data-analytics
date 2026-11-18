##Arionsae McCutcheon
#address entry Lab 3 - Ex 3B

contact_info = {
    "name": "Arionsae M",
    "address": "123 Cloud Ave",
    "city": "Jamaica",
    "state": "New York",
    "zip": "11433"
}

print (f"""{contact_info["name"]},
       {contact_info["address"]},
       {contact_info['city']}, {contact_info['state']}
         {contact_info['zip']}""")

contact_info.pop("name") #removes a key and its value alternative del contact_info['name']

print (contact_info)

full_name = {
    "first_name": "Arionsae",
    "last_name": "Mccutcheon"
}

full_name.update ({"honorific": "Ms."})
print(full_name)

contact_info.update ({"full_name": full_name})
print (contact_info) 

print (f""" 
       {contact_info["full_name"]["honorific"]}, {contact_info["full_name"]["first_name"]}, {contact_info["full_name"]["last_name"]}
       {contact_info["address"]},
       {contact_info['city']}, {contact_info['state']}
       {contact_info['zip']}""")