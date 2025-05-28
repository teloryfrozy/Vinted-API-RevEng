# Vinted Management Tool

A local tool to help manage Vinted seller activities more efficiently.

## Features

### Core Features

- Automated shipping label management
- Custom thank-you message integration
- Automated buyer communications
- Conversation management
- Feedback automation
- Item database for quick re-listing
- Automated label printing (requires Adobe Reader)
- Sales analytics and accounting exports

### Email Management

- Automated email sorting and cleanup
- Smart notification handling

## Setup

```bash
# Install dependencies
npm install

# Development server
npm run dev

# Production build
npm run build
npm run preview # Preview at http://localhost:4173/
```

## Important Notes

- Use a dedicated Vinted email address
- Access token needs periodic renewal (stored in cookies)
- For local use only - no authentication system implemented
- Currently being refactored using Svelte + FastAPI + SQLite

## Legal Notice

This tool is for personal use only and must comply with Vinted's terms of service. Any automated data collection must respect platform policies and user privacy.



# start the back

 fastapi dev main.py 