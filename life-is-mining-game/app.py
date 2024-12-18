@app.route('/dialogue/<node_id>')
def get_dialogue(node_id):
    node = dialogue_tree.dialogue_tree.get(node_id)
    if node:
            return jsonify(node)
    else:
            return jsonify({"error": "Node not found"}), 404