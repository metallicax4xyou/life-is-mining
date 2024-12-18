{  # Add this opening brace
    "start": {
            "speaker": "AI",
                    "text": "Welcome to the mine! What's your name, prospector?",
                            "options": [
                                        {"text": "My name is...", "next": "name_input"},
                                                ]
                                                    },
                                                        "name_input": {
                                                                "speaker": "Player",
                                                                        "text": "",  # Placeholder for player's name
                                                                                "options": [
                                                                                            {"text": "Continue", "next": "greet"}
                                                                                                    ]
                                                                                                        },
                                                                                                            "greet": {
                                                                                                                    "speaker": "AI",
                                                                                                                            "text": "Well, it's nice to meet you, {Player}. What brings you down to the mine today?",
                                                                                                                                    "options": [
                                                                                                                                                {"text": "I'm here to get rich!", "next": "get_rich"},
                                                                                                                                                            {"text": "I'm looking for adventure!", "next": "adventure"},
                                                                                                                                                                        {"text": "Just passing through.", "next": "passing_through"}
                                                                                                                                                                                ]
                                                                                                                                                                                    },
                                                                                                                                                                                        "get_rich": {
                                                                                                                                                                                                "speaker": "AI",
                                                                                                                                                                                                        "text": "Haha, don't we all! Well, be careful down there. Mining is a dangerous business.",
                                                                                                                                                                                                                "options": []  # This is an end node for now
                                                                                                                                                                                                                    },
                                                                                                                                                                                                                        "adventure": {
                                                                                                                                                                                                                                "speaker": "AI",
                                                                                                                                                                                                                                        "text": "Adventure, eh? You've come to the right place. But keep your wits about you; danger lurks around every corner.",
                                                                                                                                                                                                                                                "options": []  # This is an end node for now
                                                                                                                                                                                                                                                    },
                                                                                                                                                                                                                                                        "passing_through": {
                                                                                                                                                                                                                                                                "speaker": "AI",
                                                                                                                                                                                                                                                                        "text": "Just passing through.",  # Add the missing comma here
                                                                                                                                                                                                                                                                                "options": []  # This is an end node for now
                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                    }  # Add this closing brace