Title: Tracking Excel Attendance with Pandas
slug: pandas-excel-attendance
date: 2018-11-25
category: Blog
Tags: python, pandas
share_post:true
Summary: A simple Pandas tutorial to track volunteer hours from Excel file data. 
og_image:images/mileagematrix.png


In this tutorial we're going to look at some data analysis exercises using the Python library [pandas](https://pandas.pydata.org/).  We'll pretend that we're a non-profit agency with a few reporting requirements: provide monthly reports of total volunteer hours, and report on volunteers that fall short of volunteer hour obligations.  The data we'll be using is an Excel file where each row is the name of the volunteer, the date of service, and how many minutes they volunteered:
    
<fieldset style="border-style: inset;border-width: 2px;max-width: 300px">
<table class="table">
<thead><tr class="tableizer-firstrow"><th>Volunteer Name</th><th>Date</th><th>Minutes</th></tr></thead><tbody>
 <tr><td>Sally</td><td>2/12/2018</td><td>800</td></tr>
 <tr><td>Frank</td><td>2/12/2018</td><td>985</td></tr>
 <tr><td>Sally</td><td>2/13/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>2/13/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>2/14/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>2/14/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>2/16/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>2/16/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>2/20/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>2/20/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>2/21/2018</td><td>375</td></tr>
 <tr><td>Frank</td><td>2/21/2018</td><td>375</td></tr>
 <tr><td>Sally</td><td>2/22/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>2/22/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>2/23/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>2/23/2018</td><td>100</td></tr>
 <tr><td>Sally</td><td>2/26/2018</td><td>355</td></tr>
 <tr><td>Frank</td><td>2/26/2018</td><td>1300</td></tr>
 <tr><td>Sally</td><td>2/27/2018</td><td>900</td></tr>
 <tr><td>Frank</td><td>2/27/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>2/28/2018</td><td>650</td></tr>
 <tr><td>Frank</td><td>2/28/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>3/3/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>3/3/2018</td><td>450</td></tr>
 <tr><td>Sally</td><td>3/5/2018</td><td>1000</td></tr>
 <tr><td>Frank</td><td>3/5/2018</td><td>500</td></tr>
 <tr><td>Sally</td><td>3/7/2018</td><td>300</td></tr>
 <tr><td>Frank</td><td>3/7/2018</td><td>475</td></tr>
 <tr><td>Sally</td><td>3/9/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>3/9/2018</td><td>855</td></tr>
 <tr><td>Sally</td><td>3/11/2018</td><td>450</td></tr>
 <tr><td>Frank</td><td>3/11/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>3/13/2018</td><td>200</td></tr>
 <tr><td>Frank</td><td>3/13/2018</td><td>890</td></tr>
 <tr><td>Sally</td><td>3/15/2018</td><td>700</td></tr>
 <tr><td>Frank</td><td>3/15/2018</td><td>100</td></tr>
 <tr><td>Sally</td><td>3/17/2018</td><td>800</td></tr>
 <tr><td>Frank</td><td>3/17/2018</td><td>360</td></tr>
 <tr><td>Sally</td><td>3/19/2018</td><td>355</td></tr>
 <tr><td>Frank</td><td>3/19/2018</td><td>400</td></tr>
 <tr><td>Sally</td><td>3/21/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>3/21/2018</td><td>1200</td></tr>
 <tr><td>Sally</td><td>3/23/2018</td><td>360</td></tr>
 <tr><td>Frank</td><td>3/23/2018</td><td>360</td></tr>
</tbody></table>
</fieldset>

##  Monthly Attendance

First we'll import Pandas, Numpy, and calendar.  You may have to `pip install pandas, numpy`

```bash
>>> import pandas as pd
>>> import numpy as np
>>> import calendar
  
```

Then load the data file into a variable `df` as pandas will create a DataFrame from your data.  Since we will be doing a lot of work with the date column in our Excel file, we're going to include the `parse_dates` parameter:

```bash
>>> df = pd.read_excel('volunteerdata.xlsx', parse_dates=['Date'])```
```

To get the total minutes of volunteer time for ALL volunteers for ALL data:

```bash
>>> df['Minutes'].sum()  #21715``` 
```

Now we want a sum of the total volunteer hours by month, so we use `groupby` on the Date column of our dataframe, and we convert the month to the month name using month_name('en')

```bash
>>> df.groupby(df['Date'].dt.month_name('en'))['Minutes'].sum()
Date
February    10520
March       11195
Name: Minutes, dtype: int64
```

And now to include a subtotal per volunteer per month, we pass in a list of what we want to `groupby`, this time the `Date` and `Volunteer Name` column from our dataframe:

```bash
>>> df.groupby([df['Date'].dt.month_name('en'), df['Volunteer Name']])['Minutes'].sum()
Date      Volunteer Name
February  Frank            5280
          Sally      5240
March     Frank            5950
          Sally      5245
```

Great!  What we want to accomplish now is to add a subtotal for the month, so we can see at-a-glance our monthly totals and the total for each of our volunteers  This is a two step process in which we create a pivot table of our dataframe, and then concatenate it back into a dataframe.  First to make thing easier, we'll assign the above to variable `monthly_totals`:

```bash
>>> monthly_totals = df.groupby([df['Date'].dt.month_name('en'), df['Volunteer Name']])['Minutes'].sum()
```

Now, we'll create a Pivot Table out of `monthly_totals`:

```bash
>>> monthly_table = pd.pivot_table(monthly_totals, values=['Minutes'],
                       index=['Date', 'Volunteer Name'],
                       fill_value=0, aggfunc=np.sum, dropna=True)
```

And then concatenate which will return a DataFrame with out subtotals per volunteer and month, as well as a Grand Total:

```bash
>>> final_table = pd.concat([
    d.append(d.sum().rename((k, 'Total')))
    for k, d in monthly_table.groupby(level=0)
]).append(monthly_table.sum().rename(('Grand', 'Total')))

```
Resulting in...

<img style="max-width: 100%; height:  auto;" src='/images/pandasSubtotals.png'>

##  Under Hours

In our pretend non-profit agency the funding sources require that each volunteer give at least 30 hours/week.  What we need to do is go back to our original DataFrame and sum our Minutes, grouping by the week.  For this exercise, we don't care if the volunteer gave 30+ hours.  Instead we want to see what volunteers were under 30 hours and by how much.

Let's check `df` again and make sure it's our original data:

```bash
>>> df.head()
  Volunteer Name  Date      Minutes
0 Sally  2018-02-12  800
1 Sally  2018-02-13  360
2 Sally  2018-02-14  360
3 Sally  2018-02-16  360
4 Sally  2018-02-20  360
```

Then we have to subtract one week from each `Date` as we'll want our weekly totals to show the Sunday of that week:

```bash
>>> df['Date'] = df['Date'] - pd.to_timedelta(7, unit='d')
```

Now we'll assign `weekly_total` to a new DataFrame with weekly totals, accomplished by using Grouper where the 'key' is the column that we want to group, and the 'freq' is set to 'W' for a weekly frequency beginning on Sundays.  We then reset_index so that we can sort_values by Date for easier reading.  And since we're changing the data, we'll also rename the columns to match the data.

```bash
>>> weekly_totals = df.groupby(['Volunteer Name', pd.Grouper(key='Date', freq='W')])['Minutes']\
                    .sum()\
                    .reset_index()\
                    .sort_values('Date')\
                    .rename(index=str, 
                            columns={'Volunteer Name':'Name',
                                     'Date':'Week Beginning',
                                     'Minutes':'Total Minutes'})
```
Resulting in...

<img style="max-width: 100%; height:  auto;" src='/images/pandasWeeklyTotals.png'>

We see that Frank volunteered 2065 minutes in the week beginning Feb 11th, but only 1195 minutes the week beginning Feb 18th.  Confirm this by manually looking at the data in the Excel file.  If you only have a few volunteers, this is likely all you'll need and you can do your calculations manually with this report.  But since you're using Python and pandas, you most likely have lots of volunteers/data, so we need to go a step further and identify all of the volunteers with minutes less than 1800 (30 hours).

## Pandas .apply

.apply is a method that will apply a function to each row of data.  We'll use a lambda function to check if the total minutes is less than 1800, and if so, display the total minutes under 1800 for each week.  We'll store this in a variable called `underMinutes`

```bash
>>> underMinutes = weekly_totals['Minutes'].apply(lambda mins: 1800 - mins if mins < 1800 else (0)).groupby([weekly_totals['Volunteer Name'],weekly_totals['Date']]).sum().reset_index()
>>> underMinutes
   Volunteer Name       Date  Minutes
0          Frank 2018-02-11        0
1          Frank 2018-02-18      605
2          Frank 2018-02-25        0
3          Frank 2018-03-04        0
4          Frank 2018-03-11      450
5          Frank 2018-03-18        0
6          Sally 2018-02-11        0
7          Sally 2018-02-18      345
8          Sally 2018-02-25        0
9          Sally 2018-03-04        0
10         Sally 2018-03-11      100
11         Sally 2018-03-18      725
```

Now we can easily see that Frank was short in the week of Feb. 18th and March 11th, and Sally was short in the weeks of Feb. 18th, March 11th, and March 18th.  We can then apply the same table and concat logic that we previously did to obtain subtotals and grand totals for our report for volunteers with poor attendance.  
