from load_model import *


# Get the question
def question():
    question_client = input("<USER>: ")
    return question_client

question_client = question()

# Get the answer of the model
def model(instructions, question):
    output_model = client.models.generate_content(
                model="gemini-2.0-flash",
                contents= question,
                config = {
                    'system_instruction': instructions
                }
            )
    return output_model.text

output_model = model(bussines_instruction, question_client)
