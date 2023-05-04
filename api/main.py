from flask import Blueprint, request
from flask_restful import Api, Resource
from api.utils import init_pinecone_openai, qa_transcript
import json 


# api initialization
qa_transcript_pb = Blueprint("QuestionAnswerBot",__name__)
AQ_Transcript_API = Api(qa_transcript_pb)

# openai_key configuration
init_pinecone_openai()

class QuestionAnswerBot(Resource):

    def get(self):
        return "Transcript Zoom chatbot is ready"
    
    def post(self):
        if not 'question' in request.json:
            return {"error": "question shouldn't be none"}
        
        if not 'clientId' in request.json:
            return {"error": "clientId shouldn't be none"}
        
        if not 'transcript_ids' in request.json:
            return {"error": "transcript_ids shouldn't be none"}
        
        question = request.json['question']
        transcript_ids = request.json['transcript_ids']
        clientId = request.json['clientId']

        print(f"transcript_ids: {transcript_ids}")
        # s = transcript_ids.replace("\\n", "").replace("\\", "").strip()

        # parse the string into a list using json.loads()
        # my_list = json.loads(s)
        # print(f"transcript_ids: {my_list}")

        context = qa_transcript(question=question,transcriptIDs=transcript_ids,clientID=clientId)['matches']

        if not len(context):
            return {"Question": question, context: ""}
        

        print(context[0]['metadata']['context'])
        return {
            "result":context[0]['metadata'],
        }
class Test(Resource):
    def get(self):
        return "Pinecone QA Server is working"
        
# routing
AQ_Transcript_API.add_resource(QuestionAnswerBot, "/qa") # <int:chunk_id>QuestionAnswerBot
AQ_Transcript_API.add_resource(Test, "/") # <int:chunk_id>QuestionAnswerBot
