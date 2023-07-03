import json

JSON_FILE = 'questions.json'

with open(JSON_FILE) as f:
    question_data: dict = json.load(f)

qq = question_data['questions']
questions = []
answers = []
question_set = {}

for x in range(len(qq)):
    questions.append(qq[x]['q'])
    answers.append(qq[x]['a'])
    question_set[x] = set(questions[x].lower().split())

print(f"\nWith {len(question_set)} questions to search from.\nCTRL + C to exit.")

try:
    while True:

        cardinality_intersection_array = {}
        search_terms = set(input('\nPaste question >> ').lower().split())

        for x in range(len(question_set)):
            cardinality_intersection_array[x] = len(
                question_set[x].intersection(search_terms))

        sorted_values = sorted(
            cardinality_intersection_array.values())  # Sort the values
        results_by_rank = {}

        for i in sorted_values:
            for k in cardinality_intersection_array.keys():
                if cardinality_intersection_array[k] == i:
                    results_by_rank[k] = cardinality_intersection_array[k]
                    break

        result_keys = list(results_by_rank.keys())
        print(
            f'\nBest Match:\nQuestion {questions[result_keys[-1]]}\n{answers[result_keys[-1]]}')
except KeyboardInterrupt as e:
    print('KeyboardInterrupt - Exiting')
