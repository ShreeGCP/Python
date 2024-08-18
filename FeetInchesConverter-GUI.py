import FreeSimpleGUI as fsg
label1 = fsg.Text("Enter Feet")
text1 = fsg.InputText()
label2 = fsg.Text("Enter Inches")
text2 = fsg.InputText()
convert =  fsg.Button("Convert")

window = fsg.Window("Converter",layout=[[label1,text1],[label2,text2],[convert]])
window.read()
window.close()
