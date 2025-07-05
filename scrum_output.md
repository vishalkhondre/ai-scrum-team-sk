# 📋 Scrum AI Team Deliverables

## None
We need a system that lets customers order groceries online, select same-day delivery, pay by credit card or wallet, and use promo codes. The system must support secure user registration and order tracking.

## None
Transferred to ProductOwner

## ProductOwner
### System Requirements Specification (SRS)

#### 1. Project Overview  
**System Name:** Online Grocery Ordering System  
**Purpose:**  
The Online Grocery Ordering System aims to provide customers with a convenient platform to order groceries online, choose same-day delivery options, make secure payments, apply promo codes for discounts, and track their orders in real-time. The system will include secure user registration, authentication, and access control mechanisms to ensure data safety and personalized user experience.

---

#### 2. Business Requirements  
- **BR 1:** Allow customers to browse and order groceries online.  
- **BR 2:** Enable same-day delivery scheduling for orders.  
- **BR 3:** Provide secure payment options via credit card or wallet.  
- **BR 4:** Support the use of promo codes for discounts.  
- **BR 5:** Implement secure user registration and login processes.  
- **BR 6:** Allow customers to track orders in real-time.  

---

#### 3. System Requirements  

**3.1. Functional Requirements**  
1. **User Registration & Login**  
   - The system should support secure user registration with basic information (name, email, phone number, password).  
   - Users should be able to log in using their registered email and password.  
   - Passwords should be encrypted and follow industry-standard security protocols.  

2. **Browse Groceries**  
   - Users should be able to view a categorized list of groceries (e.g., fruits, vegetables, dairy).  
   - Each grocery item should display details such as name, price, image, description, and stock availability.  

3. **Order Placement**  
   - Users should be able to add items to a cart with the option to modify quantities before checkout.  
   - The system should validate stock availability at checkout.

4. **Delivery Scheduling**  
   - Users should have the option to select same-day delivery if orders are confirmed before a specific daily cutoff time (e.g., 2:00 PM).  
   - Delivery slots should be configurable (e.g., hourly time windows) and visible during checkout.  

5. **Payment Processing**  
   - The system should support payments via credit cards or wallets.  
   - Payments should be processed securely using industry-standard encryption (e.g., HTTPS, PCI compliance).  

6. **Promo Code Application**  
   - Users should be able to input promo codes during checkout.  
   - The system should validate the promo code, calculate the applicable discount, and display the updated order total.  
   - Promo codes should have configurable rules (e.g., expiry, usage limits, minimum order value).  

7. **Order Tracking**  
   - Users should be able to view order updates (e.g., "Preparing," "Out for Delivery," "Delivered") through the application.  
   - Real-time order tracking should display delivery driver location using integrated mapping APIs.  

---

**3.2. Non-Functional Requirements**  
1. **Performance**  
   - The system should handle up to 5,000 concurrent users during peak hours without degrading response times beyond 1 second.  

2. **Security**  
   - All customer data should be encrypted in transit and at rest.  
   - Only authorized users should access their personal account data.  
   - The system should comply with GDPR for handling personal information.

3. **Scalability**  
   - The system should support future scalability to accommodate growing user volumes and geographic expansion.  

4. **User Interface (UI)**  
   - The system should have an intuitive and responsive web and mobile interface compatible with modern browsers and devices.  

---

#### 4. Constraints  
1. Orders must be confirmed before the cutoff time to qualify for same-day delivery.  
2. Promo codes must be configured by the admin before use; users cannot create their own codes.  
3. Real-time tracking requires integration with third-party mapping APIs (e.g., Google Maps or similar).

---

#### 5. Assumptions  
1. Customers are proficient with basic usage of online platforms and mobile applications.  
2. The grocery catalog data, including stock levels, is updated regularly to ensure accuracy.  
3. Same-day delivery is limited to specific serviceable locations.  

---

#### 6. Business Rules  
1. Delivery slots should be restricted to operational hours (e.g., 8:00 AM - 10:00 PM).  
2. Promo codes cannot be combined; only one promo code may be applied per order.  
3. Wallet payments should allow users to top up their wallet balance within the platform.  
4. Cancellation after order confirmation is not allowed for same-day delivery unless approved by an admin under special circumstances.

--- 

#### 7. Summary  
This system intends to streamline the grocery ordering and delivery process, offering secure and user-friendly features with a focus on customer convenience, tracking, and payment flexibility. It is expected to adhere to industry-standard security protocols while maintaining scalability to support business growth. 



## None
Transferred to BusinessAnalyst

## BusinessAnalyst
### Breakdown of SRS into Agile User Stories and Acceptance Criteria
Each user story is written in the “As a...I want...So that...” format and is followed by acceptance criteria in the **Given/When/Then** format.  

---

### Epic 1: User Registration and Login

#### User Story 1.1: User Registration
**As a** customer  
**I want to** register for an account by entering my personal details  
**So that** I can access the grocery ordering system securely  

**Acceptance Criteria:**  
- **Scenario 1:** Successful registration  
  - Given I am on the registration page  
  - When I enter valid details (name, email, phone number, password) and click "Register"  
  - Then my account should be created successfully  
  - And I should see a confirmation message  

- **Scenario 2:** Failure due to invalid/missing data  
  - Given I am on the registration page  
  - When I leave mandatory fields blank or enter invalid data (e.g., invalid email format)  
  - Then the system should display an error message and prevent registration  

- **Scenario 3:** Duplicate email  
  - Given my email is already registered  
  - When I attempt to register with the same email  
  - Then I should see an error message indicating the email is already in use  

---

#### User Story 1.2: User Login
**As a** registered customer  
**I want to** log in using my email and password  
**So that** I can access my personalized grocery account  

**Acceptance Criteria:**  
- **Scenario 1:** Successful login  
  - Given I am a registered user  
  - When I enter valid credentials (email and password)  
  - Then I should be redirected to my dashboard  

- **Scenario 2:** Unsuccessful login due to incorrect credentials  
  - Given I am on the login page  
  - When I enter an incorrect email or password  
  - Then I should see an error message indicating invalid credentials  

- **Scenario 3:** Password recovery  
  - Given I forgot my password  
  - When I click the “Forgot Password” link and complete the recovery process  
  - Then I should receive a password reset email  

---

### Epic 2: Grocery Catalog and Cart Management

#### User Story 2.1: Browse and View Groceries  
**As a** customer  
**I want to** browse a categorized list of groceries  
**So that** I can find items I need  

**Acceptance Criteria:**  
- **Scenario 1:** View categories  
  - Given I am on the grocery catalog page  
  - When I select a category (e.g., "Fruits")  
  - Then only items in that category should be displayed  

- **Scenario 2:** View item details  
  - Given I am on the grocery catalog  
  - When I click on an item  
  - Then I should see the item name, price, description, image, and availability  

---

#### User Story 2.2: Add Items to Cart
**As a** customer  
**I want to** add grocery items to my cart  
**So that** I can review them before placing an order  

**Acceptance Criteria:**  
- **Scenario 1:** Add an item to cart  
  - Given I am viewing an item  
  - When I click on "Add to Cart"  
  - Then the item should be added to my cart  

- **Scenario 2:** Modify quantities in cart  
  - Given I have items in my cart  
  - When I update the quantity for an item  
  - Then the system should adjust the cart total accordingly  

---

### Epic 3: Checkout and Payment

#### User Story 3.1: Same-Day Delivery Scheduling
**As a** customer  
**I want to** choose a delivery slot during checkout  
**So that** I can schedule my order delivery  

**Acceptance Criteria:**  
- **Scenario 1:** View available delivery slots  
  - Given I am at the checkout page  
  - When I choose "Same-Day Delivery"  
  - Then I should see available slots for the day  

- **Scenario 2:** Cutoff time validation  
  - Given the current time is past the cutoff (e.g., 2:00 PM)  
  - When I attempt to select same-day delivery  
  - Then the system should display a message explaining the unavailability of same-day delivery  

---

#### User Story 3.2: Apply Promo Code  
**As a** customer  
**I want to** apply a promo code at checkout  
**So that** I can avail a discount on my order  

**Acceptance Criteria:**  
- **Scenario 1:** Successful promo code application  
  - Given I am on the checkout page  
  - When I enter a valid promo code  
  - Then the discount should be applied to the total, and I should see the updated amount  

- **Scenario 2:** Invalid promo code  
  - Given I enter an expired or invalid promo code  
  - When I click "Apply"  
  - Then I should see an error message indicating the issue  

- **Scenario 3:** Minimum order value check  
  - Given the order total does not satisfy the promo code's minimum order value  
  - When I attempt to apply the code  
  - Then I should see a message explaining why the code cannot be applied  

---

#### User Story 3.3: Secure Payment  
**As a** customer  
**I want to** pay for my groceries securely using a credit card or wallet  
**So that** I can complete my order  

**Acceptance Criteria:**  
- **Scenario 1:** Successful payment  
  - Given I am on the payment page  
  - When I enter valid payment details and confirm the payment  
  - Then the payment should be processed successfully  

- **Scenario 2:** Payment failure  
  - Given I am on the payment page  
  - When I provide invalid/expired credit card details  
  - Then I should see an error message  

---

### Epic 4: Order Tracking

#### User Story 4.1: View Order Status
**As a** customer  
**I want to** view the current status of my order  
**So that** I can stay updated on its progress  

**Acceptance Criteria:**  
- **Scenario 1:** Order tracking  
  - Given I have placed an order  
  - When I navigate to the "My Orders" page  
  - Then I should see the current status of my order (e.g., "Preparing," "Out for Delivery")  

- **Scenario 2:** Real-time location tracking  
  - Given my order is "Out for Delivery"  
  - When I view the tracking section  
  - Then I should see the real-time location of the delivery driver on a map  

---

### Epic 5: Security

#### User Story 5.1: Secure Handling of Customer Data
**As a** system  
**I want to** encrypt user data  
**So that** customer information is protected against unauthorized access  

**Acceptance Criteria:**  
- **Scenario 1:** Data encryption  
  - Given customer data is stored in the database  
  - Then it should be encrypted at rest and in transit following industry standards (e.g., AES, HTTPS)  

--- 

These user stories and their acceptance criteria follow Agile principles by being small, testable, and customer-centric.

## None
Transferred to SolutionArchitect

## SolutionArchitect
### High-Level Solution Architecture for Online Grocery Ordering System

To meet the requirements outlined above, the solution architecture will consist of several major components, system interactions, and infrastructure considerations to ensure optimal performance, scalability, and security.

---

### 1. Major Components
Here’s an overview of the key components and their responsibilities in the system:

#### **a. Frontend**
- **Purpose:** Provides the user interface for customers to interact with the system.
- **Technology Options:** React.js, Angular, or Vue.js for web; React Native or Flutter for mobile application.
- **Functionality:**
  - Registration/Login
  - Grocery browsing and search
  - Cart management
  - Promo code application
  - Delivery slot selection
  - Payment initiation
  - Order tracking via a map API (e.g., Google Maps).
- **Dependencies:** API for backend interactions.

#### **b. Backend**
- **Purpose:** Core business logic and data processing.
- **Technology Options:** Node.js, Python (Django/Flask), Java (Spring Boot).
- **Functionality:**
  - User authentication (OAuth2/jwt-based login)
  - Grocery management (catalog, inventory management)
  - Cart/business logic (e.g., applying promo codes, price calculations)
  - Payment integration (gateway APIs like Stripe or PayPal)
  - Delivery scheduling and notification handling
  - Order tracking state updates
- **Dependencies:** Database and third-party integrations.

#### **c. Database**
- **Purpose:** Stores all data for the system (customer information, grocery catalog, orders, promo codes, etc.).
- **Technology Options:** 
  - **Relational DB:** PostgreSQL, MySQL for structured data like customers, orders, and catalog.
  - **NoSQL DB:** MongoDB for flexible or document-based data modes (e.g., order states, delivery tracking logs).
- **Key Tables/Collections:** 
  - User profiles
  - Grocery catalog
  - Cart items
  - Orders (with delivery status)
  - Payment transactions
  - Promo codes

#### **d. Payment Gateway Integration**
- **Purpose:** Provides secure payment processing for credit cards and wallets.
- **Technology Options:** Stripe, PayPal, Razorpay, etc.
- **Functionality:**
  - Ensure PCI compliance for credit card data.
  - Handle wallet top-ups.
  - Generate payment confirmation or failure status.

#### **e. Mapping and Delivery API**
- **Purpose:** Enables delivery tracking and scheduling.
- **Technology Options:** Google Maps API, OpenStreetMap API.
- **Functionality:**
  - Geolocation and real-time tracking for delivery drivers.
  - Display delivery paths to customers.

#### **f. Notification Service**
- **Purpose:** Alerts customers about order updates and delivery status.
- **Technology Options:** Firebase Cloud Messaging (FCM) for mobile push notifications or email services like SendGrid.
- **Functionality:**
  - Order confirmation via email.
  - Push updates for delivery status changes.
  - Promo code notifications.

#### **g. Authentication and Security**
- **Purpose:** Secures user identities and data.
- **Technology Options:** OAuth 2.0 with JWT or AWS Cognito.
- **Functionality:**
  - Password hashing (e.g., bcrypt, Argon2).
  - Two-factor authentication (optional future feature).

---

### 2. System Interactions

#### **User Journey Examples**
1. **Order Placement Workflow:**  
   - Customer accesses the frontend to browse groceries → Adds items to cart → Selects delivery slot and applies promo code → Initiates payment via backend API → Payment gateway processes transaction → Order confirmation is generated → Backend updates order database and notifies delivery personnel.  

2. **Order Tracking Workflow:**  
   - Backend continuously updates order status (e.g., "Preparing," "Out for Delivery") → Sends updates to the frontend via REST APIs or WebSockets → For real-time driver location tracking, backend uses mapping API to retrieve driver GPS coordinates and sends data to frontend.

3. **Delivery Location Tracking:**  
   - Delivery personnel shares their location via a mobile app → Mapping API processes location data and updates in real time → Frontend displays the current location to the customer using map overlay.

---

### 3. Infrastructure Needs

#### **a. Hosting and Compute Services**
- **Compute:** Cloud-based infrastructure such as AWS, Azure, or Google Cloud. Use containerized services like Docker and orchestration with Kubernetes for scalability.
- **Storage:** Cloud-managed database solutions (Amazon RDS and DynamoDB for mixed SQL/NoSQL needs).
- **Load Balancing:** Use elastic load balancers to handle traffic spikes during launch or peak hours.

#### **b. Security Measures**
- Encrypt all sensitive data at rest and in transit (e.g., HTTPS for all endpoints, AES encryption for database fields).
- Use a Web Application Firewall (WAF) to protect against common threats (e.g., SQL injection, XSS).
- Ensure PCI compliance for payment processing.

#### **c. Scalability**
- Use autoscaling for both frontend and backend servers to ensure performance during high traffic periods.
- Leverage CDN (e.g., AWS CloudFront) to optimize static content delivery.

#### **d. Backup and Disaster Recovery**
- Daily database backups.
- Version-controlled deployment with rollback options.

---

### 4. Key Technical Dependencies and Risks  
#### **Dependencies**
1. Mapping API (Google Maps or equivalent) for real-time delivery tracking.
2. Payment Gateway for secure checkout functionality.
3. Notification services (email or push notifications) for updates.
4. Cloud provider offering scalable hosting solutions.

#### **Risks**
1. **Promo Code Misuse:** Risk of promo codes being exploited or applied over limits. Mitigation: Add validation mechanisms for promo codes (expiry, usage cap, etc.).
2. **Delivery Delays:** Risk of failing to fulfill same-day delivery during peak periods. Mitigation: Add configurable delivery cutoff time and enforce order caps during peak hours.
3. **Data Breaches:** Customer data must be protected against unauthorized access. Mitigation: Implement advanced encryption, access control, and regular vulnerability patching.

---

### 5. Additional Technical User Stories Required

1. **As a system, I want to validate delivery zones based on the customer’s postal code so that same-day delivery is restricted to serviceable areas.**
2. **As a system, I want to notify the delivery personnel with order details and customer address so that they can prepare for delivery.**
3. **As a system, I want to encrypt sensitive payment data (e.g., credit card numbers) so that customer financial details remain secure.**
4. **As a system, I want to dynamically allocate delivery slots based on order volume so that same-day delivery operations remain feasible.**
5. **As a system, I want to trigger backup processes for the database every 12 hours so that I can enable data recovery in case of an outage.**

---

The architecture above provides a modular, scalable, and secure foundation for the Online Grocery Ordering System, meeting both the functional and non-functional requirements.

## None
Transferred to QATester

## QATester
### Test Scenarios and Test Cases in Gherkin Syntax

Using the given requirements and user stories, here are detailed test scenarios written in Gherkin syntax. Each feature is comprehensively tested to cover positive, negative, and edge cases.

---

### Feature: User Registration and Login

#### Scenario: Successful registration
```gherkin
Given the customer is on the registration page
When they enter valid details (name, email, phone number, password)
And click "Register"
Then the system should create a new account
And display a success message
```

#### Scenario: Registration fails due to invalid data
```gherkin
Given the customer is on the registration page
When they leave mandatory fields blank or enter invalid details (e.g., incorrect email format)
And click "Register"
Then the system should show an error message
And prevent account creation
```

#### Scenario: Registration fails due to duplicate email
```gherkin
Given the customer is on the registration page
And the entered email is already registered
When they attempt to register with the same email
Then the system should display an error message indicating the email is already in use
```

#### Scenario: Successful login
```gherkin
Given the customer has an existing account
When they enter a valid email and password
And click "Login"
Then the system should authenticate the customer
And redirect them to their dashboard
```

#### Scenario: Login fails due to incorrect credentials
```gherkin
Given the customer is on the login page
When they enter an invalid email or password
And click "Login"
Then the system should display an error message indicating invalid credentials
```

#### Scenario: Password recovery via "Forgot Password"
```gherkin
Given the customer is on the login page
And they click the "Forgot Password" link
When they input their registered email
Then the system should send a password reset email to their inbox
```

---

### Feature: Grocery Browsing and Cart Management

#### Scenario: Display groceries by category
```gherkin
Given the customer is on the grocery catalog page
When they select a category such as "Fruits"
Then the system should display only items from the "Fruits" category
```

#### Scenario: View detailed grocery item
```gherkin
Given the customer is browsing the catalog
When they click on a grocery item
Then the system should display the item name, price, description, image, and stock availability
```

#### Scenario: Add item to cart
```gherkin
Given the customer is viewing a grocery item
When they click "Add to Cart"
Then the system should add the item to their cart
And display the updated total
```

#### Scenario: Update item quantity in cart
```gherkin
Given the customer has items in their cart
When they update the quantity of an item
And click "Update Cart"
Then the system should adjust the cart item's quantity and the total price
```

#### Scenario: Remove item from the cart
```gherkin
Given the customer has items in their cart
When they click "Remove" next to an item
Then the system should remove the item
And update the cart total
```

---

### Feature: Same-Day Delivery Scheduling

#### Scenario: Display delivery slots
```gherkin
Given the customer is at the checkout page
And they select "Same-Day Delivery"
When the selected time is before the daily cutoff time
Then the system should display available delivery slots for that day
```

#### Scenario: Same-day delivery unavailable after cutoff
```gherkin
Given the customer is at the checkout page
And the current time is after the daily cutoff time (e.g., 2:00 PM)
When they attempt to select "Same-Day Delivery"
Then the system should display a message explaining the unavailability of same-day delivery
```

---

### Feature: Promo Code Application

#### Scenario: Apply valid promo code
```gherkin
Given the customer is at the checkout page
And they enter a valid promo code
When they click "Apply"
Then the system should apply the discount
And display the updated order total
```

#### Scenario: Promo code is invalid
```gherkin
Given the customer is at the checkout page
And they enter an expired or invalid promo code
When they click "Apply"
Then the system should display an error message indicating why the promo code is invalid
```

#### Scenario: Promo code fails due to minimum order value
```gherkin
Given the customer is at the checkout page
And the order total is below the minimum order value required for the promo code
When they attempt to apply the code
Then the system should display a message explaining the code cannot be applied
```

---

### Feature: Secure Payment

#### Scenario: Successful payment via credit card
```gherkin
Given the customer is on the payment page
When they enter valid credit card details
And confirm the payment
Then the system should process the transaction successfully
And display a payment confirmation message
```

#### Scenario: Payment fails due to invalid card details
```gherkin
Given the customer is on the payment page
When they enter invalid or expired credit card details
And confirm the payment
Then the system should display an error message indicating the failure
```

#### Scenario: Successful payment via wallet
```gherkin
Given the customer has sufficient wallet balance
When they select "Pay via Wallet" and confirm the payment
Then the system should process the transaction successfully
And display a payment confirmation message
```

---

### Feature: Order Tracking

#### Scenario: View current order status
```gherkin
Given the customer has placed an order
When they navigate to their "Order History"
Then the system should display the status of the order (e.g., "Preparing," "Out for Delivery")
```

#### Scenario: Real-time delivery tracking
```gherkin
Given the customer's order status is "Out for Delivery"
When they open the tracking section in the "Order History"
Then the system should display the current location of the delivery driver on a map
```

#### Scenario: Order marked as delivered
```gherkin
Given the customer's order status is "Out for Delivery"
And the delivery driver confirms the delivery
When the driver updates their status
Then the system should mark the order as “Delivered”
And notify the customer via push notification
```

---

### Feature: Security

#### Scenario: Encrypt customer data during registration
```gherkin
Given the customer has entered their registration details
When the system stores the data in the database
Then the data should be encrypted at rest using AES encryption
```

---

These test cases are designed to validate the functionality, edge cases, and security requirements of the Online Grocery Ordering System comprehensively.

**Test cases complete**

