f = open("index.html", "+a")
heading = input("Enter Heading >>>")
matter = input("enter textual matter >>>")

x = open("files.txt", "r")
filelist = x.readlines()
x.close()
date_time = 1234
blogformat = f"<!DOCTYPE html><html><head><link rel='stylesheet' type='text/css' media='screen' href='styles.css'><title>{heading}</title></style></head><h1>{heading}</h1><content>{matter}</content><footer>Posted by Utkrishth on {date_time}</footer></html>"

while True:
    filename = input("enter filename >>>")
    filename = filename + str(".html")
    if filename+"\n" in filelist:
        print("filename is already present. Please choose a different filename")
        print(f"taken filenames = {filelist}")
    else:
        x = open("files.txt", "+a")
        x.write(filename+"\n")
        x.close()
        f.write(f"\n<ul><a href={filename}>{heading}</a></ul>")
        print("file added successfully")
        f.close()
        blog = open(filename, "x")
        blog.write(blogformat)
        blog.close()
        print("ADD GIT FUNCTONALITY HERE")
        quit()