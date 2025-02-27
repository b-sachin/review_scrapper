# Review Scraper

This repository contains a web application designed to scrape and analyze product reviews from e-commerce websites. The application extracts user reviews, processes the textual data, and provides insights into customer sentiments.

## Features

- **Web Scraping**: Extracts product reviews from specified e-commerce platforms.
- **Text Processing**: Cleans and preprocesses the scraped reviews for analysis.
- **Sentiment Analysis**: Determines the sentiment polarity of customer reviews.
- **Web Interface**: Provides a user-friendly interface to input product URLs and view analysis results.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/b-sachin/review_scrapper.git
   cd review_scrapper
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:

   ```bash
   python local_app.py
   ```

2. **Access the web interface**:

   Open your web browser and navigate to `http://localhost:5000`.

3. **Analyze reviews**:

   - Enter the URL of the product page you wish to analyze.
   - Click on the "Scrape Reviews" button.
   - View the extracted reviews and sentiment analysis results displayed on the page.

## Project Structure

```
review_scrapper/
├── .idea/                  # Project configuration files
├── templates/              # HTML templates for the web interface
├── local_app.py            # Main application script
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

## Dependencies

The project relies on the following Python packages:

- Flask
- Requests
- BeautifulSoup4
- TextBlob

Ensure all dependencies are installed by running the command mentioned in the Installation section.

## Contributing

Contributions are welcome! If you'd like to enhance the functionality or fix issues, please follow these steps:

1. **Fork the repository** to your GitHub account.
2. **Create a new branch** for your feature or bugfix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** and commit them with descriptive messages.
4. **Push your changes** to your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request** detailing your changes and the motivation behind them.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

