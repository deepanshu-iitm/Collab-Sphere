from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app import db
from app.models import User
import re

bp = Blueprint('auth_routes', __name__, url_prefix='/auth')

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if role not in ['admin', 'sponsor', 'influencer']:
        return jsonify({'msg': 'Invalid role'}), 400

    if not all([username, email, password, role]):
        return jsonify({'msg': 'Missing required fields'}), 400
    
    if not validate_email(email):
        return jsonify({'msg': 'Invalid email format'}), 400
    
    if len(password) < 8:
        return jsonify({'msg': 'Password must be at least 8 characters long'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'msg': 'Username already exists'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'msg': 'Email already exists'}), 400

    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password_hash=hashed_password, role=role)

    if role == 'sponsor':
        user.company_name = data.get('company_name')
        user.industry = data.get('industry')
        user.budget = data.get('budget')
    elif role == 'influencer':
        user.name = data.get('name')
        user.category = data.get('category')
        user.niche = data.get('niche')
        user.reach = data.get('reach')
    
    db.session.add(user)
    db.session.commit()

    return jsonify({'msg': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({'msg': 'Missing required fields'}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'msg': 'Invalid credentials'}), 401

        access_token = create_access_token(identity={'id': user.id, 'role': user.role})
        return jsonify({'access_token': access_token, 'role': user.role}), 200
    except Exception as e:
        return jsonify({'msg': str(e)}), 500
