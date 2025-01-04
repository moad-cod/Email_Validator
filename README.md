# **Email Validation with Python**

### **Overview**
This project provides a Python script to validate email addresses using two methods:
1. **Manual Validation**: Checks email structure and content with conditional statements.
2. **Regex Validation**: Uses regular expressions for robust and concise validation.

---

### **Features**
- Ensures the email has:
  - At least 6 characters.
  - Exactly one "@" symbol.
  - A valid domain ending with `.com`, `.org`, `.net`, etc.
- Detects invalid characters like spaces, uppercase letters, or special symbols in invalid positions.
- Utilizes regex for advanced validation.

---

### **Technologies Used**
- **Python 3.x**
- **Regex** (`re` module)

---

### **Validation Logic**
#### 1. **Manual Validation**
- Checks:
  - Email length (`>= 6`).
  - Presence and count of `@` symbol.
  - Valid position for the dot (`.`) using XOR (`^`).
  - Invalid characters (spaces, uppercase letters, unsupported symbols).

#### 2. **Regex Validation**
- Regex Pattern: 
  ```regex
  ^[a-zA-Z0-9]+[@][a-zA-Z0-9]+[.][a-zA-Z0-9]{2,3}$
