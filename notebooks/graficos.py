import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("data/base_cancelamentos.csv")


def grafico_cancelamentos():
    fig, ax = plt.subplots(figsize=(8, 5))
    tabela["cancelou"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Cancelamentos Geral")
    return fig


def grafico_duracao():
    fig, ax = plt.subplots()
    tabela.groupby("duracao_contrato")["cancelou"].value_counts().unstack().plot(kind="bar", ax=ax)
    ax.set_title("Cancelamentos por Duração do Contrato")
    return fig


def grafico_idade():
    fig, ax = plt.subplots()
    tabela.groupby("idade")["cancelou"].value_counts().unstack().plot(kind="line", ax=ax)
    ax.set_title("Cancelamentos por Idade")
    return fig


def grafico_assinatura():
    fig, ax = plt.subplots()
    tabela.groupby("assinatura")["cancelou"].value_counts().unstack().plot(kind="bar", ax=ax)
    ax.set_title("Cancelamentos por tipo de Assinatura")
    return fig


def grafico_sexo():
    fig, ax = plt.subplots()
    tabela.groupby("sexo")["cancelou"].value_counts().unstack().plot(kind="bar", ax=ax)
    ax.set_title("Cancelamentos por Sexo")
    return fig


def grafico_callcenter():
    fig, ax = plt.subplots()
    tabela.groupby("ligacoes_callcenter")["cancelou"].value_counts().unstack().plot(kind="bar", ax=ax)
    ax.set_title("Cancelamentos vs n° ligações no Call Center")
    return fig