# Bakehouse Dataset

The **Bakehouse Dataset** simulates a bakery franchise business, providing rich data for analytics, data pipelines, and AI/ML use cases. It contains information about sales transactions, customers, franchises, suppliers, and customer reviews, enabling comprehensive business analysis.

## Table Overview

### 1. `sales_customers`
**Description:**  
Customer demographic and contact information.

**Schema:**  
- `customerID` (bigint)  
- `first_name` (string)  
- `last_name` (string)  
- `email_address` (string)  
- `phone_number` (string)  
- `address` (string)  
- `city` (string)  
- `state` (string)  
- `country` (string)  
- `continent` (string)  
- `postal_zip_code` (bigint)  
- `gender` (string)

---

### 2. `sales_franchises`
**Description:**  
Franchise location, size, and supplier linkage.

**Schema:**  
- `franchiseID` (bigint)  
- `name` (string)  
- `city` (string)  
- `district` (string)  
- `zipcode` (string)  
- `country` (string)  
- `size` (string)  
- `longitude` (double)  
- `latitude` (double)  
- `supplierID` (bigint)

---

### 3. `sales_suppliers`
**Description:**  
Supplier details, ingredients, and approval status.

**Schema:**  
- `supplierID` (bigint)  
- `name` (string)  
- `ingredient` (string)  
- `continent` (string)  
- `city` (string)  
- `district` (string)  
- `size` (string)  
- `longitude` (double)  
- `latitude` (double)  
- `approved` (string)

---

### 4. `sales_transactions`
**Description:**  
Sales transaction records, including products, prices, and payment methods.

**Schema:**  
- `transactionID` (bigint)  
- `customerID` (bigint)  
- `franchiseID` (bigint)  
- `dateTime` (timestamp)  
- `product` (string)  
- `quantity` (bigint)  
- `unitPrice` (bigint)  
- `totalPrice` (bigint)  
- `paymentMethod` (string)  
- `cardNumber` (bigint)

---