from flask import Flask, request, jsonify
from chat_gpt import ChatGPTBotAPI
import os

ChatGPTBotApi = ChatGPTBotAPI(os.environ["api_key"])

app = Flask('Assessment_task')

@app.route("/prompt", methods=['POST'])
def create_prompt():
    prompt = request.get_json().get('prompt')
    if prompt:
        ChatGPTBotApi.create_prompt(prompt = prompt)
        return jsonify({"success": True,"messages": "Prompt Added"}), 200
    return jsonify({"success": False,"messages": "prompt required"}), 400


@app.route("/prompt/<prompt_id>", methods=['GET', 'PATCH', 'DELETE'])
def manage_prompt(prompt_id):
    
    if request.method == "GET":
        try:
            return jsonify({"success": True, "message": "", "data": {"response": ChatGPTBotApi.get_response(prompt_index = int(prompt_id))}}), 200
        except:
            return jsonify({"success": False,"messages": "Index is not valid"}), 400
    elif request.method == "DELETE":
        try:
            ChatGPTBotApi.delete_prompt(prompt_index = int(prompt_id))
            return jsonify({"success": True, "message": "Deleted Successfully"}), 200
        except:
            return jsonify({"success": True, "message": "Deleted Successfully"}), 200
    elif request.method == "PATCH":
        new_prompt = request.get_json().get('new_prompt')
        if new_prompt == None or new_prompt == "":
            return jsonify({"success": False,"messages": "Enter a new valid prompt"}), 400
        else:
            try:
                ChatGPTBotApi.update_prompt(prompt_index = int(prompt_id), new_prompt = new_prompt)
                return jsonify({"success": True,"messages": "Updated Successfully"}), 200
            except Exception as e:
                print(e)
                return jsonify({"success": False,"messages": "Enter a valid index"}), 400