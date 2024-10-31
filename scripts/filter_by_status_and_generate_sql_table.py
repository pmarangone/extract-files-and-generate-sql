#!/usr/bin/env python3

from zipfile import ZipFile
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite://", echo=False)


def unpack(file, final_location):
    with ZipFile(file, "r") as zObject:
        zObject.extractall(path=final_location)


def read_file(origem_dados, tipos):
    table = pd.read_csv(origem_dados)
    tipos = pd.read_csv(tipos)

    table_critico = table.loc[table["status"] == "CRITICO"]

    table_sorted = table_critico.sort_values(by=["created_at"])

    table_sorted = table_sorted.merge(tipos, left_on="tipo", right_on="id", how="left")

    table_sorted.rename(columns={"nome": "nome_tipo"}, inplace=True)

    table_sorted.drop(columns=["id"], inplace=True)

    return table_sorted


def from_df_to_sql():
    df = read_file("../dados/origem-dados.csv", "../dados/tipos.csv")
    df.to_sql(name="dados_finais", con=engine)

    with open("insert-dados.sql", "w") as file:
        with engine.connect() as conn:
            for line in conn.connection.iterdump():
                file.write(f"{line}\n")


def items_agrupados_por_dia_e_tipo():
    query = """
            SELECT 
                DATE(created_at) AS dia,
                tipo,
                COUNT(*) AS quantidade
            FROM 
                dados_finais
            GROUP BY 
                dia, tipo
            ORDER BY 
                dia, tipo;
        """

    # Won't be used in the first time the script will run
    # init_db()

    with engine.connect() as connection:
        result = connection.execute(text(query))

        result = result.fetchall()

        return result


# Helper function to load data from insert-dados.sql
def init_db():
    with open("insert-dados.sql", "r") as file:
        sql_statements = file.read()

    with engine.connect() as connection:
        for statement in sql_statements.split(";"):
            if statement.strip():
                connection.execute(text(statement))
        connection.commit()


if __name__ == "__main__":
    unpack("./dados.zip", "../dados/")

    read_file("../dados/origem-dados.csv", "../dados/tipos.csv")

    from_df_to_sql()

    result = items_agrupados_por_dia_e_tipo()

    print(result)
