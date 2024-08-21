
#Task 1

attendees = input ("Enter number of attendees:")
venue = "large hall" if attendees > 100 else "conference room"
print (venue)

#Task 
if attendees > 100:
    venue = "large hall"
    additional_items = "audio system and projector"
elif attendees > 50:
    venue = "medium hall"
    additional_items = "audio system"
else:
    venue = "conference room"
    additional_items = "none"
print("Venue:")
print("Additional items:")

vegetarian = input("Do you want vegetarian food? (yes/no): ")

if vegetarian == "yes":
    catering_service = "Veggie Delight Caterers"
else:
    catering_service = "Gourmet Meals Caterers"
print("Catering service:")    