#counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == "Denver":
 #   print(counties[1])

#for county in counties:
   # print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

for county, voters in counties_dict.items():
    print(county + " County has " + str(voters) + " registered voters")