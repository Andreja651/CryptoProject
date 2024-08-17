import httpx
import requests
from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required, JWTManager
from flask_migrate import Migrate

from Authentication.Controller.athentication_controller import auth_bp
from Services.coinApi_service import COINAPIService
from Transaction.blueprint import transaction_bp
from User.blueprint import user_bp
from Wallet.blueprint import wallet_bp
from config import Config
from db_extension import db

app = Flask(__name__)
#Blueprints
app.register_blueprint(user_bp)
app.register_blueprint(wallet_bp)
app.register_blueprint(transaction_bp)
app.register_blueprint(auth_bp)
coin_api_service = COINAPIService
app.config.from_object(Config)  # Load configuration from Config class in config.py
db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


# Route to fetch cryptocurrency information
@app.route('/crypto-info', methods=['GET'])
@jwt_required()
async def get_crypto_info():
    data = request.get_json()
    try:
        symbol_id = data.get('symbol_id')
        response = []
        async with httpx.AsyncClient() as client:
            response = await COINAPIService.get_crypto_info(client= client, symbol_id=symbol_id)
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': f'Request failed with status code {response.status_code}'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
