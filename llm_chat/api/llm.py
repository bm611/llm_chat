# def get_model_list(genai):
#     models = genai.list_models()
#     res = []
#     for model in models:
#         if "gemini" in model.name:
#             res.append(model.name.split("/")[-1])
#     return res


# def get_response(model, prompt):
#     return model.generate_content(prompt).text


# async def get_response(model, prompt):
#     response = model.generate_content(prompt, stream=True)
#     for chunk in response:
#         yield chunk.text
