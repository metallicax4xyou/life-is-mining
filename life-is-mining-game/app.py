from flask import Flask, jsonify
import dialogue_tree

app = Flask(__name__)

@app.route('/dialogue/<node_id>')
def get_dialogue(node_id):
    node = dialogue_tree.dialogue_tree.get(node_id)
    if node:
        return jsonify(node)
    else:
        return jsonify({"error": "Node not found"}), 404
# ... your existing code ...

if __name__ == '__main__':
    app.run(debug=True)

# Add this for Vercel deployment
application = app
