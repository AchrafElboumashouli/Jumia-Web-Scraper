# 🛍️ Jumia Web Scraper

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-green.svg)
![Requests](https://img.shields.io/badge/Requests-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A powerful and colorful Python web scraper that extracts product information from Jumia.ma. This tool helps you quickly gather product names, prices, and links for any search term on Morocco's largest e-commerce platform.

## ✨ Features

- **Product Search**: Search for any product on Jumia.ma
- **Multi-page Scraping**: Automatically scrapes through 50 pages of results
- **Colorful Terminal Output**: Beautiful progress indicators with colored output
- **CSV Export**: Saves results to a CSV file for easy analysis
- **Terminal Preview**: Option to display results directly in the terminal

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- BeautifulSoup4
- Requests library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/jumia-web-scraper.git
cd jumia-web-scraper
```
### Install required dependencies:

```bash
pip install -r requirements.txt
```
### Usage
Run the script with Python:
```bash
python jumia_scraper.py
```
You'll be prompted to:

Enter the product name you want to search for
Choose whether to display results in the terminal
The script will then:

Show a colorful progress bar as it scrapes each page

Save all results to a CSV file named [product_name]_Jumia_Products.csv

Optionally display the results in the terminal

### 📊 Output Example
The script generates a CSV file with the following columns:

Nom: Product name

Prix: Product price in MAD

Lien: Direct link to the product page

###  🎨 Terminal Preview
🚀 scarping : 
![Scraper Demo](./images/scarping.png)
✨ scarping successful :
![Scraper Demo](./images/fin.png)
🛍️ File output : 
![Scraper Demo](./images/outputs.png)
The script displays a colorful progress bar during scraping

### 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

### ⚠️ Disclaimer
This project is for educational purposes only. Please respect Jumia's terms of service and robots.txt file when using this scraper. Use responsibly and consider adding delays between requests to avoid overwhelming the server.

### 📝 License
This project is MIT licensed.

⭐ Star this repo if you found it useful!

### Powered by 🚀 ACHRAF EL BOUMASHOULI 🚀
