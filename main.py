import pandas as pd
import requests

d = pd.read_csv("student.csv")


d["Total"] = (
    d["Tamil"] +
    d["English"] +
    d["maths"] +
    d["science"] +
    d["social"]
)

d["Average"] = d["Total"] / 5

total_students = len(d)
overall_avg = d["Average"].mean()

max_avg = d["Average"].max()
toppers = d[d["Average"] == max_avg]


weak_students = d[d["Average"] < 35]

tamil_avg = d["Tamil"].mean()
english_avg = d["English"].mean()
maths_avg = d["maths"].mean()
science_avg = d["science"].mean()
social_avg = d["social"].mean()

with open("report.txt", "w") as file:
    file.write("STUDENT PERFORMANCE REPORT\n")
    file.write("=" * 35 + "\n\n")

    file.write(f"Total Students : {total_students}\n")
    file.write(f"Overall Average: {overall_avg:.2f}\n\n")

    file.write("TOPPERS\n")
    for name in toppers["Name"]:
        file.write(f" {name}\n")

    file.write("\nWEAK STUDENTS\n")
    if len(weak_students) == 0:
        file.write("No weak students found\n")
    else:
        for name in weak_students["Name"]:
            file.write(f"- {name}\n")

    file.write("\nSUBJECT WISE AVERAGES\n")
    file.write(f"Tamil   : {tamil_avg:.2f}\n")
    file.write(f"English : {english_avg:.2f}\n")
    file.write(f"Maths   : {maths_avg:.2f}\n")
    file.write(f"Science : {science_avg:.2f}\n")
    file.write(f"Social  : {social_avg:.2f}\n")

print("Report generated successfully!")

students = d.to_dict(orient="records")


webhook_url = "https://hook.eu1.make.com/vbwiehagffk6g4beugz9z1cg769x5t62"


response=requests.post(webhook_url, json={
    "Students": students
})
print(response.status_code)
print(response.text)