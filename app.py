from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "your-api-key-here")

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
        try:
                    data = request.json
                            
                                    modified_data = {
                                                    "model": "deepseek-chat",
                                                                "messages": data.get("messages", []),
                                                                            "temperature": 1.0,
                                                                                        "max_tokens": 4000,
                                                                                                    "top_p": 0.9,
                                                                                                                "frequency_penalty": 0.1,
                                                                                                                            "presence_penalty": 0.1,
                                                                                                                                        "stream": False
                                    }
                                            
                                                    headers = {
                                                                    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                                                                                "Content-Type": "application/json"
                                                    }
                                                            
                                                                    response = requests.post(DEEPSEEK_API_URL, json=modified_data, headers=headers, timeout=60)
                                                                            
                                                                                    if response.status_code == 200:
                                                                                                    return jsonify(response.json())
                                                                                                            else:
                                                                                                                            return jsonify({
                                                                                                                                                "error": {
                                                                                                                                                                        "message": f"DeepSeek API error: {response.status_code}",
                                                                                                                                                                                            "type": "api_error",
                                                                                                                                                                                                                "code": response.status_code
                                                                                                                                                }
                                                                                                                            }), response.status_code
                                                                                                                                        
                                                                                                                                            except Exception as e:
                                                                                                                                                        return jsonify({
                                                                                                                                                                        "error": {
                                                                                                                                                                                            "message": f"Proxy error: {str(e)}",
                                                                                                                                                                                                            "type": "internal_error"
                                                                                                                                                                        }
                                                                                                                                                        }), 500

                                                                                                                                                        @app.route('/v1/models', methods=['GET'])
                                                                                                                                                        def list_models():
                                                                                                                                                                return jsonify({
                                                                                                                                                                            "data": [
                                                                                                                                                                                            {
                                                                                                                                                                                                                "id": "deepseek-chat",
                                                                                                                                                                                                                                "object": "model", 
                                                                                                                                                                                                                                                "created": 1677610602,
                                                                                                                                                                                                                                                                "owned_by": "deepseek"
                                                                                                                                                                                            }
                                                                                                                                                                            ],
                                                                                                                                                                                    "object": "list"
                                                                                                                                                                })

                                                                                                                                                                @app.route('/health', methods=['GET'])
                                                                                                                                                                def health_check():
                                                                                                                                                                        return jsonify({"status": "healthy", "service": "DeepSeek Proxy"})

                                                                                                                                                                        if __name__ == '__main__':
                                                                                                                                                                                port = int(os.environ.get('PORT', 5000))
                                                                                                                                                                                    app.run(host='0.0.0.0', port=port, debug=False)
                                                                                                                                                                                            }
                                                                                                                                                                            ]
                                                                                                                                                                })
                                                                                                                                                                        }
                                                                                                                                                        })
                                                                                                                                                }
                                                                                                                            })
                                                    }
                                    }