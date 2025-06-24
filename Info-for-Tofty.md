## 🔧 Managing Users with `manage.py`

This app includes a CLI command to promote users to **admin** via the terminal.

### 📜 Command: `make_admin`

You can run this command to grant admin privileges to a user, and optionally set a new password.

### 🛠 Usage:

```bash
python manage.py make_admin <email> [--password NEW_PASSWORD]
```

### 📌 Examples:

#### ➕ Promote user to admin:

```bash
python manage.py make_admin user@example.com
```

#### 🔐 Promote and set a new password:

```bash
python manage.py make_admin user@example.com --password newsecurepassword123
```

### 💡 Notes:

* If the user does **not exist**, a message will be shown.
* This must be run from the project root with the virtual environment activated.

---