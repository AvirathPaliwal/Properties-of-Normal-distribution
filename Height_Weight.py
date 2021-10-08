from os import stat
import pandas as pd
import statistics

df = pd.read_csv('height-weight.csv')
hlist = df['Height(Inches)'].tolist()
wlist = df['Weight(Pounds)'].tolist()


hmean = statistics.mean(hlist)
hmedian = statistics.median(hlist)
hmode = statistics.mode(hlist)
hstd = statistics.stdev(hlist)
wmean = statistics.mean(hlist)
wmedian = statistics.median(hlist)
wmode = statistics.mode(hlist)
wstd = statistics.stdev(hlist)
print('Mean , Median, Mode is {} , {} , {}'.format(hmean,hmedian,hmode))
print("\n")


hfirst_std_start ,hfirst_std_end = hmean - hstd , hmean +hstd
hsecond_std_start ,hsecond_std_end = hmean - (2*hstd) , hmean +(2*hstd)
hthird_std_start ,hthird_std_end = hmean - (3*hstd) , hmean +(3*hstd)
wfirst_std_start ,hfirst_std_end = hmean - hstd , hmean +hstd
wsecond_std_start ,hsecond_std_end = hmean - (2*hstd) , hmean +(2*hstd)
wthird_std_start ,hthird_std_end = hmean - (3*hstd) , hmean +(3*hstd)




hdata_within_1_std = [result for result in hlist if result> hfirst_std_start and result <hfirst_std_end]
hdata_within_2_std = [result for result in hlist if result> hsecond_std_start and result <hsecond_std_end]
hdata_within_3_std = [result for result in hlist if result> hthird_std_start and result <hthird_std_end]
wdata_within_1_std = [result for result in hlist if result> hfirst_std_start and result <hfirst_std_end]
wdata_within_2_std = [result for result in hlist if result> hsecond_std_start and result <hsecond_std_end]
wdata_within_3_std = [result for result in hlist if result> hthird_std_start and result <hthird_std_end]


print('{} % of data lies between 1 std'.format(len(hdata_within_1_std)*100.0/len(hlist)) )
print('{} % of data lies between 2 std'.format(len(hdata_within_2_std)*100.0/len(hlist)) )
print('{} % of data lies between 3std'.format(len(hdata_within_3_std)*100.0/len(hlist)) )


print('{} % of data lies between 1 std'.format(len(wdata_within_1_std)*100.0/len(hlist)) )
print('{} % of data lies between 2 std'.format(len(wdata_within_2_std)*100.0/len(hlist)) )
print('{} % of data lies between 3std'.format(len(wdata_within_3_std)*100.0/len(hlist)) )
