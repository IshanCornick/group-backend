import csv

with open("jobs.csv", mode = "w") as csvfile:
    fieldnames = ["_title", "_field", "_qualification",  "_pay"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    writer.writerow({"_title": " Software Engineeer", "_field": "Computer Science", "_qualification": "Bachelors", "_pay": "37"})
    writer.writerow({"_title": " Software Engineeer", "_field": "Computer Science", "_qualification": "Masters", "_pay": "45"})
    writer.writerow({"_title": " Software Engineeer", "_field": "Computer Science", "_qualification": "pHd", "_pay": "56"})

    writer.writerow({"_title": "Data Scientist", "_field": "Computer Science", "_qualification": "Bachelors", "_pay": "32"})
    writer.writerow({"_title": "Data Scientist", "_field": "Computer Science", "_qualification": "Masters", "_pay": "41"})
    writer.writerow({"_title": "Data Scientist", "_field": "Computer Science", "_qualification": "pHd", "_pay": "49"})

    writer.writerow({"_title": "Mechanical Designer", "_field": "Engineering", "_qualification": "Bachelors", "_pay": "33"})
    writer.writerow({"_title": "Mechanical Designer", "_field": "Engineering", "_qualification": "Masters", "_pay": "42"})
    writer.writerow({"_title": "Mechanical Designer", "_field": "Engineering", "_qualification": "pHd", "_pay": "51"})

    writer.writerow({"_title": "Simulation Tester", "_field": "Engineering", "_qualification": "Bachelors", "_pay": "30"})
    writer.writerow({"_title": "Simulation Tester", "_field": "Engineering", "_qualification": "Masters", "_pay": "37"})
    writer.writerow({"_title": "Simulation Tester", "_field": "Engineering", "_qualification": "pHd", "_pay": "45"})

    writer.writerow({"_title": "Lawyer", "_field": "Law", "_qualification": "Bachelors", "_pay": "38"})
    writer.writerow({"_title": "Lawyer", "_field": "Law", "_qualification": "Masters", "_pay": "46"})
    writer.writerow({"_title": "Lawyer", "_field": "Law", "_qualification": "Masters ", "_pay": "55"})

    writer.writerow({"_title": "Judge", "_field": "Law", "_qualification": "Bachelors", "_pay": "35"})
    writer.writerow({"_title": "Judge", "_field": "Law", "_qualification": "Masters", "_pay": "48"})
    writer.writerow({"_title": "Judge", "_field": "Law", "_qualification": "Masters", "_pay": "62"})


    #writer.writerow({"_title": "Doctor", "_field": "Medical", "_qualification": "Masters", "_pay": "30"})
    # writer.writerow({"_title": "Video Game Designer", "_field": "Web", "_qualification": "Masters", "_pay": "300000"})
    # writer.writerow({"_title": "IT Technician", "_field": "Software", "_qualification": "Masters", "_pay": "150000"})
    # writer.writerow({"_title": "Software Engineer", "_field": "IT", "_qualification": "Masters", "_pay": "80000"})
    # writer.writerow({"_title": "Web Developer", "_field": "Software", "_qualification": "Masters", "_pay": "30200"})
    # writer.writerow({"_title": "Video Game Designer", "_field": "Web", "_qualification": "Masters", "_pay": "120000"})
    # writer.writerow({"_title": "IT Technician", "_field": "Software", "_qualification": "Masters", "_pay": "25"})
    # writer.writerow({"_title": "Software Engineer", "_field": "IT", "_qualification": "Masters", "_pay": "27"})
    # writer.writerow({"_title": "Web Developer", "_field": "Software", "_qualification": "Masters", "_pay": "32"})
    # writer.writerow({"_title": "Video Game Desgner", "_field": "Web", "_qualification": "Masters", "_pay": "30"})
    # writer.writerow({"_title": "IT Technician", "_field": "Software", "_qualification": "Masters", "_pay": "25"})
    # writer.writerow({"_title": "Software Engineer", "_field": "IT", "_qualification": "Masters", "_pay": "28"})
    # writer.writerow({"_title": "Web develpor", "_field": "Software", "_qualification": "Masters", "_pay": "32"})
    
    