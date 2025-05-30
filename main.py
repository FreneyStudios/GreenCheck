#!/usr/bin/env python3
#/*--
#
# Copyright (c) 2025  Frêney Studios
# Copyright (c) 2025  XCMG (XCube Media Group)
#
# Module Name:
#
#	 main.py
#
# Abstract:
#
#	 Main file for GreenCheck (Open-source) 
# 
# - Made in Italy
#
# Author:
#
#	 Marco Panseri (Marx) 16-05-2025
#
# Revision History:
#
#--*/

#
# [SECTIONS]
# [SECTION] - IMPORTS
# [SECTION] - VARIABLES
#
#


# [SECTION] - IMPORTS
try:
  from flask import render_template, Flask, request, jsonify # Import jsonify for JSON responses
  import os, sys
  import spixe as SPIXE # Assuming spixe is installed and available
  import multiprocessing
  from transformers import pipeline
  import cmdproc
  import geck_aim as aim
except Exception as e:
  print("Error importing modules: ", e) # More specific error message

# [SECTION] - VARIABLES
version     = "v.0.0.5"
__version__ = version
assert version != None

# Function to get the base directory of the current app
def get_base_directory():
    # Use sys._MEIPASS for PyInstaller bundled apps
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.abspath(os.path.dirname(__file__))

    return base_dir

# Paths for templates and static files
base_dir = get_base_directory()
template_folder = os.path.join(base_dir, 'templates')
static_folder   = os.path.join(base_dir, 'static'   )

# Initialize Flask app
# Check if template and static folders exist before passing them
if not os.path.exists(template_folder):
    print(f"Warning: Template folder not found at {template_folder}")
    template_folder = None 

if not os.path.exists(static_folder):
    print(f"Warning: Static folder not found at {static_folder}")
    static_folder = None 

app = Flask(__name__,
            template_folder=template_folder,
            static_folder=static_folder)

@app.route("/")
# @SPIXE.BASE.HANDLE()
def home_page():
  aim.geck_aim_init()

  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  user_input = request.form.get('user_input')  # Get the input text sent from JavaScript
  print(f"Received input: {user_input}")

  # Make the final response
  response =  cmdproc.process_string(user_input)

  # Return the response as JSON
  return jsonify({"response" : response})


def start():
  def run_flask():
      app.run(debug=True, host='127.0.0.1', port=5000) # Specify host and port explicitly

  # Run Flask in a separate process
  flask_process = multiprocessing.Process(target=run_flask)
  flask_process.start()

  # Continue with other tasks in your main program if needed
  print("Flask app is running in the background.")


if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)