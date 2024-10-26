from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.decorators import role_required
from app.models import User, Campaign, AdRequest, Flag, db

bp = Blueprint('admin_routes', __name__, url_prefix='/admin')

@bp.route('/dashboard', methods=['GET'])
@jwt_required()
@role_required('admin')
def dashboard():
    users_count = User.query.count()
    campaigns_count = Campaign.query.count()
    ad_requests_count = AdRequest.query.count()

    active_sponsors = User.query.filter_by(role='sponsor', approved=True).count()
    pending_sponsors = User.query.filter_by(role='sponsor', approved=False).count()

    return jsonify({
        'users_count': users_count,
        'campaigns_count': campaigns_count,
        'ad_requests_count': ad_requests_count,
        'active_sponsors': active_sponsors,
        'pending_sponsors': pending_sponsors
    }), 200

@bp.route('/approve_sponsor', methods=['POST'])
@jwt_required()
@role_required('admin')
def approve_sponsor():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'msg': 'User ID required'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'msg': 'User not found'}), 404
    if user.role != 'sponsor':
        return jsonify({'msg': 'User is not a sponsor'}), 400

    if user.approved: 
        return jsonify({'msg': 'Sponsor already approved'}), 400

   
    user.approved = True 
    db.session.commit()

    return jsonify({'msg': 'Sponsor approved'}), 200

@bp.route('/pending_sponsors', methods=['GET'])
@jwt_required()
@role_required('admin')
def get_pending_sponsors():
    pending_sponsors = User.query.filter_by(role='sponsor', approved=False).all()
    if not pending_sponsors:
        return jsonify([]), 200
    
    return jsonify([{
        'id': sponsor.id,
        'username': sponsor.username,
        'email': sponsor.email,
        'company_name': sponsor.company_name,
        'industry': sponsor.industry,
        'budget': sponsor.budget
    } for sponsor in pending_sponsors]), 200


@bp.route('/users', methods=['GET'])
@jwt_required()
@role_required('admin')
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role,
        'created_at': user.created_at
    } for user in users])

@bp.route('/campaigns', methods=['GET'])
@jwt_required()
@role_required('admin')
def get_campaigns():
    campaigns = Campaign.query.all()
    return jsonify([{
        'id': campaign.id,
        'name': campaign.name,
        'description': campaign.description,
        'start_date': campaign.start_date,
        'end_date': campaign.end_date,
        'budget': campaign.budget,
        'visibility': campaign.visibility,
        'goals': campaign.goals,
        'sponsor_id': campaign.sponsor_id
    } for campaign in campaigns])

@bp.route('/ad_requests', methods=['GET'])
@jwt_required()
@role_required('admin')
def get_ad_requests():
    ad_requests = AdRequest.query.all()
    return jsonify([{
        'id': ad_request.id,
        'campaign_id': ad_request.campaign_id,
        'influencer_id': ad_request.influencer_id,
        'messages': ad_request.messages,
        'requirements': ad_request.requirements,
        'payment_amount': ad_request.payment_amount,
        'status': ad_request.status
    } for ad_request in ad_requests])

@bp.route('/flag_user', methods=['POST'])
@jwt_required()
@role_required('admin')
def flag_user():
    data = request.get_json()
    user_id = data.get('user_id')
    reason = data.get('reason')

    if not user_id or not reason:
        return jsonify({'msg': 'User ID and reason required'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'msg': 'User not found'}), 404

    flag = Flag(flagged_id=user_id, flagged_type='user', reason=reason)
    db.session.add(flag)
    db.session.commit()

    return jsonify({'msg': 'User flagged successfully'}), 200

@bp.route('/flag_campaign', methods=['POST'])
@jwt_required()
@role_required('admin')
def flag_campaign():
    data = request.get_json()
    campaign_id = data.get('campaign_id')
    reason = data.get('reason')

    if not campaign_id or not reason:
        return jsonify({'msg': 'Campaign ID and reason required'}), 400

    campaign = Campaign.query.get(campaign_id)
    if not campaign:
        return jsonify({'msg': 'Campaign not found'}), 404

    flag = Flag(flagged_id=campaign_id, flagged_type='campaign', reason=reason)
    db.session.add(flag)
    db.session.commit()

    return jsonify({'msg': 'Campaign flagged successfully'}), 200

@bp.route('/flags', methods=['GET'])
@jwt_required()
@role_required('admin')
def get_flags():
    flags = Flag.query.all()
    return jsonify([{
        'id': flag.id,
        'flagged_id': flag.flagged_id,
        'flagged_type': flag.flagged_type,
        'reason': flag.reason,
        'timestamp': flag.timestamp
    } for flag in flags]), 200
