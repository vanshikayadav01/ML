from typing import Text
import wolframalpha
while True:
    try:
       questions = input('Questions: ')
       if questions=="LEAVE":
           break
       else:
            try:
              app_id = '65LGR4-VXK64HQH2U'
              client = wolframalpha.Client (app_id)
              res = client.query(questions)
              answer = next (res.results).text
            
              print(answer)
            except:
               
                print("Sorry I can't understand you...try again...")
    except:
        pass        


