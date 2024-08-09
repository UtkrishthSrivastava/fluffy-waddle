import datetime
f = open("index.html", "+a")
heading = input("Enter Heading >>>")
matter = input("enter textual matter >>>")

x = open("files.txt", "r")#open files.txt to read
filelist = x.readlines()
x.close()#close

x = open("filenames.txt", "r")#open filenames.txt to read
filenames = x.readlines()
x.close()#close

date_time = str(datetime.datetime.now().date()) + " @ " + str(datetime.datetime.now().time())

while True:
    filename = input("enter filename >>>")
    filename = filename + str(".html")
    if filename+"\n" in filelist:
        print("filename is already present. Please choose a different filename")
        print(f"taken filenames = {filelist}")
    else:
        x = open("files.txt", "+a")#open files.txt
        x.write(filename+"\n")
        x.close()# write and close
        z = open("filenames.txt", "+a")#open files.txt
        z.write(heading+"\n")
        z.close()# write and close
        f.write(f"\n<ul><a href={filename}>{heading}</a></ul>")#write in index.html
        print("file added successfully")
        f.close()#close index.html
        x = open("files.txt", "r")#open files.txt to read
        z = open("filenames.txt", "r")#open filenames.txt to read
        filelist = x.readlines()
        filenames = z.readlines()
        file_ul = ""
        x.close()#close
        z.close()#close
         

        for i in range(len(filelist)):
            file_ul = file_ul + f"<ul><a href='{filelist[i]}'>{filenames[i]}</a></ul>"
            print(file_ul)
        
        blogformat = f"<!DOCTYPE html><html><head><link rel='stylesheet' type='text/css' media='screen' href='styles.css'><title>{heading}</title></style></head><sidebar>{file_ul}</sidebar><main><h1>{heading}</h1><content>{matter}</content><footer>Posted by Utkrishth on {date_time}</footer></main></html>"
        blog = open(filename, "x")
        blog.write(blogformat)
        blog.close()
        print("ADD GIT FUNCTONALITY HERE")
        quit()
        #thank god nvim has auto indentation....
        # i hope i could get the code completion working
