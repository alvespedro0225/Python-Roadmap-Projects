from imports.APIHandler import APIHandler


if __name__ == "__main__":
    username = input("Username: ")
    APIHandler.get_info(username)
