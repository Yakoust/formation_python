class WrongLoginException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Le login ne doit posséder que des lettres minuscules", *args)

class WrongPasswordException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Le mot de passe ne doit posséder que des nombres", *args)

def input_login():
     try:
         login = str(input("Saisir entrer un login SVP (celui-ci ne doit contenir que des lettres minuscules: "))
         if not login.islower() or not login.isalpha():
             raise WrongLoginException()
     except WrongLoginException as wle:
         print(wle)
         return -1
     except ValueError as ve:
         print(ve)
         print("Saisie invalide !")
         return -1
     else:
         try:
             password = str(input("Saisir entrer votre mot de passe SVP (celui-ci ne doit contenir que des chiffres: "))
             if not password.isdigit():
                 raise WrongPasswordException()
         except WrongPasswordException as wpe:
             print(wpe)
             return -1

if __name__ == '__main__':
    login = -1
    while login == -1:
        login = input_login()
