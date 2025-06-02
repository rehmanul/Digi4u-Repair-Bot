
# Digi4u TikTok Affiliate Bot

An automated bot for inviting TikTok creators to join Digi4u Repair UK's affiliate program. The bot searches for relevant creators based on followers, category, and estimated GMV (Gross Merchandise Value).

## Features

- **Targeted Creator Search**: Filter creators by:
  - Follower count
  - Content category
  - Promotion type (Video/Live)
  - Estimated GMV

- **Smart Filtering**:
  - Sorts creators by estimated GMV
  - Stops at preset minimum GMV threshold
  - Tracks invited creators to avoid duplicates

- **Automatic Invitation Links**:
  - Generates collaboration invite links
  - Tracks all generated links
  - Real-time link status monitoring

## Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run locally:
```bash
python app.py
```

## Deployment on Render.com

1. Fork or clone this repository

2. Create a new Web Service on Render.com:
   - Connect your GitHub repository
   - Select "Docker" as the environment
   - The following settings will be automatically configured from `render.yaml`:
     - Build command: `docker build -t digi4u-affiliate-bot .`
     - Start command: `docker run -p $PORT:5000 digi4u-affiliate-bot`

3. Environment Variables (automatically set from render.yaml):
   - `CHROME_PROFILE_PATH`: `/chrome-profile`
   - `PORT`: `5000`

4. Deploy:
   - Render will automatically build and deploy your application
   - The deployment process includes:
     - Setting up a containerized environment
     - Installing Chrome and dependencies
     - Configuring the virtual display
     - Starting the web application

5. Access your deployed bot:
   - Render will provide a URL like `https://your-app-name.onrender.com`
   - Open this URL in your browser to access the bot interface

## Important Notes for Deployment

1. **Chrome Profile**:
   - The deployed version uses a fresh Chrome profile
   - You'll need to log in to TikTok when starting the bot
   - The profile is persistent within the container

2. **Security**:
   - The bot runs in a secure, containerized environment
   - All traffic is encrypted via HTTPS
   - Credentials are stored securely in the container

3. **Monitoring**:
   - Use Render's dashboard to monitor:
     - Application logs
     - Resource usage
     - Error reports

4. **Scaling**:
   - The application can be scaled through Render's dashboard
   - Multiple instances can be run for parallel campaigns

## Usage

1. Access the web interface
2. Configure campaign settings:
   - Set minimum followers
   - Set minimum GMV
   - Choose category
   - Select promotion type
3. Start the campaign
4. Monitor progress and generated links in real-time

## Support

For issues and support:
1. Check the application logs in Render dashboard
2. Submit issues on GitHub
3. Contact the development team

## Legal Compliance

Ensure compliance with:
- TikTok's Terms of Service
- Local regulations
- Data protection laws
