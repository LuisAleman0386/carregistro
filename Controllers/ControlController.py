from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from Routes.routes import control

@control.route('/' )
def ver_pant_principal():
    


    return render_template('control_vehicular.html')