# SupportHub – IT Service Management Portal

## 1. Project Overview

SupportHub is a web-based IT Service Management Portal developed using the Django web framework and deployed on an Amazon Web Services (AWS) EC2 instance.

The purpose of SupportHub is to provide employees with a centralized platform for submitting and managing IT support requests. Instead of handling support requests manually, users can create tickets and track their status through a web-based dashboard.

The application includes user authentication, protected pages, ticket management, CRUD operations, dashboard statistics, and AWS deployment.

The final project demonstrates the complete development process from application creation and database integration to deployment, security testing, and source-code management using Git and GitHub.

---

## 2. Project Goals

The main goals of the SupportHub project are:

- Build a functional IT Service Management web application.
- Provide a simple interface for employees to submit IT support requests.
- Allow authenticated users to manage their own support tickets.
- Implement secure user authentication.
- Protect pages that should only be accessible to logged-in users.
- Provide a dashboard showing ticket statistics.
- Implement Create, Read, Update, and Delete (CRUD) functionality.
- Deploy the application on an AWS EC2 instance.
- Use Git and GitHub for source-code version control.
- Test the application after deployment to verify that the major features work correctly.

---

## 3. Main Application Features

### 3.1 User Registration

New users can create an account through the registration page.

The registration process allows users to provide their account information and create credentials that can later be used to log into SupportHub.

---

### 3.2 User Login

Registered users can log into SupportHub using their email address and password.

After successful authentication, the user can access protected application features such as the employee dashboard and ticket list.

A successful login displays a confirmation message and redirects the user to the appropriate page.

---

### 3.3 User Logout

Users can log out using the Logout option in the navigation bar.

After logout, the application displays a confirmation message:

"You have been logged out successfully."

The user's authenticated session is ended.

---

## 4. Authentication and Security

Authentication is an important part of the SupportHub application.

Protected pages use Django's authentication system to ensure that only authenticated users can access them.

For example, the dashboard view uses Django's `login_required` decorator.

If a user is not logged in and attempts to directly access a protected page, the application redirects the user to the login page.

### Security Test

The authentication/security functionality was tested using the following process:

1. Log into SupportHub.
2. Access the employee dashboard.
3. Access the ticket list.
4. Click Logout.
5. Manually enter the protected ticket-list URL.
6. Confirm that the user cannot access the ticket list while logged out.
7. Confirm that the application redirects the user to the login page.

The test successfully confirmed that protected pages require authentication.

---

## 5. Employee Dashboard

After logging in, users can access the Employee Dashboard.

The dashboard provides an overview of the current support-ticket information.

It displays:

- Open Tickets
- In Progress Tickets
- Closed Tickets
- Recent Activity

The ticket counts are calculated from the ticket data stored in the database.

The dashboard also provides buttons for:

- Creating a new ticket
- Viewing submitted tickets

This gives users a central location from which they can manage their support requests.

---

## 6. Ticket Management

SupportHub provides complete CRUD functionality for support tickets.

### Create

Users can create a new support ticket by entering information such as:

- Title
- Category
- Priority
- Description
- Status

### Read

Users can view their submitted tickets in the "My Support Tickets" section.

The ticket list displays:

- Ticket ID
- Title
- Category
- Priority
- Status
- Date
- Available actions

### Update

Users can select the Edit option to modify an existing ticket.

The updated information is saved to the database and displayed when the ticket list is refreshed.

### Delete

Users can delete an existing ticket using the Delete option.

The ticket is removed from the application's ticket list.

---

## 7. Ticket Categories

SupportHub provides predefined categories for IT support requests.

The available categories are:

- Hardware
- Software
- Network
- Other

These categories help organize support requests according to the type of IT problem.

---

## 8. Ticket Priority

Each ticket can have a priority level.

Available priority levels are:

- Low
- Medium
- High

This allows support requests to be categorized according to their importance.

---

## 9. Ticket Status

Each ticket has a status that indicates its current progress.

Available statuses are:

- Open
- In Progress
- Closed

The status is also reflected on the dashboard through the ticket statistics.

---

## 10. Ticket Database Model

The SupportHub application uses a Django model to represent support tickets.

The Ticket model contains fields for:

- Title
- Category
- Priority
- Description
- Status
- Created Date

The application uses Django's ORM to interact with the database.

This allows the application to create, retrieve, update, and delete ticket records without manually writing SQL queries for each operation.

---

## 11. Technology Stack

### Programming Language

- Python

### Web Framework

- Django

### Frontend

- HTML
- CSS
- Bootstrap

### Database

- SQLite

### Cloud Platform

- Amazon Web Services (AWS)

### Cloud Service

- Amazon EC2

### Version Control

- Git
- GitHub

---

## 12. AWS EC2 Deployment

The SupportHub application was deployed on an AWS EC2 instance.

The EC2 instance provides the computing environment where the Django application runs.

The deployment process included:

1. Launching an EC2 instance.
2. Connecting to the EC2 instance using SSH.
3. Uploading and configuring the SupportHub project.
4. Creating and activating a Python virtual environment.
5. Installing the required Python packages.
6. Configuring Django settings.
7. Running database-related commands.
8. Configuring the application to run as a system service.
9. Starting the SupportHub service.
10. Testing the application through the EC2 public IPv4 address.

The deployed application was successfully accessed through a web browser.

---

## 13. Python Virtual Environment

A Python virtual environment was used to isolate the project's Python dependencies from the system environment.

The virtual environment can be activated using:

```bash
source venv/bin/activate
