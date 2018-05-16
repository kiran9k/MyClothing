import config
import datetime
import json
from functools import wraps
import sys

import pymongo.errors as mongoErrs

from flask import Flask, send_from_directory, request, redirect, url_for, json, jsonify, render_template, Response, session, flash


app = Flask(__name__,static_url_path='')


#Routing Function 


# Index Page Routing function
@app.route('/')
@app.route('/home')
def main():
    """! \brief  Routing function for Index Page
        Routing function for handling Main Index Page"""
    """Description : Sends the index.html file from static folders

    Route: /
    """
    return render_template('main/index.html')



@app.errorhandler(500)
def server_error(e):
    """! \brief  Routing function for handling Errors 
    """
    """Description : 
        1. Routing function for handling Errors
        2. Renders 500 internal Error page

    """
    # Log the error and stacktrace.
    return 'An internal error occurred.', 500

if(__name__ =='__main__'):
    """! \brief  Main Entry Point
    """
    """Description : 
        1. Runs a Flask App

    """
    app.run(host=config.HOST, port=config.PORT_NO, debug= config.DEBUG)