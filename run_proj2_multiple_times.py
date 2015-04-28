import os

thread_values = range(1, 9);

schedule_type = ('STATIC', 'DYNAMIC')
granularity = ('FINE', 'COARSE')

for s in schedule_type:
    for g in granularity:
        # print s, g
        for t in thread_values:
            os.system('icpc -openmp -DNUMT=%s -D%s -D%s project2.cpp  && ./a.out'%(str(t), s, g))
