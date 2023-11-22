# kidney_match A bipartite solution :)
Welcome to Our project -_-
An creative approach towards Kidney Matching System

Teammates:-) 1)Tushar kanda (https://github.com/Tusharkanda) 
            mail :- tusharkanda.221ai042@nitk.edu.in
            2) Priyanshu maniyar(https://github.com/priyanshu-Maniyar)
            mail:- priyanshumaniyar.221ai023@nitk.edu.in

This project implements a Kidney Matching System using Python with functionalities to register patients and donors, analyze compatibility between them based on blood type and HLA tissues, and visualize the compatibility using a graph.

Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)


## Introduction

The Kidney Matching System is a Python-based application using libraries such as NetworkX, Matplotlib, and Tkinter. It allows registering patients and donors, checking their compatibility based on blood groups and tissues, and visualizing the compatibility graphically.
This uses a greedy Algorythm to compare the compatability between diffrent patients and donors.
This is small try to cure this humanity's great misdeed.

# Comparison with the algorythm already available on internet 
##Note :- we do not critisize the already available on this topic
we did a different approach towards the problem of stable kidney matching 
# our creative keypoints include
1)Using sets for the effective data storage and distribution
2) Using greedy algorythm to find the stable match
3)Using # Bipartite graph for showing the connection between the patient and the donor 

## Requirements

To run this system, ensure you have the following installed:
- Python 3.x
- Required Python libraries: NetworkX, Matplotlib, Pandas, Pillow (PIL)

The provided project relies on various Python modules for different functionalities. To run this project successfully, ensure you have the following modules installed:

NetworkX: For creating and manipulating graphs.

To install: pip install networkx
Matplotlib: Used for visualization, particularly for plotting graphs.

To install: pip install matplotlib
Tkinter: For the graphical user interface (GUI).

Tkinter is usually included by default with Python installations. However, if you encounter issues or use a specific Python distribution that might not include it, you can install it using:
 For Debian/Ubuntu based systems
sudo apt-get install python3-tk

 For macOS (using Homebrew)
brew install python-tk

 For Windows (if not already included with Python)
Download and install Python from the official website, ensuring to select the "tcl/tk and IDLE" option during installation.
#Setup

Pandas: For handling data in DataFrame structures.

To install: pip install pandas
Pillow (PIL): For handling images and image-related operations.

To install: pip install pillow
These are the major modules used in the provided code for various functionalities. Before running the code, ensure you've installed these modules using pip install <module_name> if they're not already installed in your Python environment. Additionally, make sure to have a compatible Python version (3.x) installed on your system to execute this project.

1. Clone the repository:
   ```bash
   git clone https://github.com/sachin9536/kidney_matching.git
   cd kidney-matching-system
Install the required dependencies:

pip install -r requirements.txt
Ensure the necessary data files are present:

patients.xlsx: Excel file containing patient data
donors.xlsx: Excel file containing donor data

## Usage
To run the Kidney Matching System:

python kidney_match.py
Follow the on-screen instructions to register patients, donors, and explore compatibility.

## Contributing
Contributions to improve this system are welcome! Here's how you can contribute:

Fork the repository
Create your feature branch (git checkout -b feature/YourFeature)
Commit your changes (git commit -m 'Add YourFeature')
Push to the branch (git push origin feature/YourFeature)
Open a pull request
