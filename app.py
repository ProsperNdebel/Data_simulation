from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Main route that displays the mai interface for the whole app and 
    each individual elements point to a route that handles it.


    Parameters: None

    Returns:
        str: Rendered HTML content for the main menu.
    """
    # You can customize this data with the necessary information for your menu
    menu_data = {
        'menu_items': [
            {'label': 'Plot Data', 'url': '/plot_data'},
            {'label': 'Simulate Data', 'url': '/simulate_data'},
            {'label': 'Pick Data Type', 'url': '/pick_data_type'},
            # Add more menu items as needed
        ],
        'app_name': 'Data Simulation Project'
    }

    return render_template('menu.html', **menu_data)


# Sample/dummy data for demonstration purposes
sample_data = {
    'data_for_plot': [1, 2, 3, 4, 5],
    'simulated_data': [5, 4, 3, 2, 1],
    'available_data_types': ['Type A', 'Type B', 'Type C']
}

# Define a route for plotting data


@app.route('/plot_data')
def plot_data():
    """
    Route to display a visualization of the data .

    Returns:
        str: Rendered HTML content for the data plotting page.
    """
    return render_template('plot_data.html', data=sample_data['data_for_plot'])

# Define a route for simulating data


@app.route('/simulate_data')
def simulate_data():
    """
    Route to simulate changes in data as an animation of a matplotlib
    graph

    Parameters:
    -  None

    Returns:
        str: Rendered HTML content for the data simulation page.
    """
    return render_template('simulate_data.html', simulated_data=sample_data['simulated_data'])

# Define a route for picking data types


@app.route('/pick_data_type')
def pick_data_type():
    """
    Route to pick a specific data type.

    Returns:
        str: Rendered HTML content for the data type picking page.
    """
    return render_template('pick_data_type.html', data_types=sample_data['available_data_types'])


if __name__ == '__main__':
    app.run(debug=True)
