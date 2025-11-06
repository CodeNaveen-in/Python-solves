# Read the template
with open("./email_template.txt") as templ:
    template = templ.read()

# Read all names
with open("./data.txt") as d:
    names = d.readlines() #read all lines and give them in a list

# Create personalized emails
for name in names:
    name = name.strip()  # Remove newline
    content = template.replace("{{name}}", name)
    with open(f"{name}.txt", 'w') as fl:
        fl.write(content)