def handledata(context):
    result={"contacts":[],'subject':'1','date':'1'}
    for i in context['contacts']:
        result["contacts"].append(i["hkuid"])
    result['subject']=context['subject']['hkuid']
    result['date']=context['subject']['datetime']
    return result