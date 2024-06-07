import os
import pandas as pd
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def autenticar_google():
    SCOPES = ['https://www.googleapis.com/auth/forms.body']

    flow = InstalledAppFlow.from_client_secrets_file('.json', SCOPES)
    creds = flow.run_local_server(port=0)

    return build('forms', 'v1', credentials=creds)

def criar_forms_google(service, form_title, questions):
    form = service.forms().create(body={'info': {'title': form_title}}).execute()
    form_id = form['formId']

    questions = questions[:30]

    requests = []
    for i, question in enumerate(reversed(questions)):
        options = []
        seen_values = set()
        for option in ['A', 'B', 'C', 'D']:
            if pd.notna(question[option]):
                value = str(question[option]).replace('\n', ' ').replace('\r', ' ').strip()
                if value not in seen_values:
                    options.append({'value': value})
                    seen_values.add(value)

        if not options:
            continue  # Skip questions without options

        requests.append({
            'createItem': {
                'item': {
                    'title': question['title'].replace('\n', ' ').replace('\r', ' ').strip(),
                    'questionItem': {
                        'question': {
                            'required': True,  # Set the question to be required
                            'choiceQuestion': {
                                'type': 'RADIO',
                                'options': options
                            }
                        }
                    }
                },
                'location': {
                    'index': 0
                }
            }
        })

    if requests:
        for request in requests:
            service.forms().batchUpdate(
                formId=form_id,
                body={'requests': [request]}
            ).execute()
            time.sleep(1)
    
    return form_id

def main():
    service = autenticar_google()
    
    excel_file = 'teste1.xlsx'
    df = pd.read_excel(excel_file)

    start_row = 1  # Starting from the second row (index 1)
    num_questions_per_form = 30
    num_forms = int(input("Quantos formulários você quer criar? "))

    for i in range(num_forms):
        start = start_row + i * num_questions_per_form
        end = start + num_questions_per_form
        questions = [{'title': row['Conteúdo'], 'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']} for index, row in df.iloc[start:end].iterrows()]

        form_title = f'ExameTopcs 798Q - 30Q {i+1}'
        form_id = criar_forms_google(service, form_title, questions)

        print(f"O Formulario Automatizado {i+1} está pronto, acesse essa URL: https://docs.google.com/forms/d/{form_id}")

if __name__ == '__main__':
    main()
