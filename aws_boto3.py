import boto3
import json 


db = boto3.resource('dynamodb')
table = db.Table('rh_offline_users')


def update_add(phone_num, ticker):
   response = table.update_item(
      Key={
         'user_id': phone_num
      },
      UpdateExpression="ADD watchlist :c",
      ExpressionAttributeValues={
         ":c": set({ticker})
      },
      ReturnValues="UPDATED_NEW"
   )


def retrieve(phone_num):
   response = table.get_item(
      Key={
         'user_id': phone_num
      }
   )
   if not response.get("Item"):
      return None
   return response["Item"].get("watchlist")


def remove(phone_num, ticker):
   response = table.update_item(
      Key={
         'user_id': phone_num
      },
      UpdateExpression="DELETE watchlist :c",
      ExpressionAttributeValues={
         ":c": set({ticker})
      },
      ReturnValues="UPDATED_NEW"
   )