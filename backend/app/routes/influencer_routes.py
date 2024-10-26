from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.decorators import role_required
from app.models import AdRequest, Campaign, db


bp = Blueprint('influencer_routes', __name__, url_prefix='/influencer')

@bp.route('/ad_requests', methods=['GET'])
@jwt_required()
@role_required('influencer')
def get_ad_requests():
    influencer_id = get_jwt_identity()['id']
    ad_requests = AdRequest.query.filter_by(influencer_id=influencer_id).all()
    return jsonify([{
        'id': ad_request.id,
        'campaign_id': ad_request.campaign_id,
        'messages': ad_request.messages,
        'requirements': ad_request.requirements,
        'payment_amount': ad_request.payment_amount,
        'status': ad_request.status
    } for ad_request in ad_requests]), 200

@bp.route('/ad_requests/<int:ad_request_id>/accept', methods=['POST'])
@jwt_required()
@role_required('influencer')
def accept_ad_request(ad_request_id):
    influencer_id = get_jwt_identity()['id']
    ad_request = AdRequest.query.get(ad_request_id)
    if not ad_request:
        return jsonify({'msg': 'Ad request not found'}), 404
    if ad_request.status != 'pending':
        return jsonify({'msg': 'Ad request cannot be accepted'}), 400
    if ad_request.influencer_id != influencer_id:
        return jsonify({'msg': 'Unauthorized access'}), 403
    
    ad_request.status = 'accepted'
    db.session.commit()
    return jsonify({'msg': 'Ad request accepted'}), 200

@bp.route('/ad_requests/<int:ad_request_id>/reject', methods=['POST'])
@jwt_required()
@role_required('influencer')
def reject_ad_request(ad_request_id):
    influencer_id = get_jwt_identity()['id']
    ad_request = AdRequest.query.get(ad_request_id)
    if not ad_request:
        return jsonify({'msg': 'Ad request not found'}), 404
    if ad_request.status != 'pending':
        return jsonify({'msg': 'Ad request cannot be rejected'}), 400
    if ad_request.influencer_id != influencer_id:
        return jsonify({'msg': 'Unauthorized access'}), 403
    ad_request.status = 'rejected'
    db.session.commit()
    return jsonify({'msg': 'Ad request rejected'}), 200

@bp.route('/ad_requests/<int:ad_request_id>/negotiate', methods=['POST'])
@jwt_required()
@role_required('influencer')
def negotiate_ad_request(ad_request_id):
    ad_request = AdRequest.query.get(ad_request_id)
    if not ad_request:
        return jsonify({'msg': 'Ad request not found'}), 404
    data = request.get_json()
    payment_amount = data.get('payment_amount')

    if payment_amount is None:
        return jsonify({'msg': 'Payment amount required'}), 400

    ad_request.payment_amount = payment_amount
    ad_request.status = 'pending'
    db.session.commit()
    return jsonify({'msg': 'Ad request negotiated'}), 200

@bp.route('/search/campaigns', methods=['GET'])
@jwt_required()
@role_required('influencer')
def search_campaigns():
    niche = request.args.get('niche')
    visibility = 'public'

    query = Campaign.query.filter_by(visibility=visibility)

    if niche:
        query = query.filter(Campaign.goals.ilike(f'%{niche}%'))

    campaigns = query.all()

    return jsonify([{
        'id': campaign.id,
        'name': campaign.name,
        'description': campaign.description,
        'start_date': campaign.start_date.strftime('%Y-%m-%d') if campaign.start_date else None,
        'end_date': campaign.end_date.strftime('%Y-%m-%d') if campaign.end_date else None,
        'budget': campaign.budget,
        'visibility': campaign.visibility,
        'goals': campaign.goals,
        'sponsor_id': campaign.sponsor_id
    } for campaign in campaigns]), 200

