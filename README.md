# Railway Management System 🚂

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

This project is a **Command-Line Interface (CLI)** application for managing a railway transport system, developed entirely in Python. It serves as the first major project for the **Quera Bootcamp (QBC10)**. The system is designed without a graphical user interface (GUI) or an external database, focusing on core programming logic and in-memory data management.

## ✨ Key Features

The system provides three distinct user panels with different levels of access and functionality:

### 👤 Admin Panel
The Super Admin has the highest level of access and is responsible for managing the system's employees.
- **✅ Employee Management**:
  - Add new employees to the system.
  - Remove employees from the system using their username.
  - View a complete list of all registered employees.

### 🛠️ Train Employee Panel
Train Employees are responsible for managing the operational side of the system, namely the lines and trains.
- **✅ Line Management**:
  - Define new lines with an origin, destination, and a list of stations.
  - Update the information of existing lines.
  - Delete railway lines.
- **✅ Train Management**:
  - Add new trains with a unique ID, capacity, ticket price, etc.
  - Remove trains from the system.
  - View a complete list of available trains.

### 🎫 Normal User Panel
The end-users of the system (passengers) can use this panel for the following services:
- **✅ Registration & Login**: Create a new user account and log into the system with personal credentials.
- **✅ Ticket Purchasing**: View the list of active trains and purchase tickets for a desired quantity.
- **✅ Wallet System**:
    - Charge their personal wallet through a simulated bank card validation system.
    - The cost of purchased tickets is deducted from the wallet balance.
- **✅ Ticket Issuing**: After a successful purchase, the ticket information is generated and saved as a text file (`.txt`) for the user.

---

## 🚀 Setup and Installation

To run this project on your local machine, follow these steps:

**1. Clone the Repository:**
First, clone the project from GitHub:
```bash
git clone [https://github.com/YOUR_USERNAME/Railway-Management-System.git](https://github.com/YOUR_USERNAME/Railway-Management-System.git)