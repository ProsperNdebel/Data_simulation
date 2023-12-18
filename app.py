from flask import Flask, render_template, render_template_string, send_file
from api_handler import fetch_forex_data
from flask import request, jsonify
from flask_cors import CORS
import pandas as pd
import plotly.express as px
import requests


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    """
    Main route that displays the mai interface for the whole app and 
    each individual elements point to a route that handles it.


    Parameters: None

    Returns:
        str: Rendered HTML content for the main menu.
    """

    return render_template('menu.html')


@app.route('/plot_data', methods=['POST'])
def plot_data():
    """
    Endpoint to receive JSON data and convert it to a specific format for chart rendering.

    This function expects a POST request with JSON data containing date, open, high, low, and close values.
    It converts this data into a specific JSON format suitable for rendering a chart.

    Returns:
        JSON response containing the chart data.
    """
    # Get the JSON data from the request
    data = request.get_json()

    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)

    # Convert the DataFrame to the desired JSON format
    chartjs_data = {
        'date': df['date'].tolist(),
        'open': df['open'].tolist(),
        'high': df['high'].tolist(),
        'low': df['low'].tolist(),
        'close': df['close'].tolist()
    }

    # Print the 'date' values for debugging (you can remove this line in production)
    print(chartjs_data['date'])

    # Return the JSON response
    return jsonify(data=chartjs_data)


0


@app.route('/fetch_forex_data', methods=['POST'])
def fetch_forex_data0():
    """
    Endpoint to fetch Forex data within a specified date range and interval.

    This function expects a POST request with JSON data containing the following parameters:
    - startDate: The start date for fetching Forex data.
    - endDate: The end date for fetching Forex data.
    - frame: The time interval for data (e.g., '1H' for 1-hour intervals).
    - currency: The currency pair to fetch data for (e.g., 'EURUSD').

    It makes an API call to fetch Forex data for the specified parameters and returns the data in JSON format.

    Returns:
        JSON response containing the fetched Forex data.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extracting the parameters
        start_date = data.get('startDate')
        end_date = data.get('endDate')
        interval = data.get('frame')
        currency = data.get('currency')

        # Making the API call to fetch Forex data
        data = fetch_forex_data(
            currency, 'EURUSD', start_date, end_date, interval)

        # Convert the fetched data to JSON format
        data_json = data.to_json(orient='records')
        print(data_json)

        # Return the JSON response
        return jsonify({'result': data_json})

    except Exception as e:
        # Handle exceptions and return an error response
        print(f"Error: {str(e)}")
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/get_weather_data', methods=['POST'])
def get_weather_data():
    """
    Endpoint to fetch weather data for a specified location and date range.

    This function expects a POST request with JSON data containing the following parameters:
    - location: The location for which weather data is requested.
    - startDate: The start date for fetching weather data.
    - endDate: The end date for fetching weather data.
    - timeFrame: The time frame or interval for weather data (e.g., '1h' for hourly data).
    - weatherElements: A list of weather elements to include in the data.

    It makes an API call to the Visual Crossing Weather API to retrieve weather data based on the provided parameters.

    Returns:
        JSON response containing the fetched weather data.
    """
    api_key = '93WH8JAHRT6LTFNRJJ2H4HYQJ'  # Replace with your API key

    try:
        # Get JSON data from the request
        form_data = request.get_json()

        # Retrieve the selected location and other parameters
        location = form_data.get("location")
        start_date = form_data.get('startDate')
        end_date = form_data.get('endDate')
        time_frame = form_data.get('timeFrame')
        weather_elements = form_data.get('weatherElements')

        # Construct the API URL with the provided parameters and API key
        API_URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?key={api_key}"

        # Make the API call to Visual Crossing Weather API
        res = requests.get(API_URL)

        # Print the API response for debugging purposes (can be removed in production)
        print(res.json())

        # Return the JSON response containing the fetched weather data
        return jsonify(res.json())

    except Exception as e:
        # Handle exceptions and return an error response
        print(f"Error: {str(e)}")
        return jsonify({'error': 'An error occurred'}), 500


# Dictionary to store data for different options, acts a simple database
data_dict = {}


@app.route("/store_data", methods=["POST"])
def store_data():
    """
    Endpoint to store data in a dictionary.

    This function expects a POST request with JSON data containing the following parameters:
    - option: The option or key under which to store the data.
    - data: The data value to be stored.

    It stores the data in a dictionary called `data_dict`, using the provided option as the key.
    If the key already exists in the dictionary, the new data value is appended to the existing list of values.
    If the key doesn't exist, a new key-value pair is created with the provided option and data value.

    Returns:
        JSON response indicating the success or failure of data storage.
    """
    try:
        data = request.get_json()
        option = data.get("option")
        data_value = data.get("data")

        if option in data_dict:
            # If the option already exists in data_dict, append the data_value to the existing list
            data_dict[option].append(data_value)
        else:
            # If the option doesn't exist, create a new key-value pair
            data_dict[option] = [data_value]

        return jsonify({"message": "Data stored successfully"})

    except Exception as e:
        # Handle exceptions and return an error response with a 500 status code if an exception occurs
        return jsonify({"error": str(e)}), 500


@app.route("/get_plot_data", methods=["POST"])
def get_plot_data():
    """
    Endpoint to retrieve plot data for a specific option from the data dictionary.

    This function expects a POST request with JSON data containing the following parameter:
    - option: The option for which plot data is requested.

    It retrieves data for the selected option from the `data_dict` dictionary, which should have been populated
    using the 'store_data' endpoint. The retrieved data is returned in a JSON format suitable for plotting.

    Returns:
        JSON response containing the plot data if the option exists in the data dictionary.
        JSON response with an error message if the option is not found or if an error occurs.
    """
    try:
        data = request.get_json()
        option = data.get("option")

        # Check if data for the selected option exists in data_dict
        if option in data_dict:
            # Generate dates as a list of integers from 1 to the length of progress data
            dates = [i for i in range(1, len(data_dict[option]) + 1)]
            progress_data = data_dict[option]

            plot_data = {
                "dates": dates,
                "progressData": progress_data,
            }

            return jsonify(plot_data)
        else:
            # Return an error response if the option is not found in data_dict
            return jsonify({"error": "No data available for this option"}), 404
    except Exception as e:
        # Handle exceptions and return an error response with a 500 status code if an exception occurs
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=6002)
