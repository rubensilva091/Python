with open("a_file.txt") as file:
    file.read()


#try:
#    with open("data.json", "r") as data_file:
#        # Reading old data
#        data = json.load(data_file)
#except FileNotFoundError:
#    with open("data.json", "w") as data_file:
#        json.dump(new_data, data_file, indent=4)
#else:
#    # Updating old data with new data
#    data.update(new_data)
#
#    with open("data.json", "w") as data_file:
#        # Saving updated data
#        json.dump(data, data_file, indent=4)
#finally:
#    website_entry.delete(0, END)
#    password_entry.delete(0, END)



#Nothing important here!
