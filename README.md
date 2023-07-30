# Library Management System

This is a project to develop an online management system for book borrowings in a library.
The system aims to optimize the work of library administrators and provide a user-friendly experience for customers.
It will automate the tracking of books, borrowings, users, and
payments, eliminating the need for manual paper-based processes.

## Project Description

The library management system will address the following issues in the current manual system:

- Lack of book inventory tracking
- Inability to check availability of specific books
- Cash-only payments without credit card support
- Manual tracking of book returns and late returns

To overcome these problems, we will develop an online system that allows users to borrow
books, make payments, and receive notifications.
The system will enable administrators to manage books, track borrowings, and
receive updates about new borrowings, overdue books, and successful payments.

## Features

* JWT authenticated.
* Admin panel /admin/
* Documentation at /api/doc/swagger/
* Books inventory management.
* Books borrowing management.
* Notifications service through Telegram API (bot and chat).
* Scheduled notifications with Django Q and Redis.
* Payments handle with Stripe API.

## Getting access

* create user via /api/users/
* get access token via /api/users/token/

## Getting access

* create user via /api/users/
* get access token via /api/users/token/

## How to run with Docker

Docker should be installed.

Create `.env` file with your variables (look at `.env.sample`
file, don't change `POSTGRES_DB` and `POSTGRES_HOST`).

```shell
docker-compose build
docker-compose up
```
