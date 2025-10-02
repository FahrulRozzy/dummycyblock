# routes/dummy_routes.py
from flask import Blueprint, jsonify, request
from controllers.dummy_controllers import DummyController
import os

dummy_bp = Blueprint("dummy_bp", __name__)

# Mapping cyid ke nama depo
CYID_MAPPING = {
    "1": "DEPO4",
    "216": "YON"
}

# GET /get-dummy?cy=YON&user=fahrul
@dummy_bp.route("/get-dummy", methods=["GET"])
def get_dummy():
    cyid = request.args.get("cyid")
    block = request.args.get("block")
    user = request.args.get("user")
    
    if not cyid:
        return jsonify({"error": "cyid parameter is required"}), 400

    # validasi cyid
    if cyid not in CYID_MAPPING:
        return jsonify({"error": f"Invalid cyid '{cyid}'"}), 400
    
    cy = CYID_MAPPING[cyid]

    if not cy:
        return jsonify({"error": "cy parameter is required"}), 400
    
    # validasi block hanya ALL
    if block and block.upper() != "ALL":
        return jsonify({"error": "Only block=ALL is allowed"}), 400
    
    # buat path file sesuai parameter cy
    base_dir = os.path.dirname(os.path.dirname(__file__))  # folder APIDUMMYCYBLOCK
    file_path = os.path.join(base_dir, f"{cy}.csv")

    controller = DummyController(file_path)
    result = controller.get()
    
    return jsonify({
        "status": "succes",
        "user": user,
        "cy": cy,
        "data": result
    })

# POST /update-dummy
@dummy_bp.route("/update-dummy", methods=["POST"])
def update_dummy():
    cyid = request.json.get("cyid")
    nc = request.json.get("nc")  # nomor container
    blockbaru = request.json.get("blockbaru")  # format "BLOCK.COLUMN.ROW.TIER"

    if not cyid or not nc or not blockbaru:
        return jsonify({"error": "cyid, nc, and blockbaru are required"}), 400

    # validasi cyid
    if cyid not in CYID_MAPPING:
        return jsonify({"error": f"Invalid cyid '{cyid}'"}), 400
    
    cy = CYID_MAPPING[cyid]

    # buat path file sesuai parameter cy
    base_dir = os.path.dirname(os.path.dirname(__file__))  # folder APIDUMMYCYBLOCK
    file_path = os.path.join(base_dir, f"{cy}.csv")

    controller = DummyController(file_path)
    result = controller.update_dummmy(nc, blockbaru)

    return jsonify({
        "status": "success",
        "cyid": cyid,
        "cy": cy,
        "nc": nc,
        "blockbaru": blockbaru,
        "data": result
    })