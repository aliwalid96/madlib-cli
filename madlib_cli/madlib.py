

def welcoming():
    print("you are wlcome in the madlib")
welcoming()

def prompting():
   adjective= input("please enter the  Adjective ")
   adjective_2=input("please enter the  Adjective  ")
   a_first_name=input("please enter the first name   ")
   past_tense_verb=input("please enter Past Tense Verb   ")
   another_a_first_name=input("please enter the first name   ")
   adjective_3=input("please enter the  Adjective ")
   adjective_4=input("please enter the  Adjective ")
   plural_noun=input("please enter a plural noun ")
   my_object={adjective:adjective,adjective_2:adjective_2}
   return my_object


def read_template():
    try:
      variable=prompting()
      print()
      print(f"I the {variable.adjective} and {variable.adjective_2} {variable.a_first_name}")
    except FileNotFoundError:
        pass

    finally:
        pass



def parse_template():
    pass
def merge():
    pass