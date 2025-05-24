# 🚆 Booking KAI POM

Selenium python automation project for testing the ticket booking functionality on the Booking KAI built using the POM and Pytest Fixture

Target: https://booking.kai.id

## 📌 Features

- Automated UI test for train ticket booking from Bandung to Jakarta.
- Clean Page Object Model for better modularity and reusability.
- Uses `pytest` fixtures for setup and teardown of browser sessions.
- Supports interaction with dynamic dropdowns and date pickers.

## 📝 Requirements

- Python 3.8+
- Firefox browser
- Pytest
- Pytest-html
- Pytest-xdist
- Python-dotenv

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/indahyi/booking-kai-pom.git
```

2. Install Virtual Environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the tests:

```bash
pytest
```
