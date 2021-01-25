dates = ["1st Oct 2052", "2nd Jun 1933", "3rd May 1960", "20th Sep 1958", "16th Mar 2068", "25th May 1912", "16th Dec 2018"]

def preprocessDate(dates):
    ans = []
    for i in range(len(dates)):
        date = dates[i].split()
        day = date[0][:-2]
        if len(day) == 1:
            day = str(0)+str(day)
        month = date[1]
        year = date[2]
        if month == 'Jan':
            month = '01'
        elif month == 'Feb':
            month = '02'
        elif month == 'Mar':
            month = '03'
        elif month == 'Apr':
            month = '04'
        elif month == 'May':
            month = '05'
        elif month == 'Jun':
            month = '06'
        elif month == 'Jul':
            month = '07'
        elif month == 'Aug':
            month = '08'
        elif month == 'Sep':
            month = '09'
        elif month == 'Oct':
            month = '10'
        elif month == 'Nov':
            month = '11'
        elif month == 'Dec':
            month = '12'

        res = '{}-{}-{}'.format(year,month,day)
        ans.append(res)
    return ans

print(preprocessDate(dates))