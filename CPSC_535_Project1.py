#!/usr/bin/python3


#message is a string containing the message 
#list contains tuples with the word to be replaced and what will replace it 
def replace(message, list):
    prev = [] #used to keep track of the previoulsy replaced words
    for target, x in list:
        index =  message.find(target)
        while index > 0:
            
            if index not in prev:
                #chech that the first word if is target had nothing but spaces or punctuation
                #after it
                message =message[:index] + x + message[index + len(target):]
                prev.append(index)

                
                for i in range(len(prev)):
                    if prev[i] > index: #update previously replaced words indexes 
                        prev[i] +=  len(x) - len(target)
                            
            
            y =  index + len(target)

            #search remaining message
            index = message[y:].find(target)
            if index > 0:
                index += y  #readjusting index to be relavant for the whole string if it finds something 
    return message




ex1message = "Our youngest students have been asked to stay today until the end of the classes. The old principal."
ex1list = [("old", "young"),  ("student", "teacher"),  ("to", "yester"),  ("end", "beginning"), ("new", "old"), ("young","new")]

ex2message = "Please come now to my apartment! We have a birthday party surprise for my roommate and I do not know what song to choose. Alison"
ex2list = [("now", "later"), ("party","gift"), ("we", "I")]

ex3message = "Please come now to my apartment! We have a birthday party surprise for my roommate and I do not know what song to choose. Alison"
ex3list = [("now to", "later by"), ("choose.","give!"), ("we", "I")]

if __name__ == "__main__":

    print("ex1 input: ", ex1message)
    print("ex1 result: ", replace(ex1message, ex1list) )
    

    print("ex2 input: ", ex2message)
    print("ex2 result: ", replace(ex2message, ex2list))
    

    print("ex3 input: ", ex3message)
    print("ex3 result: ", replace(ex3message, ex3list))
    