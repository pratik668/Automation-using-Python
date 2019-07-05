import facebook
def main():
  
  cfg = {
    "page_id"      : "*****************",
    "access_token" : "****************************"   
    }

  api = get_api(cfg)
  msg = "posted using python2 !!"
  status = api.put_wall_post(msg)
def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  print("succesfully posted")
  return graph
  
if __name__ == "__main__":
  main()

