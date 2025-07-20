from flask import Flask, jsonify
import logging
import os

# Initialize Flask App
app = Flask(__name__)

# Setup Logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# App Configurations
app.config['ENVIRONMENT'] = os.getenv('ENV', 'production')

# Root Endpoint
@app.route('/')
def index():
    app.logger.info("Root endpoint accessed.")
    return jsonify({
        'status': 'success',
        'message': 'Welcome to the Flask Web Application!',
        'environment': app.config['ENVIRONMENT']
    }), 200

# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health():
    app.logger.info("Health check endpoint accessed.")
    return jsonify({'status': 'healthy'}), 200

# Info Endpoint
@app.route('/info', methods=['GET'])
def info():
    app.logger.info("Info endpoint accessed.")
    return jsonify({
        'app': 'Flask Web App',
        'version': '1.0.0',
        'maintainer': 'Your Name',
    }), 200

# Error Handler Example
@app.errorhandler(404)
def not_found(error):
    app.logger.warning("404 error occurred.")
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"500 error: {str(error)}")
    return jsonify({'error': 'Internal Server Error'}), 500

# Start the Server
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.logger.info(f"Starting server in {app.config['ENVIRONMENT']} mode on port {port}")
    app.run(host='0.0.0.0', port=port)
