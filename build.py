
import os
import glob
import json
import shutil
from PIL import Image

IMAGE_EXTENSIONS = ["png", "jpg"]
IMAGE_FORMAT = "png"
IMAGE_MAX_SIZE = 1000000
BASE_DIR = "./"

PROJECT_DIR = "projects"
PROJECT_JSON = "projects/projects.json"
PROJECT_FILE = "projects.html"
PROJECTS_TAG = "<!-- include:projects -->"

REPLACE_TAGS = {
    "<!-- include:header -->": "common/header.html",
    "<!-- include:footer -->": "common/footer.html"
}

# Recursively reduce the image resolution of all the images in the repository
def reduceImageResolution(baseDir, maxSize=1000000, extensions=["png", "jpg"], outputFormat="png"):

    images = [a for e in extensions for a in glob.glob(f"{baseDir}/**/*.{e}", recursive=True)]

    for i in images:
        img = Image.open(i)
        totSize = img.size[0] * img.size[1]
        cr = (totSize / maxSize)**0.5
        if cr > 1:
            ns = (int(img.size[0]//cr), int(img.size[1]//cr))
            print(f"recuding {i} from {img.size} to {ns}")
            img = img.resize(ns, Image.ANTIALIAS)
            os.remove(i)
            img.save(".".join(i.split(".")[:-1]) + "." + outputFormat)
 

# Replace tags within a file with contents
def replaceFileTagWithContents(htmlFile, tag, contents):
    with open(htmlFile, "r") as f:
        lines = f.readlines()
    
    try:
        start = [l.strip() for l in lines].index(tag)
    except:
        return
    
    try:
        end = [l.strip() for l in lines].index(tag, start+1)
    except:
        print(f"Failed to find matching tag \"{tag}\" for tag on line {start}")
        return

    lines = lines[:start+1] + [contents] + lines[end:]
    
    with open(htmlFile, "w") as f:
        f.writelines(lines)


# Replace a comment tag with contents in all HTML files
def replaceTagWithContents(baseDir, tag, contents):
    htmlFiles = glob.glob(f"{baseDir}/**/*.html", recursive=True)
    
    for htmlFile in htmlFiles:
        replaceFileTagWithContents(htmlFile, tag, contents)


# Replace a comment tag with the contents of replacementFile int all HTML files	 
def replaceTagWithFile(baseDir, tag, replacementFile):
    with open(os.path.join(baseDir, replacementFile), "r") as f:
        replaceTagWithContents(baseDir, tag, f.read())


# Build projects HTML pages
def buildProjectHtml(template, projectFile):
    pass


# Build projects page
def buildProjectPage(projectshtmlFile="projects.html"):
    pass


# Build projects pages
def buildProjectsPage(projectFile, projectDir, projectJson, projectTag):
    with open(projectJson, "r") as f:
        projectInfo = json.load(f)
    
    projectList = "<ul>\n"
    
    for p in projectInfo:
        href = os.path.join(projectDir, p["folder"], p["folder"] + ".html")    

        projectList += "<li><h2><a href=\"" + href + "\">"
        projectList += p["date"]
        projectList += " - "
        projectList += p["title"]
        projectList += "</a></h2></li>\n"
        
    projectList += "</ul>\n" 
    
    replaceFileTagWithContents(projectFile, projectTag, projectList)

    
if __name__ == "__main__":
    reduceImageResolution(BASE_DIR, IMAGE_MAX_SIZE, IMAGE_EXTENSIONS, IMAGE_FORMAT)
    
    for k, v in REPLACE_TAGS.items():
        replaceTagWithFile(BASE_DIR, k, v)
    
    buildProjectsPage(PROJECT_FILE, PROJECT_DIR, PROJECT_JSON, PROJECTS_TAG)
    
