import function
import FreeSimpleGUI as fsg
label = fsg.Text("Enter a Todo item")
input_text = fsg.InputText(tooltip="Enter Todo here")
add_button = fsg.Button("Add")
window = fsg.Window("TO-DO APPLICATION",layout=[[label],[input_text,add_button]])
window.read()
window.close()  