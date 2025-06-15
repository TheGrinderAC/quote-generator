from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

# Simple quotes database
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Life is what happens to you while you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/quote')
def get_quote():
    """Return a random quote"""
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

@app.route('/api/add-quote', methods=['POST'])
def add_quote():
    """Add a new quote"""
    data = request.get_json()
    if data and 'quote' in data:
        quotes.append(data['quote'])
        return jsonify({"message": "Quote added successfully!", "total": len(quotes)})
    return jsonify({"error": "Invalid quote data"}), 400

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "quotes_count": len(quotes)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port, debug=False)