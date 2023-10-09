Hi, this is a template configuration for Obsidian to use to sync up all your notes to Github and beyond. An example file is in [[Example file 1]].

### How to use the template
First, you'll want to use [Mendeley **desktop**](https://www.mendeley.com/guides/desktop) to read and **organise** your papers. To do this:
- Download the app
- Set a watched folder where you can just drag and drop papers and Mendeley will read them in.
	- You can do this under Tools->Options->Watched folders
- Now set up Mendeley to organise your files. Go to Tools->Options->File Organizer and configure it to the following, where the files copy to YOUR/REPO/Papers:
  ![[Pasted image 20231009105025.png]]
- Make sure the Year_Author.pdf is outputted. You can change this if you like, but the script I've got to make the corresponding .md files reads it in this format. So change at your own risk.
- Once you've set this up, make sure to make Mendeley do its thing by pressing Sync. Once its finished, you should be able to view the papers you added in the "Papers" folder to the left.
- Next, **EDIT** the python script makeMDfiles.py in the scripts folder. Change the root_directory path to where this vault is located.
- Run the script. You should now have a file in the annotations folder called "2023_mcculloch.md".
- You can go to this file and view the PDF. Use this file (rather than the original PDF) to do any changes. If the PDF doesn't appear, open the file options (3 dots in the top right) and select "annotate", as shown below:
  ![[Pasted image 20231009112733.png]]
  - Enjoy!

### A couple of things to note
You can view the plugins in the settings. I've installed a couple to get you going, namely, "Annotate" and "Excalidraw". Annotate is used to read the PDFs and allow you to make targeted comments on them. You can also use hashtags to categorise notes. Excalidraw is useful for making quick drawings or snapshotting figures. Both have a good amount of documentation and guides online, so check that out if you want to learn more.

I use this setup on my Windows P

Once you're done with this note, feel free to delete the Setup folder