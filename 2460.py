#https://ahoy.twilio.com/twilio-products?utm_source=google&utm_medium=cpc&utm_term=twilio&utm_campaign=G_S_Brand_Latam&gclsrc=aw.ds&gclid=EAIaIQobChMIp6iI77vc7AIVEIWRCh2wAgEHEAAYASAAEgJMgfD_BwE
def main():
  len_people_queue = int(input())
  id_people_queue = input().split()

  len_people_leave_queue = int(input())
  id_people_who_leave_queue = input().split()

  for id_people in id_people_who_leave_queue:
      id_people_queue.remove(id_people)

  print(' '.join(id_people_queue))

if __name__ == '__main__':
  main()
