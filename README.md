# BDD Automation Framework 🚀

## 📌 Overview
This is a **BDD (Behavior-Driven Development) automation framework** using **Selenium and Python** for automating the sign-up and login flow on [Magento Test Website](https://magento.softwaretestingboard.com/). It follows the **Page Object Model (POM)** to ensure maintainability and scalability.

---

## 🛠 Tech Stack
- **Programming Language:** Python 🐍
- **Test Framework:** Behave (BDD)
- **Web Automation:** Selenium WebDriver 🌐
- **Assertions:** Pytest
- **Reports:** Allure
- **Version Control:** Git & GitHub

---

## 📂 Project Structure
```
BDD-Automation/
│── features/               # BDD feature files
│   ├── login.feature       # Login test scenarios
│   ├── signup.feature      # Signup test scenarios
│── steps/                  # Step definitions
│   ├── login_steps.py      # Login step implementation
│   ├── signup_steps.py     # Signup step implementation
│── pages/                  # Page Object Model classes
│   ├── login_page.py       # Login page elements
│   ├── signup_page.py      # Signup page elements
│── config/                 # Configuration files
│── reports/                # Test execution reports
│── screenshots/            # Screenshots of test runs
│── requirements.txt        # Python dependencies
│── run_tests.py            # Script to execute tests
│── README.md               # Project documentation
```

---

## 🔧 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/gaganshetty07/bdd-automation.git
cd bdd-automation
```
### 2️⃣ Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```
### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 🚀 Running the Tests
### 1️⃣ Run All Tests
```sh
behave
```
### 2️⃣ Run Tests with HTML Report
```sh
behave --format html --outfile reports/test_report.html
```
### 3️⃣ Run Specific Feature
```sh
behave features/login.feature
```

---

## 📸 Screenshots
Screenshots of test execution will be available in the `screenshots/` directory.

---

## 🤝 Contribution Guidelines
1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to the branch and submit a PR.

---

## 📜 License
This project is open-source. Feel free to contribute!

---

📌 **Author:** [Gagan Shetty](https://github.com/gaganshetty07)
