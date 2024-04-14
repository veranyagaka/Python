import keyword

# a. Print the list of Python keywords and store it in a variable named keywords_list
keywords_list = keyword.kwlist
print("List of Python keywords:", keywords_list)

# b. Select five keywords from the list
selected_keywords = keywords_list[:5]  # Select the first five keywords
print("Selected keywords:", selected_keywords)
# help() function
for keyword in selected_keywords:
    print("\nKeyword:", keyword)
    help(keyword)