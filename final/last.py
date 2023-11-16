import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

root = tk.Tk()
root.geometry("1280x1024")

# Use the 'clam' theme for a more modern appearance
style = ttk.Style()
style.theme_use("clam")

# Customize the style of the buttons
style.configure("TButton",
    font=("Helvetica", 10),
    padding=10,
    foreground="white",
    background="black",
    borderwidth=3,
    relief="raised"
)

# Customize the style of labels
style.configure("TLabel",
    font=("Arial", 10, "bold"),
    foreground="green"
)

# Customize the style of entry fields
style.configure("TEntry",
    font=("Times New Roman", 12),
    foreground="black",
    borderwidth=2,
    relief="sunken"
)

# Load background image
background_image = Image.open("kidneybg.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.image = background_photo  # Keep a reference to the image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Data storage
patients = {}  # Dictionary to store patient information
donors = {}    # Dictionary to store donor information

blood_type_compatibility = {
        'O': ['O', 'A', 'B', 'AB'],
        'A': ['A', 'AB'],
        'B': ['B', 'AB'],
        'AB': ['AB']
    }

def register_patient():
    # Get patient information from input fields
    name = name_entry.get()
    age = age_entry.get()
    blood_group = blood_group_entry.get()
    tissue1 = tissue1_entry.get()
    tissue2 = tissue2_entry.get()
    tissue3 = tissue3_entry.get()

    # Check if the patient name is not empty
    if name:
        # Store patient information in the dictionary
        patients[name] = {
            'age': age,
            'blood_group': blood_group,
            'tissues': {tissue1, tissue2, tissue3}
        }

        # Clear input fields
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        blood_group_entry.delete(0, END)
        tissue1_entry.delete(0, END)
        tissue2_entry.delete(0, END)
        tissue3_entry.delete(0, END)

        # Display success message
        messagebox.showinfo("Success", "Patient registered successfully!")
    else:
        # Display error message if patient name is empty
        messagebox.showerror("Error", "Please enter patient name.")

def register_donor():
    # Get donor information from input fields
    name = name_entry.get()
    age = age_entry.get()
    blood_group = blood_group_entry.get()
    tissue1 = tissue1_entry.get()
    tissue2 = tissue2_entry.get()
    tissue3 = tissue3_entry.get()

    # Check if the donor name is not empty and age is 18 or above
    if name and age.isnumeric() and int(age) >= 18:
        # Store donor information in the dictionary
        donors[name] = {
            'age': age,
            'blood_group': blood_group,
            'tissues': {tissue1, tissue2, tissue3}
        }

        # Clear input fields
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        blood_group_entry.delete(0, END)
        tissue1_entry.delete(0, END)
        tissue2_entry.delete(0, END)
        tissue3_entry.delete(0, END)

        # Display success message
        messagebox.showinfo("Success", "Donor registered successfully!")
    elif not name:
        # Display error message if donor name is empty
        messagebox.showerror("Error", "Please enter donor name.")
    elif not age.isnumeric() or int(age) < 18:
        # Display error message if age is not numeric or below 18
        messagebox.showerror("Error", "Donor must be 18 years or older.")

def create_graph():
    # Create a bipartite graph
    G = nx.Graph()

    # Add patients and donors as nodes to the graph
    G.add_nodes_from(patients, bipartite=0)
    G.add_nodes_from(donors, bipartite=1)

    # Define blood type compatibility

    # Add edges between compatible patients and donors
    for patient, pdata in patients.items():
        for donor, ddata in donors.items():
            patient_blood_group = pdata['blood_group']
            donor_blood_group = ddata['blood_group']

            # Check blood type compatibility
            if patient_blood_group in blood_type_compatibility and \
               donor_blood_group in blood_type_compatibility[patient_blood_group]:
                # Check for at least two matching tissues
                matching_tissues = pdata['tissues'] & ddata['tissues']
                if len(matching_tissues) >= 2:
                    G.add_edge(patient, donor)

    # Draw the graph
    pos = nx.bipartite_layout(G, [node for node, data in G.nodes(data=True) if data['bipartite'] == 0])
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold')
    plt.title("Kidney Matching Graph")
    plt.show()

def display_compatible_combinations():
    compatible_combinations = []

    for patient, pdata in patients.items():
        for donor, ddata in donors.items():
            patient_blood_group = pdata['blood_group']
            donor_blood_group = ddata['blood_group']

            # Check blood type compatibility
            if patient_blood_group in blood_type_compatibility and \
               donor_blood_group in blood_type_compatibility[patient_blood_group]:
                # Check for at least two matching tissues
                matching_tissues = pdata['tissues'] & ddata['tissues']
                if len(matching_tissues) >= 2:
                    compatible_combinations.append((patient, donor))

    # Display compatible combinations in the GUI (e.g., in a listbox or a table)
    if compatible_combinations:
        messagebox.showinfo("Compatible Combinations", f"Compatible combinations: {compatible_combinations}")
    else:
        messagebox.showinfo("No Compatible Combinations", "No compatible combinations found.")
def show_donor_details():
    donor_details = ""
    for donor, ddata in donors.items():
        donor_details += f"Name: {donor}\n"
        donor_details += f"Age: {ddata['age']}\n"
        donor_details += f"Blood Group: {ddata['blood_group']}\n"
        donor_details += f"Tissues: {', '.join(ddata['tissues'])}\n\n"

    if donor_details:
        messagebox.showinfo("Donor Details", donor_details)
    else:
        messagebox.showinfo("No Donor Details", "No donor details available.")

def show_patient_details():
    patient_details = ""
    for patient, pdata in patients.items():
        patient_details += f"Name: {patient}\n"
        patient_details += f"Age: {pdata['age']}\n"
        patient_details += f"Blood Group: {pdata['blood_group']}\n"
        patient_details += f"Tissues: {', '.join(pdata['tissues'])}\n\n"

    if patient_details:
        messagebox.showinfo("Patient Details", patient_details)
    else:
        messagebox.showinfo("No Patient Details", "No patient details available.")

# Add a button to trigger displaying compatible combinations
compatible_combinations_button = Button(root, text="Show Compatible Combinations", command=display_compatible_combinations)
compatible_combinations_button.place(x=450, y=230)

# Add buttons to show donor and patient details
donor_details_button = Button(root, text="Show Donor Details", command=show_donor_details)
donor_details_button.place(x=650, y=230)

patient_details_button = Button(root, text="Show Patient Details", command=show_patient_details)
patient_details_button.place(x=800, y=230)
# UI components
name_label = Label(root, text="Name")
name_label.place(x=100, y=50)
name_entry = Entry(root)
name_entry.place(x=200, y=50)

age_label = Label(root, text="Age")
age_label.place(x=100, y=80)
age_entry = Entry(root)
age_entry.place(x=200, y=80)

blood_group_label = Label(root, text="Blood Group")
blood_group_label.place(x=100, y=110)
blood_group_entry = Entry(root)
blood_group_entry.place(x=200, y=110)

tissue1_label = Label(root, text="Tissue 1")
tissue1_label.place(x=100, y=140)
tissue1_entry = Entry(root)
tissue1_entry.place(x=200, y=140)

tissue2_label = Label(root, text="Tissue 2")
tissue2_label.place(x=100, y=170)
tissue2_entry = Entry(root)
tissue2_entry.place(x=200, y=170)

tissue3_label = Label(root, text="Tissue 3")
tissue3_label.place(x=100, y=200)
tissue3_entry = Entry(root)
tissue3_entry.place(x=200, y=200)

patient_button = Button(root, text="Register Patient", command=register_patient)
patient_button.place(x=100, y=230)

donor_button = Button(root, text="Register Donor", command=register_donor)
donor_button.place(x=220, y=230)

graph_button = Button(root, text="Create Graph", command=create_graph)
graph_button.place(x=330, y=230)

root.mainloop()
