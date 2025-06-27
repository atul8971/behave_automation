# Playwright BDD Framework with Page Object Model

This framework combines Playwright with Behave for BDD testing, implementing the Page Object Model pattern for better maintainability and reusability.

## Project Structure

```
├── requirements.txt      # Project dependencies
└── tests/               # Test directory
    ├── environment.py     # Behave environment setup
    ├── features/         # BDD feature files
    │   └── login.feature # Login scenarios
    ├── pages/            # Page Object Model classes
    │   ├── __init__.py
    │   └── login_page.py # Login page elements and actions
    └── steps/            # Step definitions
        ├── __init__.py
        └── login_steps.py # Login step implementations
```

## Setup Instructions

1. Install dependencies:
```bash
# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
playwright install
```

2. Set up your configuration:
- Update URL in behave.ini or pass via command line

## Running Tests

Run all tests:
```bash
behave tests/features
```

Run specific feature:
```bash
behave tests/features/login.feature
```

## Framework Design

### Page Object Model (POM)
The framework uses the Page Object Model pattern to:
- Separate test logic from page interactions
- Encapsulate page elements and their behaviors
- Improve test maintenance
- Make tests more readable and reusable

### Key Components

1. **Page Objects** (`pages/`)
   - Contain element locators
   - Implement page-specific actions
   - Abstract away technical details

2. **Step Definitions** (`steps/`)
   - Implement BDD steps
   - Use page objects for interactions
   - Focus on business logic

3. **Feature Files** (`features/`)
   - Define test scenarios in Gherkin
   - Business-readable test specifications

4. **Environment Setup** (`environment.py`)
   - Handles test setup and teardown
   - Initializes Playwright and page objects
   - Manages browser context