# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "example hw=no,ms=single,ai=low,ce=no for this it triggers 2 rules they are rule 3&4 which contradicts the ,utually exclusive condition."
    answers["(b) explain"] = "example ms=divorced,ce=yes,ai=high for this there is no rule specified,which contradicts the function of exhaustive"
    answers["(c) explain"] = "example ho=yes,ms=single triggers rule 1&3 ,hence it is not mutually exclusive ordering is very important in this case"
    answers["(d) explain"] = "default class is needed beacuse if any record doesnt comes under any specified rule still it has a chance to come under a rule by defining a default class."


    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = yes
    answers["(b)"] = no
    answers["(c)"] = no

    # explain-string: explanation in english prose
    answers["(a) example"] = "each rule specifies a unique combination of all attributes and doesnt overlap with one another. hence it is mutually exclusive."
    answers["(b) example"] = "there is no rule specified for coldblooded that gives birth which says that the given data is not exhaustive"
    answers["(c) example"] = "since the rules are mutually exclusive there is no need for ordering."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = "true"
    answers["(b)"] = "true"
    answers["(c)"] = "false"
    answers["(d)"] = "false"

    # explain_string: explanation in english prose
    answers["(a) explain"] = "asss"
    answers["(b) explain"] = "asssdffg"
    answers["(c) explain"] = "asdfjgigedg"
    answers["(d) explain"] = "abfberjhfjkewf"

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.24

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = None
    answers["(d) Row 2"] = None
    answers["(d) Row 3"] = None
    answers["(d) Row 4"] = None

    # float between 0 and 1
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "if we choose k=1 it will result in overfitting or if we choose k=50 it might go for underfitting because there is much noise in the 1st figure region as it is tightly bonded."
    answers["(b) explain"] = " if we choose k=1 it will result in overfitting or if we choose k=50 it might go for underfitting because there is much noise in the overlapped region."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.5
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.5
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = None 
    answers["(b) P(R|+)"] = 0.12
    answers["(b) P(R|-)"] = 0.02

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "probability for the positive class is higher when compared to the probablity of the negative class."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.45

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "no"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.55

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "no"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "p(a=1)*p(b=1)=p(a=1,b=1)then only we can say they are conditionally independent but here it is not same."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
