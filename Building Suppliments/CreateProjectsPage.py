import os

PROJECTS_TEMPLATE = "projects_template.html"
OUTPUT_NAME = "projects.html"
PROJECTS_FOLDER = "../projects"
START_TAG = "<!--1-->"
NAME_TAG = "<name>"
DATE_TAG = "<date>"
TEXT_TAG = "<text>"

# Read all the template text
def get_file_text(file):
	print(file)
	with open(file, "r") as f:
		str = f.read()
	return(str)

# Get everything before the start tag
def get_template_preface(text):
	start = text.find(START_TAG)
	return(text[0:start])

# Get everything after the start tag
def get_template_postface(text):
	start = text.find(START_TAG)
	return(text[start:-1])

# Get the date from the project file
def get_date(text):
	start = text.find(DATE_TAG) + len(DATE_TAG)
	end = text.find("</" + DATE_TAG[1:-1])
	return(text[start:end])

# Get the title from the project file
def get_title(text):
	str = get_date(text)
	start = text.find(NAME_TAG) + len(NAME_TAG)
	end = text.find("</" + NAME_TAG[1:-1])
	str += " - " + text[start:end]
	return(str)

# Get the text from the project file
def get_text(text):
	start = text.find(TEXT_TAG) + len(TEXT_TAG)
	end = text.find("</" + TEXT_TAG[1:-1])
	return(text[start:end])

# Format the projects text
def format(title, text):
	str = comment(title)
	str += "<h1><a name=\"" + title + "\"></a>\n"
	str += title + "\n"
	str += "</h1>\n"
	str += "<h2>\n"
	str += text + "\n"
	str += "</h2>"
	return(str)

# Create the table of contents
def create_contents(titles):
	str = comment("Table of Contents")
	str += "<h1>\n"
	str += "<b>Contents</b><br>\n"
	for t in titles:
		str += "<a href=\"#" + t + "\">\n"
		str += t + "\n"
		str += "</a><br>\n"
	str += "</h1>"
	return(str)

# Print text to the output file
def output_print(text, preSpace=True, postSpace=True):
	with open(OUTPUT_NAME, "a") as f:
		if(preSpace):
			f.write("\n\n")
		f.write(text)
		if(postSpace):
			f.write("\n\n")

# Create an HTML comment from the text
def comment(text):
	return("<!-- " + text + "-->\n")


def sort_projects(projects):
	dates = [get_date(p)[::-1] for p in projects]
	return([p for d, p in sorted(zip(dates, projects), reverse=True)])
	

os.remove(OUTPUT_NAME)
templateText = get_file_text(PROJECTS_TEMPLATE)
templatePreface = get_template_preface(templateText)
templatePostface = get_template_postface(templateText)
projects = [get_file_text(PROJECTS_FOLDER + "/" + p) for p in os.listdir(PROJECTS_FOLDER) if '.html' in p]
projects = sort_projects(projects)
contents = create_contents([get_title(p) for p in projects])

output_print(templatePreface)
output_print(contents)

for p in projects:
	output_print("<br><br><div id=\"divline\"></div><br><br>")
	output_print(format(get_title(p), get_text(p)))
	
	
output_print(templatePostface)






