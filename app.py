
from flask import Flask, render_template, jsonify, request
from tiktok_bot import TikTokAffiliateBot
import threading
import json
import os

app = Flask(__name__)
bot = None
campaign_thread = None

# Get port from environment variable (Render.com sets this)
port = int(os.environ.get('PORT', 5000))

# Get Chrome profile path from environment variable
default_chrome_profile = os.environ.get('CHROME_PROFILE_PATH', '/chrome-profile')

@app.route('/')
def index():
    return render_template('index.html', 
                         default_profile=default_chrome_profile)

@app.route('/api/start', methods=['POST'])
def start_campaign():
    global bot, campaign_thread
    
    config = request.json
    chrome_profile = config.get('chrome_profile', default_chrome_profile)
    
    if bot and bot.status['running']:
        return jsonify({
            'success': False,
            'error': 'Campaign already running'
        })
    
    bot = TikTokAffiliateBot(chrome_profile)
    campaign_thread = threading.Thread(
        target=bot.run_campaign,
        args=(config,)
    )
    campaign_thread.start()
    
    return jsonify({'success': True})

@app.route('/api/stop')
def stop_campaign():
    if bot:
        bot.stop_campaign()
        return jsonify({'success': True})
    return jsonify({
        'success': False,
        'error': 'No campaign running'
    })

@app.route('/api/status')
def get_status():
    if bot:
        return jsonify(bot.get_status())
    return jsonify({
        'running': False,
        'invites_sent': 0,
        'creators_found': 0,
        'current_creator': '',
        'last_error': None,
        'invite_links': []
    })

if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible externally
    app.run(host='0.0.0.0', port=port)
