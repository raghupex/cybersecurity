class SystemUser:
    def __init__(self, username, role):
        self.username, self.role = username, role

    def request_admin_action(self, action):
        print(f"\n[+] User: '{self.username}' | Assigned Role: '{self.role}'")
        print(f"    Action Requested: {action}")
        if self.role == "labadmin":
            print("    [RESULT] Access Granted. Administrative privilege confirmed.")
        else:
            print("    [RESULT] Access Denied. Insufficient privileges.")
            print("    [NOTE] Privilege escalation requires authorized authentication.")

    def elevate_privileges(self, token):
        print(f"\n[*] Attempting privilege escalation for '{self.username}'...")
        if token == "AUTH_ADMIN_SECRET":
            self.role = "labadmin"
            print(f"    [SUCCESS] Valid token. Role successfully escalated to: '{self.role}'")
        else:
            print("    [FAILED] Invalid authorization token. Privilege escalation denied.")

print("==================================================")
print("=== Privilege Escalation Simulation (RBAC Lab) ===")
print("==================================================")

user = SystemUser("student_user", "student")
user.request_admin_action("Update System Policy")
user.elevate_privileges("wrong_token")
user.request_admin_action("Update System Policy")
user.elevate_privileges("AUTH_ADMIN_SECRET")
user.request_admin_action("Update System Policy")

admin = SystemUser("labadmin_user", "labadmin")
admin.request_admin_action("Restart Network Service")
