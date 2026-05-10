contact_info = {
    "name": "Hritik",
    "address": "123 Main St",
    "city": "San Francisco",
    "state": "CA",
    "zip": "94101"
}

# Print formatted address
print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

# Remove name
contact_info.pop("name")

# Create nested dictionary
full_name = {
    "first name": "Hritik",
    "last name": "Zope"
}

# Add honorific
full_name.update({"honorific": "Mr."})

# Add to contact_info
contact_info.update({"full_name": full_name})

print(contact_info)