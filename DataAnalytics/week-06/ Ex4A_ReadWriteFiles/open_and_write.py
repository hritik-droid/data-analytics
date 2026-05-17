# Exercise 4.A Lab 1
# Practicing file writing

# Open about_me.txt in append mode.
f = open("about_me.txt", "a")

# Add additional information to the file.
f.write("\nIf I could do anything for my perfect night out, I would go out to dinner, see a movie, and spend time with friends.\n")

# Close the file after writing.
f.close()
