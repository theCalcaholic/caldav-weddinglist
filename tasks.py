import caldav
import vobject

def load_gift_list(username, password, cal_url):

    client = caldav.DAVClient(url=cal_url, username=username, password=password)
    calendar = caldav.Calendar(client=client, url=cal_url)
    wunsch_list = calendar.todos(include_completed=True)
    outputliszt =[]

    for item in wunsch_list:
        #print (item.data)

        faucal = vobject.readOne(item.data)
        #print(faucal.vtodo.summary.value)

        is_completed = False
        if 'status' in faucal.vtodo.contents:
            status = faucal.vtodo.contents['status'][0].value
            if status in ['COMPLETED', 'CANCELLED']:
                is_completed = True

        dictionary = {
            'name': faucal.vtodo.summary.value,
            'completed': is_completed,
        }
        
        outputliszt.append(dictionary)
        
        
        
    return outputliszt

# ['COMPLETED', 'NEEDS-ACTION', 'CANCELLED', 'IN-PROCESS']