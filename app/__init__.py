import os

from flask import Flask, render_template, redirect, request
from app.functions import checkNIM, getKelasProposal

def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only

    # ======== Routing ============================= #
    # -------- Home -------------------------------- #
    
    @app.route('/', methods=['GET'])
    def index():
        return render_template('layouts/index.html')

    @app.route('/how', methods=['GET'])
    def how():
        return render_template('layouts/how.html')

    @app.route('/why', methods=['GET'])
    def why():
        return render_template('layouts/why.html')    
    
    @app.route('/form-proposal',methods=['GET'])
    def fp():
        res = getKelasProposal()
        return render_template('layouts/form-proposal.html',res=res)

    @app.route('/check',methods=['POST'])
    def redirectCheck():
        return redirect("/check/"+str(request.form['nim']))
    
    @app.route('/check/<int:nim>',methods=['GET'])
    def check(nim):
        res = checkNIM(nim=nim)
        print(nim)
        return render_template('layouts/check.html',res=res)

    return app