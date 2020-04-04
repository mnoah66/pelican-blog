Title: Addin to Create A Date Range
slug: excel-addin-date-range
date: 2019-04-04
category: Blog
Tags: excel,addin
share_post:true
Summary: How to get a week range value from a single date in Excel.
og_image:images/mileagematrix.png

Summarizing data with dates can be difficult.  For example, if you have a list of invoices with various dates, how do you summarize that for reporting?  If you want to report on weekly figures, you could use a helper column and drop in a `=WEEKNUM(cell)` formula to get an integer of the week.  To report on monthly figures, you could use `=MONTH(cell)` to get the integer of the number of the month (1 for January).  

But when looking at reports, nobody wants to see week numbers of the number of the month&mdash;they want to see something relatable.  We're going to look at three solutions to create fields to report on:
1. Week Beginning: for each invoice date, this gives us the Sunday date of that week.
2. Week Ending: for each invoice date, this gives us the Saturday date of that week.
3. Week Period: this gives us the Sun-Sat dates (03/31/19 - 04/06/19)

We'll then turn the Week Period into an add-in so that we can reuse it with ease.


Here's the data we'll be working with.  Copy and paste it into your spreadsheet:
<fieldset style="border-style: inset;border-width: 2px;max-width: 400px">
<table class="table">

<thead><tr class="tableizer-firstrow"><th>Invoice Date</th><th>Qty</th><th>Description</th><th>Unit Price</th><th>Amount</th></tr></thead><tbody>
 <tr><td>4/1/2019</td><td>1</td><td>Apples</td><td>0.79</td><td>$0.79</td></tr>
 <tr><td>4/2/2019</td><td>2</td><td>Oranges</td><td>0.98</td><td>$1.96</td></tr>
 <tr><td>4/3/2019</td><td>3</td><td>Apples</td><td>0.79</td><td>$2.37</td></tr>
 <tr><td>4/4/2019</td><td>4</td><td>Bananas</td><td>1.12</td><td>$4.48</td></tr>
 <tr><td>4/5/2019</td><td>2</td><td>Strawberry</td><td>2.34</td><td>$4.68</td></tr>
 <tr><td>4/6/2019</td><td>4</td><td>Apples</td><td>0.79</td><td>$3.16</td></tr>
 <tr><td>4/7/2019</td><td>5</td><td>Bananas</td><td>1.12</td><td>$5.60</td></tr>
 <tr><td>4/8/2019</td><td>3</td><td>Strawberry</td><td>2.34</td><td>$7.02</td></tr>
 <tr><td>4/9/2019</td><td>2</td><td>Apples</td><td>0.79</td><td>$1.58</td></tr>
 <tr><td>4/10/2019</td><td>2</td><td>Bananas</td><td>1.12</td><td>$2.24</td></tr>
 <tr><td>4/11/2019</td><td>5</td><td>Oranges</td><td>0.98</td><td>$4.90</td></tr>
 <tr><td>4/12/2019</td><td>1</td><td>Apples</td><td>0.79</td><td>$0.79</td></tr>
 <tr><td>4/13/2019</td><td>2</td><td>Oranges</td><td>0.98</td><td>$1.96</td></tr>
 <tr><td>4/14/2019</td><td>3</td><td>Apples</td><td>0.79</td><td>$2.37</td></tr>
 <tr><td>4/15/2019</td><td>4</td><td>Bananas</td><td>1.12</td><td>$4.48</td></tr>
 <tr><td>4/16/2019</td><td>2</td><td>Strawberry</td><td>2.34</td><td>$4.68</td></tr>
 <tr><td>4/17/2019</td><td>4</td><td>Apples</td><td>0.79</td><td>$3.16</td></tr>
 <tr><td>4/18/2019</td><td>5</td><td>Bananas</td><td>1.12</td><td>$5.60</td></tr>
 <tr><td>4/19/2019</td><td>3</td><td>Strawberry</td><td>2.34</td><td>$7.02</td></tr>
 <tr><td>4/20/2019</td><td>2</td><td>Apples</td><td>0.79</td><td>$1.58</td></tr>
 <tr><td>4/21/2019</td><td>2</td><td>Bananas</td><td>1.12</td><td>$2.24</td></tr>
 <tr><td>4/22/2019</td><td>5</td><td>Oranges</td><td>0.98</td><td>$4.90</td></tr>
</tbody>
</table>
</fieldset>


## The Formula's

Let's drop in three helper columns to the right of our data:

![Screenshot showing the sumifs formula we are using]({attach}images/billingperiodHelper.png)

In cell `F2`, enter the formula `=A2-WEEKDAY(A2)+1`

In cell `G2`, enter the formula `=A2-WEEKDAY(A2)+7`

Which gives us (make sure these cells are formatted as dates):
![Screenshot showing the sumifs formula we are using]({attach}images/sundaysaturday.png)


And now in cell `H2` we will combine these formulas to get the Sun-Sat dates.  They have to be formatted as text, otherwise the underlying integer date values will just be added together and we would end up with some bizarre future date.

`=TEXT(A2-WEEKDAY(A2)+1, "mm/dd/yyyy")&" - "&TEXT(A2-WEEKDAY(A2)+7, "mm/dd/yyyy")`

Drag the formula's down and you end up with three helper columns to help you report on the data.

![Screenshot showing the sumifs formula we are using]({attach}images/billingweek.png)


## Creating the Add-in

The formula's above can be difficult to remember.  With a user-defined function (UDF) we can re-use these formula's in any workbook we want just like we would with any built-in Excel formulas.

1. Open a separate workbook and right click on the worksheet tab: select `View Code`
2. In the menu, click Insert > Module.

    ![Screenshot showing the sumifs formula we are using]({attach}images/excelInsertModule.png)

3. Copy and paste the following into the white space:

    ```
    Function WEEKBEGINNING(rng As Range)
    WEEKBEGINNING = (rng - Weekday(rng) + 1)
    End Function
    Function WEEKENDING(rng As Range)
    WEEKENDING = (rng - Weekday(rng) + 7)
    End Function 
    Function BILLINGPERIOD(rng As Range)
    BILLINGPERIOD = Format((rng - Weekday(rng) + 1), "mm/dd/yy") & " - " & Format((rng - Weekday(rng) + 7), "mm/dd/yy")
    End Function
    ```

