# Tropical Fish Database

A web application for managing information about tropical pet fish. This application allows you to store, view, edit, and delete information about different types of tropical fish, including their characteristics, care requirements, and other important details.

## Features

- Add new fish entries with detailed information
- View a list of all fish in a grid layout
- View detailed information about individual fish
- Edit existing fish entries
- Delete fish entries
- Responsive design that works on all devices

## Information Stored

For each fish, the following information is stored:
- Common name
- Scientific name
- Family
- Maximum size (in centimeters)
- Minimum tank size (in liters)
- Temperature range (in Celsius)
- pH range
- Diet
- Temperament
- Description
- Date added

## Setup Instructions

1. Make sure you have Python 3.7 or higher installed on your system.

2. Clone this repository or download the files to your local machine.

3. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. **Adding a New Fish**
   - Click the "Add Fish" button in the navigation bar
   - Fill in the required information
   - Click "Add Fish" to save

2. **Viewing Fish**
   - The home page displays all fish in a grid layout
   - Click on any fish card to view its detailed information

3. **Editing Fish**
   - View the fish details
   - Click the "Edit" button
   - Make your changes
   - Click "Save Changes"

4. **Deleting Fish**
   - View the fish details
   - Click the "Delete" button
   - Confirm the deletion

## Technologies Used

- Python Flask
- SQLite Database
- Bootstrap 5
- Bootstrap Icons

## Contributing

Feel free to submit issues and enhancement requests! 
