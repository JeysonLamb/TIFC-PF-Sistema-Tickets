# IT Support Ticket System

## 📌 Project Description

This project involves the development of a console-based technical support ticket system for the company TechSoluciones S.A.

The system allows users to register incidents, view tickets, list them, and mark them as resolved during a work session.

All tickets are temporarily stored in an in-memory list while the program is running.


## 🧩 Business Case

The company TechSoluciones S.A. receives dozens of support requests daily and needs a simple solution to manage technical incidents in an organized way.

The objective of the system is to help the IT team to:

- Register support tickets  
- Consult ticket information  
- List registered tickets  
- Change ticket status  
- Generate basic reports  


## 🗂️ Data Structure

All tickets are stored in a list called:

```python
tickets = []
```

The list is created in `main.py` and shared across the different system functions.

Each ticket contains information related to:

- Ticket number  
- Incident description  
- Assigned specialist  
- Issue type  
- Ticket source  
- Priority  
- Date and time opened  
- Ticket status  


## ⚙️ System Features

### 📥 Ticket Registration

Allows the creation of new support tickets by entering the corresponding information.

### 🔎 Query and Listing

Allows users to view registered tickets and consult specific information.

### ✅ Closing and Reporting

Allows users to update the status of tickets and generate basic system reports.


## 👥 Group Participants

- Angelica Herrera Gonzalez  
- Andrea Llorenta  
- Esteban Cordero  
- Lina Chavez


## 🛠️ Technologies Used

- Python  
- Git  
- GitHub  
- Console / Terminal  


## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Enter the project folder

```bash
cd TIFC-PF-Sistema-Tickets
```

### 3. Run the program

```bash
python main.py
```