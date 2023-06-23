import pyodbc

# tratar credenciais
def return_cursor() -> pyodbc.Cursor | Exception:

    for driver in pyodbc.drivers():
        if ('MySQL' in driver and 'ANSI' in driver):
            try:
                return pyodbc.connect(f"DRIVER={driver}; SERVER=localhost;DATABASE=estoque; UID=fabricio.serrano; PASSWORD=FSerran0.;", autocommit=True).cursor()

            except (ConnectionError, pyodbc.Error) as exception:
                return exception
