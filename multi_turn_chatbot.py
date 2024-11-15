from vdbb import docsearch
import os

from groq import Groq


client = Groq(
    api_key="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"
)

messages=[
{"role":"system", "content": "You are a helpful asistant"},
]
system_prompt = "you are a help full assistant"

print ("==============================================================================")
while True:

    question = input("Type a question: ")

    r_docs = docsearch.similarity_search(query=question,k=2)

    context = "\n\n".join(doc.page_content for doc in r_docs)

    usr_message = f"""Answer the following question based on the context provided,If you
                do not know the answer say do not know. DO NOT SAY "Based on the given context"
                
                ## Question: 
                {question}

                ## Context:
                {context}

                """
    messages.append({"role":"user", "content": usr_message})
  

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )

    llm_response = chat_completion.choices[0].message.content

    messages.append({"role":"assistant", "content": llm_response})



    print(llm_response)

