
# Digi4u Repair UK - TikTok Affiliate Invitation Bot

An automated bot for inviting TikTok creators to promote Digi4u Repair UK services through collaborations.

## Features

- Automated TikTok creator search and filtering
- Customizable filters for:
  - Follower count
  - Category
  - Promotion type (Video/Live)
- GMV-based targeting (highest to lowest)
- Automatic invitation link generation
- Detailed logging and tracking of invited affiliates

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rehmanul/Digi4u-Repair-Bot.git
cd Digi4u-Repair-Bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python -m src.main
```

### With Custom Parameters
```bash
python -m src.main --invite-count 50 --min-followers 20000 --min-gmv 10000
```

### Command Line Arguments

- `--invite-count`: Number of invitation links to generate
- `--min-followers`: Minimum number of followers required
- `--min-gmv`: Minimum GMV threshold for creators

## Configuration

Edit `src/config.py` to customize:
- TikTok search filters
- Business information
- GMV thresholds
- Logging settings

## Logging

Logs are stored in `affiliate_bot.log`. Invited affiliates are tracked in `invited_affiliates.csv`.

## Business Information

- Website: https://www.digi4u.co.uk/
- Services: Mobile and electronics repair
- Location: UK

## Safety Features

- Automatic stop when GMV threshold is reached
- Tracking of invited creators to prevent duplicates
- Error handling and logging
- Rate limiting to comply with TikTok's policies

## Note

This bot is designed for use with TikTok's platform. Please ensure compliance with TikTok's terms of service and API usage policies.
