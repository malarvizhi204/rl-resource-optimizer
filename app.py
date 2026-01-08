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
    # Page 1: Welcome/Entry page
    return render_template('index.html')

@app.route('/config')
def configuration():
    # Page 2: Configuration/Setup page
    return render_template('config.html')

@app.route('/dashboard')
def dashboard():
    # Page 3: Final RL Visualization
    return render_template('dashboard.html')

@app.route('/optimize')
def optimize():
    state_idx = random.randint(0, 2)
    action_idx = random.randint(0, 2)
    base_efficiency = 88
    random_variation = random.randint(-6, 10)
    final_efficiency = base_efficiency + random_variation
    if final_efficiency > 99: final_efficiency = 99

    return jsonify({
        "status": states[state_idx],
        "action": actions[action_idx],
        "efficiency": f"{final_efficiency}%"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
