import pyexcel
#1. prepare date


data =[
    {
        "name":"Huy",
        "age":20,
    },

    {
        "name":"Quan",
        "age":19,
    },
    {
        "name":"Duc",
        "age":18,

    },
]
#2 save
pyexcel.save_as(records=data, dest_file_name="sample.xlsx")