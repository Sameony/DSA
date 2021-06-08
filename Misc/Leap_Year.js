function leappu(year){
    var mes="";
    if (year%4==0)
    {
        if (year%100==0)
        {
            if (year%400==0)
            {
                mes=year+" is a leap year";
            }
            else
            {
                mes=year+" is not a leap year";
            }
        }
        mes=year+" is leap year"
    } 
    else
    {
        mes=year+" is not a leap year";
    }
    return mes;
}

var year=prompt("Enter year: ");
leappu(year);