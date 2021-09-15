# %% if

a = 4
b = 7.0

if a < b:
    print("a is smaller than b")
else:
    print("a is NOT smaller than b")
    
    
a = "string"
b = "string"

if a == b:
    print("Both symbols carry the same.")
else:
    print("The symbols differ.")
    
# %% for

for i in range(5):
    print(i)
    
for item in ["string", 2, 2.0, True]:
    print(item)
    
# %% while

counter = 0

while counter < 10:
    print(counter)
    counter += 1
    
# %% break

counter = 0

while counter < 100:
    print(counter)
    if counter == 3:
        break
    counter += 1
    