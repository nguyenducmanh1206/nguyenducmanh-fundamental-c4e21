r1={
    "#":1,
    "name":"huy",
    "level":25,
    "hour":14,

}
r2={
    "#":2,
    "name":"hoa",
    "level":20,
    "hour":7,
}
r3={
    "#":3,
    "name":"tam",
    "level":15,
    "hour":20,
}









salary_list=[r1, r2, r3]
total_wage =0
wage_list= []
for salary in salary_list:
    name = salary["name"]
    hour = salary["hour"] 
    level = salary["level"]
    wage_info={
        "name":name,
        "wage":hour * level,
        "hour":hour,

    }
    wage_list.append(wage_info)
    wage = hour * level
    total_wage += wage
    print("total wage: ", total_wage)
import pyexcel    
pyexcel.save_as(records=wage_list, dest_file_name="bangluong.xlsx")







