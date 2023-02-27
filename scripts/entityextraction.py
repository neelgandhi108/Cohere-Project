import cohere
import datetime

api_key = 'nidVfcm5xYEyW8etrREYrKmXjcdD65sCGVhxRJOl'
co = cohere.Client(api_key)

job_entities =[
      ("text", "Bachelor",
        "start", '0',
        "end", '8',
        "token_start", '0',
        "token_end", '0',
        "entityLabel", "DIPLOMA"),
     ("text", "Mechanical Engineering",
        "start", '21',
        "end", '43',
        "token_start", '4',
        "token_end", '5',
        "entityLabel", "DIPLOMA_MAJOR"),
     ("text", "developing",
        "start", '89',
        "end", '99',
        "token_start", '15',
        "token_end", '15',
        "entityLabel", "SKILLS"),
     ("text", "connector related products",
        "start", '137',
        "end", '163',
        "token_start", '22',
        "token_end", '24',
        "entityLabel", "SKILLS")
 ]
    
class cohereExtractor():
    def __init__(self, examples, example_labels, labels, task_desciption, example_prompt):
        self.examples = examples
        self.example_labels = example_labels
        self.labels = labels
        self.task_desciption = task_desciption
        self.example_prompt = example_prompt

    def make_prompt(self, example):
        examples = self.examples + [example]
        labels = self.example_labels + [""]
        return (self.task_desciption +
                "\n---\n".join( [examples[i] + "\n" +
                                self.example_prompt + 
                                 labels[i] for i in range(len(examples))]))

    def extract(self, example):
      extraction = co.generate(
          model='large',
          prompt=self.make_prompt(example),
          max_tokens=10,
          temperature=0.1,
          stop_sequences=["\n"])
      return(extraction.generations[0].text[:-1])


cohereJobExtractor = cohereExtractor([e[1] for e in job_entities], 
                                       [e[11] for e in job_entities], [],
                                       "", 
                                       "extract the EntityLabel:")
print(cohereJobExtractor.make_prompt(''))

num_posts = 5

job_list = job_entities(size=num_posts, 
      subreddit="jobs", 
      sort_type="score", 
      sort="desc")

# Show the list
# job_list

print(job_list)
