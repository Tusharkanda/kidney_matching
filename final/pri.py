import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import scrolledtext


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



blood_type_compatibility = {
        'O': ['O', 'A', 'B', 'AB'],
        'A': ['A', 'AB'],
        'B': ['B', 'AB'],
        'AB': ['AB']
    }
# Excel files
patients_file = "patients.xlsx"
donors_file = "donors.xlsx"


def load_data():
    global patients, donors  # Declare as global variables

    # Load patient and donor data from Excel files
    try:
        patients_df = pd.read_excel(patients_file, index_col='Name')  # Specify 'Name' as the index
        donors_df = pd.read_excel(donors_file, index_col='Name')  # Specify 'Name' as the index

        # Check if 'tissues' column exists in patients_df
        if 'tissues' not in patients_df.columns:
            patients_df['tissues'] = [set()] * len(patients_df)

        # Check if 'tissues' column exists in donors_df
        if 'tissues' not in donors_df.columns:
            donors_df['tissues'] = [set()] * len(donors_df)

        # Convert tissues column to sets
        patients_df['tissues'] = patients_df['tissues'].apply(lambda x: set(eval(x)))
        donors_df['tissues'] = donors_df['tissues'].apply(lambda x: set(eval(x)))

        # Convert dataframes to dictionaries
        patients = patients_df.to_dict(orient='index')
        donors = donors_df.to_dict(orient='index')

        return patients, donors
    except FileNotFoundError:
        # If the file is not found, create empty dataframes
        patients_df = pd.DataFrame(columns=['age', 'blood_group', 'tissues'])
        donors_df = pd.DataFrame(columns=['age', 'blood_group', 'tissues'])

        patients_df.to_excel(patients_file, index=True)  # Save with 'Name' as the index
        donors_df.to_excel(donors_file, index=True)  # Save with 'Name' as the index

        return {}, {}



def save_data():
    global patients, donors  # Declare as global variables

    patients_df = pd.DataFrame.from_dict(patients, orient='index')
    donors_df = pd.DataFrame.from_dict(donors, orient='index')

    # Save patients' names as a separate column
    patients_df.reset_index(inplace=True)
    patients_df.rename(columns={'index': 'Name'}, inplace=True)

    # Save donors' names as a separate column
    donors_df.reset_index(inplace=True)
    donors_df.rename(columns={'index': 'Name'}, inplace=True)

    patients_df.to_excel(patients_file, index=False)
    donors_df.to_excel(donors_file, index=False)



# Load existing data on startup
patients, donors = load_data()

def patient_or_donor_exists(name, data_type):
    """
    Check if a patient or donor already exists.

    Parameters:
        name (str): Name of the patient or donor.
        data_type (str): 'patient' or 'donor'.

    Returns:
        bool: True if the patient or donor exists, False otherwise.
    """
    if data_type == 'patient':
        return name in patients
    elif data_type == 'donor':
        return name in donors
    else:
        raise ValueError("Invalid data type. Use 'patient' or 'donor'.")

def register_patient():
    # Get patient information from input fields
    name = name_entry.get()
    age = age_entry.get()
    blood_group = blood_group_entry.get()
    tissue1 = tissue1_entry.get()
    tissue2 = tissue2_entry.get()
    tissue3 = tissue3_entry.get()
    tissue4 = tissue4_entry.get()
    tissue5 = tissue5_entry.get()
    tissue6 = tissue6_entry.get()

    # Check if the patient name is not empty and patient does not exist
    if name and not patient_or_donor_exists(name, 'patient'):
        # Store patient information in the dictionary
        patients[name] = {
            'age': age,
            'blood_group': blood_group,
            'tissues': {tissue1, tissue2, tissue3, tissue4, tissue5, tissue6}
        }

        # Clear input fields
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        blood_group_entry.delete(0, END)
        tissue1_entry.delete(0, END)
        tissue2_entry.delete(0, END)
        tissue3_entry.delete(0, END)
        tissue4_entry.delete(0, END)
        tissue5_entry.delete(0, END)
        tissue6_entry.delete(0, END)
        # Save data to Excel
        save_data()
        # Display success message
        messagebox.showinfo("Success", "Patient registered successfully!")
    elif not name:
        # Display error message if patient name is empty
        messagebox.showerror("Error", "Please enter patient name.")
    else:
        # Display error message if patient already exists
        messagebox.showerror("Error", "Patient data already exists")

def register_donor():
    # Get donor information from input fields
    name = name_entry.get()
    age = age_entry.get()
    blood_group = blood_group_entry.get()
    tissue1 = tissue1_entry.get()
    tissue2 = tissue2_entry.get()
    tissue3 = tissue3_entry.get()
    tissue4 = tissue4_entry.get()
    tissue5 = tissue5_entry.get()
    tissue6 = tissue6_entry.get()

    # Check if the donor name is not empty, donor does not exist, and age is 18 or above
    if name and not patient_or_donor_exists(name, 'donor') and age.isnumeric() and int(age) >= 18:
        # Store donor information in the dictionary
        donors[name] = {
            'age': age,
            'blood_group': blood_group,
            'tissues': {tissue1, tissue2, tissue3, tissue4, tissue5, tissue6}
        }

        # Clear input fields
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        blood_group_entry.delete(0, END)
        tissue1_entry.delete(0, END)
        tissue2_entry.delete(0, END)
        tissue3_entry.delete(0, END)
        tissue4_entry.delete(0, END)
        tissue5_entry.delete(0, END)
        tissue6_entry.delete(0, END)
        # Save data to Excel
        save_data()
        # Display success message
        messagebox.showinfo("Success", "Donor registered successfully!")
    elif not name:
        # Display error message if donor name is empty
        messagebox.showerror("Error", "Please enter donor name.")
    elif not age.isnumeric() or int(age) < 18:
        # Display error message if age is not numeric or below 18
        messagebox.showerror("Error", "Donor must be 18 years or older.")
    else:
        # Display error message if donor already exists
        messagebox.showerror("Error", "Donor data already exists")

def create_graph():
    # Create a bipartite graph
    G = nx.Graph()

    # Add patients and donors as nodes to the graph
    G.add_nodes_from(patients, bipartite=0)
    G.add_nodes_from(donors, bipartite=1)

    # Define blood type compatibility

    # Add edges between compatible patients and donors with weights
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
                    score = int((len(matching_tissues) * 100) / 6)

                    # Add edge with weight
                    G.add_edge(patient, donor, weight=score)

    # Draw the graph
    pos = nx.bipartite_layout(G, [node for node, data in G.nodes(data=True) if data['bipartite'] == 0])
    edge_labels = {(patient, donor): weight['weight'] for patient, donor, weight in G.edges(data=True)}

    # Separate patients and donors for coloring
    patient_nodes = [node for node, data in G.nodes(data=True) if data['bipartite'] == 0]
    donor_nodes = [node for node, data in G.nodes(data=True) if data['bipartite'] == 1]

    # Node colors
    node_colors = ['skyblue' if node in patient_nodes else 'lightcoral' for node in G.nodes]

    node_labels = {
        node: f"{node}\n({G.nodes[node].get('blood_group', 'patient')})" if G.nodes[node]['bipartite'] == 0 else f"{node}\n({G.nodes[node].get('blood_group', 'donor')})"
        for node in G.nodes
    }

    nx.draw(G, pos, with_labels=True, labels=node_labels, node_color=node_colors, node_size=1500, font_size=10,
            font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
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
                    score=int((len(matching_tissues) *100)/6)

                    compatible_combinations.append((patient, donor,score))


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

tissue4_label = Label(root, text="Tissue 4")
tissue4_label.place(x=100, y=230)
tissue4_entry = Entry(root)
tissue4_entry.place(x=200, y=230)

tissue5_label = Label(root, text="Tissue 5")
tissue5_label.place(x=100, y=260)
tissue5_entry = Entry(root)
tissue5_entry.place(x=200, y=260)

tissue6_label = Label(root, text="Tissue 6")
tissue6_label.place(x=100, y=290)
tissue6_entry = Entry(root)
tissue6_entry.place(x=200, y=290)
patient_button = Button(root, text="Register Patient", command=register_patient)
patient_button.place(x=100, y=230)

donor_button = Button(root, text="Register Donor", command=register_donor)
donor_button.place(x=220, y=230)

graph_button = Button(root, text="Create Graph", command=create_graph)
graph_button.place(x=330, y=230)

root.mainloop()