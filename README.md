# Shopping Cart Checkout System - TDD Exercise

A test-driven development practice project implementing a shopping cart checkout system with discount functionality using Python and pytest.

## 🎯 Overview

This project demonstrates TDD principles by implementing a flexible checkout system that handles:
- Dynamic item inventory management
- Shopping cart operations
- Bulk discount/promotion system
- Comprehensive error handling
- Complete test coverage

The implementation follows clean code principles with a focus on maintainability and extensibility.

## 🛠️ Technologies Used

- **Python 3.x** - Core implementation language
- **pytest** - Testing framework with fixtures and assertions
- **TDD Methodology** - Test-first development approach

## ✨ Features

### Core Functionality
- ✅ Add items to inventory with custom pricing
- ✅ Add items to shopping cart with quantity tracking
- ✅ Calculate cart totals with automatic pricing
- ✅ Apply bulk discount rules (e.g., "buy 3 for $2")
- ✅ Robust error handling for invalid items
- ✅ Flexible discount system supporting various promotion types

### Discount System
- **Bulk Discounts**: Buy N items for a special price
- **Automatic Application**: Discounts apply when quantity thresholds are met
- **Partial Discounts**: Remaining items charged at regular price
- **Multiple Item Support**: Different discount rules per item

## 🚀 Quick Start

### Prerequisites
```bash
pip install pytest
```

### Running the Tests
```bash
# Run all tests with verbose output
pytest TestCheckout.py -v

# Run tests with coverage (if pytest-cov installed)
pytest TestCheckout.py --cov=Checkout

# Run specific test
pytest TestCheckout.py::test_can_apply_discount_rule -v
```

### Basic Usage Example
```bash
from Checkout import Checkout

# Create checkout system
checkout = Checkout()

# Add items to inventory
checkout.add_item_price_to_inventory("apple", 0.50)
checkout.add_item_price_to_inventory("banana", 0.30)

# Add discount: buy 3 apples for $1.00
checkout.add_discount("apple", 3, 1.00)

# Add items to cart
checkout.add_item_to_cart("apple")
checkout.add_item_to_cart("apple")
checkout.add_item_to_cart("apple")
checkout.add_item_to_cart("banana")

# Calculate total (discount applied automatically)
total = checkout.calculate_cart_total()  # $1.30
```

## Project Structure
```bash
checkout-kata
|-- Checkout.py
|-- README.md
|-- TestCheckout.py
|-- Checkout.py
-- __init__.py
```

### Code Architecture

**`Checkout.py`**
- `Checkout` class: Main checkout system
- `Discount` nested class: Discount rule definition
- Key methods: `add_item_to_cart()`, `calculate_cart_total()`, `add_discount()`

**`TestCheckout.py`**
- pytest fixture setup for consistent test data
- Comprehensive test coverage including edge cases
- Exception testing for error handling

## 🧪 Test Coverage

The test suite covers all critical functionality:

| Test Case | Description |
|-----------|-------------|
| `test_can_calculate_total` | Basic single item calculation |
| `test_get_correct_total_with_multiple_items` | Multi-item cart totals |
| `test_can_add_discount_rule` | Discount rule creation |
| `test_can_apply_discount_rule` | Bulk discount application |
| `test_exception_with_bad_item` | Error handling for invalid items |

### Test Features Demonstrated
- **pytest fixtures**: Reusable test setup with `@pytest.fixture()`
- **Assertions**: Multiple assertion types for validation
- **Exception testing**: `pytest.raises()` for error scenarios
- **Test isolation**: Each test runs independently

## 💡 Learning Objectives & TDD Process

This project practices key software development concepts:

### Test-Driven Development Workflow
1. **Red**: Write failing test first
2. **Green**: Write minimal code to pass test
3. **Refactor**: Improve code while keeping tests green

### Python Testing Best Practices
- Fixture-based test setup for consistency
- Clear, descriptive test names
- Comprehensive edge case coverage
- Separation of test data and test logic

### Object-Oriented Design Patterns
- Single Responsibility Principle
- Encapsulation of discount logic
- Clean method interfaces

## 🔮 Future Enhancements

Potential extensions for continued learning:
- [ ] Percentage-based discounts (e.g., 10% off)
- [ ] Multiple discount types per item
- [ ] Cart item removal functionality
- [ ] Tax calculation system
- [ ] JSON-based inventory loading
- [ ] Performance testing for large inventories

## 🎓 Skills Demonstrated

- **Python Programming**: Clean, readable object-oriented code
- **Test-Driven Development**: Systematic test-first approach
- **pytest Framework**: Fixtures, assertions, exception handling
- **Algorithm Design**: Discount calculation logic
- **Error Handling**: Robust input validation
- **Code Organization**: Logical separation of concerns

---

*This project showcases practical Python development skills with a focus on testing excellence and clean code principles.*
