
failed_by_user = {}

with open("login_logs.txt", "r") as file:
    for line in file:
        parts = line.split()

        if len(parts) == 2 and parts[0].startswith("user=") and parts[1] == "status=failed":
            username = parts[0].split("=")[1]

            if username not in failed_by_user:
                failed_by_user[username] = 0

            failed_by_user[username] += 1

for username, count in failed_by_user.items():
    print(username, ":", count, "failed logins")

    if count >= 3:
        print("ALERT: Suspicious login activity for", username)

with open("report.txt", "w") as file:
    for username, count in failed_by_user.items():
        file.write(f"{username} : {count} failed logins\n")

        if count >= 3:
            file.write(f"ALERT: Suspicious login activity for {username}\n")
