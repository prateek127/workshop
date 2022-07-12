#day 7
# properties = {
#     "data": {
#         "profiles":[
#             {
#                 "name" : "Ram",
#                 "rank" : 1,
#                 "contact" : ["98999", "98777"]
#             },
#             {
#                 "name" : "Sita",
#                 "rank" : 2,
#                 "contact" : ["98666", "98555"]
#             }
#         ]
#     }
#  }
 
# print(properties.get("data").get("profiles"))
# profiles = properties.get("data").get("profiles")
# for profile in profiles:
#     print("********************")
#     print(f"Name:  {profile.get('name')}")
#     print(f"Rank:  {profile.get('rank')}")
#     for indx, contact in enumerate(profile.get("contact"),1):
#         print(f"Contact {indx}:  {contact}")
    

def profile(name, contact, address):
    print("-----------------------")
    print(f"Name: {name}")
    print(f"Contact: {contact}")
    print(f"Address: {address}")

profile("Ram", "98978", "KTM")  #positional arguments
profile("Ram", "KTM", "98978")
profile(name = "Ram", contact = "98978", address = "KTM") #keyword arguments