# jda-exercise
To run the code, the following instructions must be followed:

1. Install Python: Ensure that Python is installed on the device where you want to run the code. You can download the latest version of Python from the official website (https://www.python.org) and follow the installation instructions specific to your operating system.
2. Install required packages: Open a terminal or command prompt and execute the following commands to install the necessary packages (assuming you have Python and pip installed):

   pip install yfinance
   pip install streamlit  
   pip install pandas
   pip install matplotlib

3. Get the code: Download the code and use an integrated development environment (IDE) of your choice.
4. Run the code: Open a terminal or command prompt, navigate to the directory where you saved the btc_analysis.py file, and execute the following command:

   streamlit run btc.py

This command will start the Streamlit server and launch a web browser with the application.

5. View the results: After executing the command, a new browser tab should open automatically, displaying the Streamlit application. You will see the BTC price data, closing prices, line plot, weeks with price movement, and the bar plot. You can interact with the web page and explore the visualizations.

Note: Make sure the device has an internet connection since the code downloads data from Yahoo! Finance using the yfinance package.
