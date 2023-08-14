# Housing Price Prediction Web App

This web application allows users to predict housing prices in **Bangalore** based on various input parameters such as location, area, number of bathrooms, and BHK (bedroom, hall, kitchen). The prediction is made using a machine learning model trained on housing data specific to Bangalore.

## Features

- Input form to specify location, area, number of bathrooms, and BHK.
- Dynamic selection of predefined Bangalore locations.
- Display of predicted price based on user inputs.
- User-friendly interface.

## Prerequisites

- Python (version 3.6 or higher)
- Flask (install via requirements or separately)
- NumPy, pandas (install via requirements or separately)
- scikit-learn (install via requirements or separately)
- jQuery (included via CDN in the HTML template)
- Bootstrap (included via CDN in the HTML template)

## Installation

1. Clone or download the repository to your local machine.
2. Navigate to the project directory:

    ```bash
    cd Housing-Price-Prediction
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app using the following command:

    ```bash
    python app.py
    ```

2. Open your web browser and visit `http://localhost:5000` to access the web app.

3. Fill in the form with the required input parameters: location, area, number of bathrooms, and BHK.

4. Click the "Predict Price" button to see the predicted housing price based on your inputs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
