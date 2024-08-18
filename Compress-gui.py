import FreeSimpleGUI as fsg
label1 = fsg.Text("Select the files to compress")
text1 = fsg.Input()
button1 = fsg.FilesBrowse("Choose")
label2 = fsg.Text("Select the files to compress")
text2 = fsg.Input()
button2 = fsg.FolderBrowse("Choose")
compress = fsg.Button("Compress")
window = fsg.Window("File Compression App",layout=[[label1,text1,button1],
                                                   [label2,text2,button2],[compress]])
window.read()
window.close()