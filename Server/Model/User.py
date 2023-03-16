import uuid


class Users:

    """
    Esta clase se encarga de crear los usuarios, es un modelo
    """

    def __init__(self, user=None, password=None, email=None, id=None, name=None, courses=None):
        self.user = user
        self.password = password
        self.email = email
        self.id = id
        self.name = name
        self.courses = courses

    def set_user(self, user):

        """
        Setter de Usuario.
        :param user: Usuario a asignar.
        """

        self.user = user

    def set_password(self, password):

        """
        Setter de Contraseña.
        :param password: Contraseña a asignar.
        """

        self.password = password

    def set_email(self, email):

        """
        Setter de Email
        :param email: Email a asignar
        """

        self.email = email

    def set_id(self, id):

        """
        Setter de ID
        :param id: ID a asignar.
        """

        self.id = id

    def set_name(self, name):

        """
        Setter de Nombre
        :param name: Nombre a asignar.
        """

        self.name = name

    def set_courses(self, courses):

        """
        Setter de Cursos
        :param courses: Curso a asignar
        """

        self.courses = courses

    def dict_from_class(self):

        """
        Crea diccionario en base a los atributos de clase.
        :return: Retorna el diccionario creado.
        """

        return {
            "User": self.user,
            "Password": self.password,
            "Email": self.email,
            "ID": self.id,
            "Name": self.name,
            "Courses": self.courses,
        }


