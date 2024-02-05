from dotenv import load_dotenv
import os


# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        # Create client using endpoint and key       
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

        # Submit a question and display the answer
        user_question = ''
        # loop while question is not quit, ie, if input is quit, exit Q&A 
        while user_question.lower() != 'quit':
            # user makes question
            user_question = input('\nQuestion:\n')
            # API response
            response = ai_client.get_answers(question=user_question,
                                            project_name=ai_project_name,
                                            deployment_name=ai_deployment_name)
            # all the reposnses
            for candidate in response.answers:
                print(candidate.answer)
                # confidence rate
                print("Confidence: {}".format(candidate.confidence))
                #grounding 
                print("Source: {}".format(candidate.source))


    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
