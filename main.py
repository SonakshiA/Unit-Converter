from tkinter import *
from tkinter import ttk
from math import pow

initial = 0
final = 0

# selected metric 

def selected(event):
    global input_dropdown, output_dropdown
    option = dropdown.get()

    if option=="Length":
        input_dropdown = ttk.Combobox(window, values=["cm", "mm", "m", "km","dm","dam","hm"], state="readonly",textvariable=unit)
        input_dropdown.grid(row=3, column=1)
        input_dropdown.bind("<<ComboboxSelected>>", length_convert)

        output_dropdown = ttk.Combobox(window, values=["cm", "mm", "m", "km","dm","dam","hm"], state="readonly",textvariable=unit)
        output_dropdown.grid(row=3, column=2)
        output_dropdown.bind("<<ComboboxSelected>>", length_convert)

    elif option == "Temperature":
        input_dropdown = ttk.Combobox(window, values=["Kelvin","Fahrenheit","Celsius"],state="readonly",textvariable=unit)
        input_dropdown.grid(row=3,column=1)
        input_dropdown.bind("<<ComboboxSelected>>", temp_convert)

        output_dropdown = ttk.Combobox(window, values=["Kelvin","Fahrenheit","Celsius"],state="readonly",textvariable=unit)
        output_dropdown.grid(row=3, column=2)
        output_dropdown.bind("<<ComboboxSelected>>", temp_convert)

    elif option == "Speed":
        input_dropdown = ttk.Combobox(window, values=["km/h","m/s"], state="readonly",textvariable=unit)
        input_dropdown.grid(row=3, column=1)
        input_dropdown.bind("<<ComboboxSelected>>", speed_convert)

        output_dropdown = ttk.Combobox(window, values=["km/h","m/s"], state="readonly",textvariable=unit)
        output_dropdown.grid(row=3, column=2)
        output_dropdown.bind("<<ComboboxSelected>>", speed_convert)

    elif option == "Angle":
        input_dropdown = ttk.Combobox(window, values=["Degrees","Radians"], state="readonly",textvariable=unit)
        input_dropdown.grid(row=3, column=1)
        input_dropdown.bind("<<ComboboxSelected>>",angle_convert)

        output_dropdown = ttk.Combobox(window, values=["Degrees","Radians"], state="readonly",textvariable=unit)
        output_dropdown.grid(row=3, column=2)
        output_dropdown.bind("<<ComboboxSelected>>",angle_convert)

    elif option == "Mass":
        input_dropdown = ttk.Combobox(window, values=["kg","g","mg","pound","tonne","ounce"],state="readonly",textvariable=unit)
        input_dropdown.grid(row=3, column=1)
        input_dropdown.bind("<<ComboboxSelected>>", mass_convert)

        output_dropdown = ttk.Combobox(window, values=["kg","g","mg","pound","tonne","ounce"], state="readonly",textvariable=unit)
        output_dropdown.grid(row=3, column=2)
        output_dropdown.bind("<<ComboboxSelected>>", mass_convert)

    elif option == "Area":
        input_dropdown = ttk.Combobox(window, values=["sq. km", "sq. hm (hectares)", "sq. dam", "sq. m", "sq. dm", "sq. cm","sq. mm"], state="readonly",textvariable=unit)
        input_dropdown.grid(row=3, column=1)
        input_dropdown.bind("<<ComboboxSelected>>", area_convert)

        output_dropdown = ttk.Combobox(window,  values=["sq. km", "sq. hm (hectares)", "sq. dam", "sq. m", "sq. dm", "sq. cm","sq. mm"], state="readonly",textvariable=unit)
        output_dropdown.grid(row=3, column=2)
        output_dropdown.bind("<<ComboboxSelected>>", area_convert)

    elif option == "Volume":
        input_dropdown = ttk.Combobox(window, values=["kL","hL","daL","L or (cubic. dm)","dL","cL","mL (cubic cm)"], state="readonly",textvariable=unit)
        input_dropdown.grid(row=3, column=1)
        input_dropdown.bind("<<ComboboxSelected>>", volume_convert)

        output_dropdown = ttk.Combobox(window,  values=["kL","hL","daL","L or (cubic. dm)","dL","cL","mL (cubic cm)"], state="readonly",textvariable=unit)
        output_dropdown.grid(row=3, column=2)
        output_dropdown.bind("<<ComboboxSelected>>", volume_convert)

    elif option == "Pressure":
        input_dropdown = ttk.Combobox(window, values=["bar","atm","mm of Hg (torr)","cm of Hg","pascal"], state="readonly",textvariable=unit)
        input_dropdown.grid(row=3, column=1)
        input_dropdown.bind("<<ComboboxSelected>>", pressure_convert)

        output_dropdown = ttk.Combobox(window, values=["bar","atm","mm of Hg (torr)","cm of Hg","pascal"], state="readonly",textvariable=unit)
        output_dropdown.grid(row=3, column=2)
        output_dropdown.bind("<<ComboboxSelected>>", pressure_convert)



def button_output():
    global final
    converted_entered_val.delete(0, END)
    converted_entered_val.insert(0, final)

def length_convert(event):
    global input_dropdown,output_dropdown, input_val,final,initial
    input_dropdown_option = input_dropdown.get()

    #convert input into metre
    if input_dropdown_option == "dm":
        initial = input_val.get() / 10
    elif input_dropdown_option == "cm":
        initial = input_val.get() / 100
    elif input_dropdown_option == "mm":
        initial = input_val.get() / 1000
    elif input_dropdown_option == "km":
        initial = input_val.get() * 1000
    elif input_dropdown_option == "hm":
        initial = input_val.get() * 100
    elif input_dropdown_option == "dam":
        initial = input_val.get() * 10
    else:                                                   #if "input_dropdown_option == m"
        initial = input_val.get()

    output_dropdown_option = output_dropdown.get()

    # converting input (changed to metres) to desired unit
    if output_dropdown_option == "dm":
        final = initial * 10
    elif output_dropdown_option == "cm":
        final = initial * 100
    elif output_dropdown_option == "mm":
        final = initial * 1000
    elif output_dropdown_option == "dam":
        final = initial / 10
    elif output_dropdown_option == "hm":
        final = initial / 100
    elif output_dropdown_option == "km":
        final = initial / 1000
    elif output_dropdown_option == "m":
        final = initial

def temp_convert(event):
    global input_dropdown, output_dropdown,input_val, initial, final
    input_dropdown_option = input_dropdown.get()
    
    # converting to Kelvin
    if input_dropdown_option == "Celsius":
        initial = input_val.get() + 273.15
    elif input_dropdown_option == "Fahrenheit":
        initial = (input_val.get() + 459.67) * (5/9)
    else:
        initial = input_val.get()

    output_dropdown_option = output_dropdown.get()

    if output_dropdown_option == "Celsius":
        final = initial - 273.15
    elif output_dropdown_option == "Fahrenheit":
        final = (9/5)*(initial - 273) + 32
    elif output_dropdown_option == "Kelvin":
        final = initial

def speed_convert(self):
    global input_dropdown, output_dropdown, input_val, initial, final
    input_dropdown_option = input_dropdown.get()
    
    #converting to m/s
    if input_dropdown_option == "km/h":
        initial = input_val.get()/3.6
    else:
        initial = input_val.get()

    output_dropdown_option = output_dropdown.get()

    if output_dropdown_option == "km/h":
        final = initial * 3.6
    elif output_dropdown_option == "m/s":
        final = initial

def angle_convert(self):
    global input_dropdown, output_dropdown, input_val, initial, final
    input_dropdown_option = input_dropdown.get()

    # converting to degrees
    if input_dropdown_option == "Radians":
        initial = input_val.get()*57.3
    else:
        initial = input_val.get()

    output_dropdown_option = output_dropdown.get()

    if output_dropdown_option == "Radians":
        final = input_val.get() * 0.0174
    else:
        final = initial

def mass_convert(event):
    global input_dropdown, output_dropdown, input_val, initial, final
    input_dropdown_option = input_dropdown.get()

    # converting into gram
    if input_dropdown_option == "kg":
        initial = input_val.get() * 1000
    elif input_dropdown_option == "mg":
        initial = input_val.get() / 1000
    elif input_dropdown_option == "tonne":
        initial = input_val.get() * 1000 * 1000
    elif input_dropdown_option == "pound":
        initial = input_val.get() * 453.592
    elif input_dropdown_option == "ounce":
        initial = input_val.get() * 28.35
    elif input_dropdown_option == "g":
        initial = input_val.get()

    output_dropdown_option = output_dropdown.get()

    if output_dropdown_option == "kg":
        final = initial/1000
    elif output_dropdown_option == "mg":
        final = initial * 1000
    elif output_dropdown_option == "tonne":
        final = initial/(1000*1000)
    elif output_dropdown_option == "pound":
        final = initial/453.592
    elif output_dropdown_option == "ounce":
        final = initial/28.35
    elif output_dropdown_option == "g":
        final = initial

def area_convert(event):
    global input_dropdown, output_dropdown, input_val, initial, final
    input_dropdown_option = input_dropdown.get()
    
    #converting to sq. metres
    if input_dropdown_option == "sq. mm":
        initial = input_val.get()/(1000*1000)
    elif input_dropdown_option == "sq. cm":
        initial = input_val.get() / (100 * 100)
    elif input_dropdown_option == "sq. dm":
        initial = input_val.get() / (10 * 10)
    elif input_dropdown_option == "sq. dam":
        initial = input_val.get() * 10 * 10
    elif input_dropdown_option == "sq. hm":
        initial = input_val.get() * 100 * 100
    elif input_dropdown_option == "sq. km":
        initial = input_val.get() * 1000 * 1000
    else:
        initial = input_val.get()

    output_dropdown_option = output_dropdown.get()

    if output_dropdown_option == "sq. mm":
        final = input_val.get() * (1000 * 1000)
    elif output_dropdown_option == "sq. cm":
        final = input_val.get() * (100 * 100)
    elif output_dropdown_option == "sq. dm":
        final = input_val.get() * (10 * 10)
    elif output_dropdown_option == "sq. dam":
        final = input_val.get() / (10 * 10)
    elif output_dropdown_option == "sq. hm (hectares)":
        final = input_val.get() / (100 * 100)
    elif output_dropdown_option == "sq. km":
        final = input_val.get() / (1000 * 10000)
    else:
        final = initial

def volume_convert(event):
    global input_dropdown, output_dropdown, input_val, initial, final
    input_dropdown_option = input_dropdown.get()
    
    # converting to L
    if input_dropdown_option == "dL":
        initial = input_val.get() / 10
    elif input_dropdown_option == "cL":
        initial = input_val.get() / 100
    elif input_dropdown_option == "mL (cubic cm)":
        initial = input_val.get() / 1000
    elif input_dropdown_option == "kL":
        initial = input_val.get() * 1000
    elif input_dropdown_option == "hL":
        initial = input_val.get() * 100
    elif input_dropdown_option == "daL":
        initial = input_val.get() * 10
    elif input_dropdown_option == "gallon":
        initial = input_val.get() * 3.785
    elif input_dropdown_option == "L or (cubic. dm)":                                                   #if "input_dropdown_option == L"
        initial = input_val.get()

    output_dropdown_option = output_dropdown.get()

 
    if output_dropdown_option == "dL":
        final = initial * 10
    elif output_dropdown_option == "cL":
        final = initial * 100
    elif output_dropdown_option == "mL (cubic cm)":
        final = initial * 1000
    elif output_dropdown_option == "daL":
        final = initial / 10
    elif output_dropdown_option == "hL":
        final = initial / 100
    elif output_dropdown_option == "kL":
        final = initial / 1000
    elif output_dropdown_option == "gallon":
        final = initial / 3.785
    elif output_dropdown_option == "L or (cubic. dm)":
        final = initial

def pressure_convert(event):
    global input_dropdown, output_dropdown, input_val, initial, final
    input_dropdown_option = input_dropdown.get()

    if input_dropdown_option == "atm":
        initial = input_val.get() * 101325
    elif input_dropdown_option == "mm of Hg (torr)":
        initial = input_val.get() * 133.322
    elif input_dropdown_option == "bar":
        initial = input_val.get() * 100000
    elif input_dropdown_option == "pascal":
        initial = input_val.get()
    elif input_dropdown_option == "cm of Hg":
        initial = input_val.get() * 1333.22

    output_dropdown_option = output_dropdown.get()

    if output_dropdown_option == "atm":
        final = initial / 101325
    elif output_dropdown_option == "mm of Hg (torr)":
        final = initial / 133.322
    elif output_dropdown_option == "bar":
        final = initial / 100000
    elif output_dropdown_option == "cm of Hg":
        final = initial / 1333.22
    elif output_dropdown_option == "pascal":
        final = initial



window=Tk()
window.title("Converter App")
window.geometry("900x250")
window.configure(bg="AntiqueWhite1")

# GUI Labels
Label(text="Converter-o-Meter",font=("Times","30","bold"),bg="light goldenrod",fg="light coral").grid(row=0,column=1,pady=20)
Label(window,text="Input",bg="AntiqueWhite1",font=("Times",15,"bold")).grid(row=2,column=0)
Label(window,text="Output",bg="AntiqueWhite1",font=("Times",15,"bold")).grid(row=2,column=3)

# initialising variables
input_val = DoubleVar()  #INPUT
input_dropdown = StringVar()
output_dropdown = StringVar()

#entry widgets
entered_val = Entry(window, textvariable=input_val)
converted_entered_val = Entry(window)
entered_val.grid(row=3, column=0, padx=20)
converted_entered_val.grid(row=3, column=3)

button = Button(text="Convert",fg="red",bg="AntiqueWhite1",command=button_output).grid(row=4,column=1,pady=20)

# dropdown menu
method = StringVar(value="Choose a metric") # to add text to dropdown
unit =  StringVar(value="Choose unit") # to add text to unit dropdown
dropdown = ttk.Combobox(window,values=["Length","Temperature","Speed","Angle","Mass","Area","Volume","Pressure"],state="readonly",textvariable=method)
dropdown.grid(row=1,column=1)
dropdown.bind("<<ComboboxSelected>>",selected)

window.mainloop()
