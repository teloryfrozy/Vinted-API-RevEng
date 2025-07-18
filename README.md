# Vinted Management Tool

A local tool to help you manage your Vinted account super fast !
Interface in French only for now.

## Getting Started

### Prerequisites for Non-Developers

Before starting, you'll need to install:

- [Node.js](https://nodejs.org/en/download)
- [Python](https://www.python.org/)

### First Time Setup

```bash
cd frontend
npm install

cd ../backend
pip install -r requirements.txt
```

### Running the Application

```bash
# Start Frontend (Development)
cd frontend
npm run dev
# OR for Production
npm run build
npm run preview # Access at http://localhost:4173/

# Start Backend (in another terminal)
cd backend
fastapi dev main.py
```

> **Note**: A Docker version might be released in the future to simplify setup for non-developers.

## Features Status

| Feature                | Description                                              | Status               |
| ---------------------- | -------------------------------------------------------- | -------------------- |
| English translation    | Add a language switcher button + i18n translations       | ⚠️ Not Planned       |
| Conversation Cleanup   | Auto-delete conversations after x months of inactivity   | ✅ Done              |
| Ad Refresh             | Automatic refreshing of listings                         | ⚒️ Under Refactoring |
| Sales Analytics        | Export transactions, generate graphs & statistics        | ✅ Done              |
| Favorite Messages      | Quick-copy system for 5 favorite messages                | ✅ Done              |
| Publication Menu       | Database-linked posting system with search functionality | 📝 To Be Done        |
| Shipping Labels        | Automatic retrieval of shipping labels                   | ⚠️ Not Planned       |
| Thank You Messages     | Add customizable thank-you messages on shipping labels   | ⚠️ Not Planned       |
| Feedback System        | Random automated feedback for transactions               | ⚠️ Not Planned       |
| Like Notifications     | Auto-send notifications to users who liked an item       | ⚠️ Not Planned       |
| Auto Purchase Response | Automatic message when a buyer purchases an item         | ⚠️ Not Planned       |
| Item Database          | Auto re upload for items with multiple copies            | ⚠️ Not Planned       |

## Legal Notice

This tool is for personal use only and must comply with Vinted's terms of service. Any automated data collection must respect platform policies and user privacy.
