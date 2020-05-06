from flask import jsonify
from domainDAO import postDAO

class PostHandler:

    def createPost(row):
        post = {}
        #can not be a number or negative
        post['pid'] = row[0]
        #limit until 21 chars
        post['puser'] = row[1]
        #has to be a valid user
        post['pprovider'] = row[2]
        #must follow email patter
        post['pstatus'] = row[3]
        #must follow phone patter
        post['ptext'] = row[4]
        #picture
        #post['pattachment'] = row[5]
        #if it is a ticket
        post['tid']

        return post

        #we use dao to return the list so we build a json dictionary and jsonify it back  to the main
    def getAllPosts():


    
