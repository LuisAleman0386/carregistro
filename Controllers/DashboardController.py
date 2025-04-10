from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from Routes.routes import dashboard

@dashboard.route('/' )
def ver_pant_principal():
    


    return render_template('dashboard.html')