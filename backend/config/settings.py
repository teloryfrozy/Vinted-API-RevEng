"""
All secrets will be loaded from environment variables
"""

DEBUG_MODE = True
ALLOW_ORIGINS = ["http://localhost:5173"]


# DB might change, I just use sqlite for now
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
