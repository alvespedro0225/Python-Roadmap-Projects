from imports.APIHandler import APIHandler


if __name__ == "__main__":
    username: str = input("Username: ")
    APIHandler.get_info(username)
