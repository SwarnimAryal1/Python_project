from datetime import datetime as dt

path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = ["github.com", "www.github.com","www.reddit.com","reddit.com","youtube.com","www.youtube.com","facebook.com",
            "www.facebook.com","instagram.com","www.instagram.com"]
time = int(input("Enter the time (0-23) : "))
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 00) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          time):

        with open(path, "r+") as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

        print("All listed Website are Blocked")
        break
    else:
        with open(path, "r+") as file:
            content = file.readline()
            file.seek(0)

            for line in content:

                if not any(website in line for website in websites):
                    file.write(line)

            file.truncate()
        print("The websites are unblocked")
        break
