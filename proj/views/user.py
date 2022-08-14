from flask import Blueprint, render_template, request, make_response,jsonify
import sys, os, json
from proj.models.model import *

bp_user = Blueprint('bp_user', __name__)


@bp_user.route('/list', methods=['GET'])
def list():
    data = []

    try:
        use = User(name="Zamani Rahman",age="24",date_birth=None,gender="Male")
        db.session.add(use)
        db.session.commit()

        item = dict()
        item['name'] = "Zamani Rahman"
        item['age'] = "24"
        item['birth'] = None
        item['gender'] = "Male"

        data.append(item)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        msg = exc_obj, fname, "Line number : ", exc_tb.tb_lineno
        print(msg)
    return jsonify(data)