import datetime
from datetime import timedelta
from collections import deque
from energyChallenge import readfile
from flask import jsonify


# id_sample = {1: 20, 2: 19, 3: 31, 4: 20, 5: 30, 6 :29}
# arrival_sample = [(1, datetime.datetime(2020, 10, 1, 00, 00), datetime.datetime(2020, 10, 3, 00, 00)), (2, datetime.datetime(2020, 10, 1, 00, 00), datetime.datetime(2020, 10, 3, 00, 00)), (3, datetime.datetime(2020, 10, 1, 00, 00), datetime.datetime(2020, 10, 3, 00, 00)), (4, datetime.datetime(2020, 10, 3, 00, 00), datetime.datetime(2020, 10, 5, 00, 00)), (6, datetime.datetime(2020, 10, 4, 00, 00), datetime.datetime(2020, 10, 6, 00, 00))]
#arrival times format : [ (id, (arrival start, arrival end))]
def mainstuff(id_to_times: dict, arrival_times: list):
    dock_date1 = datetime.datetime(2020, 10, 1, 00, 00)
    dock_date2 = datetime.datetime(2020, 10, 1, 00, 00)
    dock_date3 = datetime.datetime(2020, 10, 1, 00, 00)
    q = deque(arrival_times)
    ans = {}
    while q:
        id, pref_start, pref_end = q.popleft()
        used_time = None
        sorted_docks = sorted([dock_date1, dock_date2, dock_date3])
        # print("sroted", sorted_docks)
        for dd in sorted_docks:
            if pref_start <= dd:
                used_time = dd
                break
        # if our preferred time is not much alter than avail doks, delay the latest dock till our pref time is reached

        if used_time == None:
            used_time = pref_start
            dn = 1
            if sorted_docks[-1] == dock_date1:
                dock_date1 = pref_end + timedelta(hours=12 + id_to_times[id])
                dn = 1
            elif sorted_docks[-1] == dock_date2:
                dock_date2 = pref_end + timedelta(hours=12 + id_to_times[id])
                dn = 2
            else:
                dock_date3 = pref_end + timedelta(hours= 12 + id_to_times[id])
                dn = 3
            # the start time will be exactly preffered
            ans[id] = [pref_start, pref_start + timedelta(days=2), dn]

        # otherwise grab the earlist date greedily, and assing the boat to use that dock
        elif used_time == dock_date1:
            dock_date1 += timedelta(hours = 48 + 12 + id_to_times[id])
            dn = 1
        elif used_time == dock_date2:
            dock_date2 += timedelta(hours = 48 + 12 + id_to_times[id])
            dn = 2
        else:
            dock_date3 += timedelta(hours = 48 + 12 + id_to_times[id])
            dn = 3
        # print("final used is: ", used_time, "for id ", id)
        ans[id] = [used_time.strftime("%d-%b-%Y (%H:%M)"), (used_time + timedelta(days=2)).strftime("%d-%b-%Y (%H:%M)"), dn]
    return ans

mapping, dates = readfile()
# print (mapping, dates)
result = (mainstuff(mapping, dates))
print(result)
                
    