# Django E-Commerce Project 

## Project Description
This Django project is an e-commerce platform designed to facilitate online shopping for users. It includes features such as a product catalog, shopping cart system, order placement, email confirmation for orders, integration with a payment gateway, payment notifications management, export of orders to CSV files, creation of custom views for the administration site, and dynamic generation of PDF invoices.

## Features
- **Product Catalog Management**: 
  - Models for managing products are created to represent the product catalog.
  - Products are added to the administration site for easy management.

- **Shopping Cart System**:
  - Utilizes Django sessions to allow users to keep selected products while browsing the site.
  - Users can add, remove, and adjust quantities of products in their shopping cart.

- **Order Placement**:
  - Includes functionality to create orders, capturing user details and selected products from the shopping cart.
  - Users can review their order summary before finalizing the purchase.
  - Integration with a payment gateway allows users to securely complete transactions.

- **Email Confirmation**:
  - Implements asynchronous email confirmation for users when they successfully place an order.
  - Sends confirmation emails containing order details to users' email addresses.

- **Payment Gateway Integration**:
  - Integrates with a payment gateway to securely process online payments.
  - Manages payment notifications to track successful transactions and handle payment failures.

- **Order Management**:
  - Allows administrators to export orders to CSV files for further analysis and processing.
  - Custom views are created for the administration site to provide enhanced functionality and insights into order management.

- **PDF Invoice Generation**:
  - Dynamically generates PDF invoices for orders, providing users with detailed transaction summaries.

## Setup and Installation
1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Configure database settings in `settings.py`.
4. Run migrations to create the necessary database tables: `python manage.py migrate`.
5. Create a superuser to access the admin site: `python manage.py createsuperuser`.
6. Start the development server: `python manage.py runserver`.
7. Access the admin site at `http://127.0.0.1:8000/admin/` and add products to the catalog.
8. Navigate to the main site to browse the catalog, add products to the shopping cart, and place orders.

## Usage
- Browse through the product catalog by visiting the main site.
- Click on products to view detailed information.
- Add products to the shopping cart by clicking the "Add to Cart" button.
- Navigate to the shopping cart to review selected products and adjust quantities.
- Proceed to checkout to place an order, providing necessary shipping information and completing payment.
- Receive email confirmation upon successful order placement.
- Administrators can manage orders, export them to CSV files, and access custom views in the administration site.

## Contributors
- snipher marube - https://twitter.com/snipherdev | sniphermarube@gmail.com

