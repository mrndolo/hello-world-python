#converting smileys into emojis

#get the input from the user and store it in message
message = input(">")
#break the message into individual words using .split, pass the boundary/separator(a space),
words = message.split(' ')
#define the emoji dictionary to map the characters into emojis
emojis = {
    ":)": "😊",
    ":(": "😌"
}
output = ""
#loop the message words to find the characters and swap them with emojis
for word in words:
    #use .get that will enable you supply a default value
    output += emojis.get(word, word) + " "
print(output)