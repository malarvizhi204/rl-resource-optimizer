from flask import Flask, jsonify, render_template
from flask_cors import CORS
import numpy as np
import random

app = Flask(__name__)
CORS(app)

# English labels for the Reinforcement Learning Agent
states = ["Low Demand", "Optimal", "High Demand"]
actions = ["Reduce Resources", "Maintain Current", "Increase Resources"]

@app.route('/')
def home():
    # Renders the main dashboard HTML
    return render_template('index.html')

@app.route('/optimize')
def optimize():
    # Simulate RL process with variations to ensure a wavy chart
    state_idx = random.randint(0, 2)
    action_idx = random.randint(0, 2)
    
    # Generate varied efficiency values for the dynamic wave effect
    base_efficiency = 88
    random_variation = random.randint(-6, 10)
    final_efficiency = base_efficiency + random_variation
    
    # Cap efficiency at 99% for realism
    if final_efficiency > 99: final_efficiency = 99

    return jsonify({
        "status": states[state_idx],
        "action": actions[action_idx],
        "efficiency": f"{final_efficiency}%"
    })

if __name__ == "__main__":
    # Ensure this is running in your terminal
    app.run(debug=True, port=5000)