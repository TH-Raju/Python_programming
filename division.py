bd_division_info = {}
bd_division_info["Feni"] = {"District": 6, "Upazila": 14, "Council": 333}
bd_division_info["Chittagong"] = {"District": 11, "Upazila": 97, "Council": 336}
bd_division_info["Dhaka"] = {"District": 13, "Upazila": 93, "Council": 1833}
bd_division_info["khulna"] = {"District": 10, "Upazila": 59, "Council": 270}
bd_division_info["mymensingh"] = {"District": 4, "Upazila": 34, "Council": 350}
bd_division_info["Rajshahi"] = {"District": 8, "Upazila": 70, "Council": 558}
bd_division_info["Rangpur"] = {"District": 8, "Upazila": 58, "Council": 536}
bd_division_info["Sylhet"] = {"District": 4, "Upazila": 38, "Council": 334}

for div in bd_division_info:
    print(div,":")
    print("     ", "District",bd_division_info[div]["District"])
    print("     ", "Upazila",bd_division_info[div]["Upazila"])
    print("     ", "Council",bd_division_info[div]["Council"])
    print("     ")
    
enter = input("Please Enter Your Division Name: ")
if enter in bd_division_info:
    print(enter,"division has", bd_division_info[enter])
else:
    print("Not in list")