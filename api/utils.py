import os 
import pinecone
import openai 
import pinecone


# pinecone settings
def init_pinecone_openai():
    pinecone_api_key = os.environ.get("PINECONE_API_KEY")
    pinecone_environment = os.environ.get("PINECONE_ENVIRONMENT")
    pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)
    openai.api_key = os.environ.get("OPENAI_API_KEY")



def qa_transcript(question,
                    clientID="12345",
                    transcriptIDs="1T1g8KNFkxzxhDgsxUjlYl2ow2YQoUc82"): # "1T73I4uA3BpNPWuCppF664YncSVBJhVJs"
    
    index_name = "dailyautomations"
    index = pinecone.Index(index_name)
    namespace = "Zoom"

    metadata = {
        "transcript_id": {
            # "$in": transcriptIDs
            "$eq": transcriptIDs

        },
        "clientID": {
            "$eq": clientID
        }
    }
    embedded_question = openai.Embedding.create(
        model="text-embedding-ada-002", input=question)['data'][0]['embedding']

    query_result = index.query(vector=embedded_question,
                               namespace=namespace,
                               filter=metadata,
                               top_k=1,
                               include_metadata=True)
    return query_result



