# routes/dummy_routes.py
from flask import Blueprint, jsonify, request
from controllers.dummy_controllers import DummyController
import os

dummy_bp = Blueprint("dummy_bp", __name__)

# GET /get-dummy?cy=YON&user=fahrul
@dummy_bp.route("/get-dummy", methods=["GET"])
def get_dummy():
    cy = request.args.get("cy")
    user = request.args.get("user")

    if not cy:
        return jsonify({"error": "cy parameter is required"}), 400
    
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
    cy = request.json.get("cy")
    nc = request.json.get("nc")  # nomor container
    blockbaru = request.json.get("blockbaru")  # format "BLOCK.COLUMN.ROW.TIER"

    if not cy or not nc or not blockbaru:
        return jsonify({"error": "cy, nc, and blockbaru are required"}), 400

    # buat path file sesuai parameter cy
    base_dir = os.path.dirname(os.path.dirname(__file__))  # folder APIDUMMYCYBLOCK
    file_path = os.path.join(base_dir, f"{cy}.csv")

    controller = DummyController(file_path)
    result = controller.update_dummmy(nc, blockbaru)

    return jsonify({
        "status": "succes",
        "cy": cy,
        "nc": nc,
        "blockbaru": blockbaru,
        "data": result
    })
