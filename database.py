import csv
# with open('names.csv', 'w') as file:
#     fieldnames = ['question', 'title']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
questionid = 100000
with open('01_01_2014-12_31_2014_1_.csv') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        questionid += 1
        type = row['type']
        title = row['title']
        content = row['content']
        text = row['text']
        code= row['code']
        user_id = row['user_id']
        time = row['time']
        upvote = row['vote']
        reputation = row['reputation']
        accept_rate = row['accept_rate']
        tags = row['tag'].split()
        print(tags)
        if type == "question":
            with open('question_details.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow([questionid,user_id,time,text,title,content,tags,upvote,tags])
                #Here tags is array! We want to have different tag. How will we do that?
        if (type == "answer") | (type == "accepted-answer"):
            # Remove following and do answer schema here. Field as per discussion in whatsapp group.
            with open('answer_details.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow([questionid,user_id,time,text,title,content,tags,upvote,tags])
        password = user_id
        with open('users.csv','a') as file:
            # Remove following and do answer schema here . Put Password == user id. Login/Logout History. Include Tags and the weight.
            writer = csv.writer(file)
            writer.writerow([questionid, user_id, time, text, title, content, tags, upvote, tags])
