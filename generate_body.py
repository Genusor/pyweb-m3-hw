# -*- coding: utf-8 -*-

from horoscope import generate_prophecies, times, advices, promises
from datetime import datetime as dt

def generate_page(head, body):
    return f"<html>{head}{body}</html>"

def generate_head(title):
	head = f"""<meta charset='utf-8'>
     <title>{title}</title>"""
	return f"<head>{head}</head>"


def generate_body_index(header, paragraphs):
    body = f"<h1>{header}</h1>"
    for p in paragraphs:
        body = body + f"<p>{p}</p>"
    body = body + "<hr><a href=\"about.html\">О реализации</a>"
    return f"<body>{body}</body>"

def generate_body_about(header, paragraphs):
    body = f"<h1>{header}</h1>"
    body+="<img src=\"zodiac.jpg\" height=100 wight=100 /><ol>"
    for item in paragraphs:
        body+=f"<li>{item}:<ul>"
        for v in paragraphs[item]:
            body+=f"<li>{v};</li>"
        body=body[:-6]+".</li>"
        body+="</ul>"
    body+="</ol><hr><a href=\"index.html\">На главную</a>"
    return f"<body>{body}</body>"

def save_page(title, header, paragraphs, output="index.html"):
    fp = open(output, "w", encoding="UTF8")
    today = dt.now().date()
    if output=="index.html":
        page = generate_page(
            head=generate_head(title),
            body=generate_body_index(header=header, paragraphs=paragraphs)
        )
    else:
        page = generate_page(
            head=generate_head(title),
            body=generate_body_about(header=header, paragraphs=paragraphs)
        )
    print(page, file=fp)
    fp.close()

today = dt.now().date()
save_page(
    title="Гороскоп на сегодня",
    header="Ваши предсказания на " + str(today),
    paragraphs=generate_prophecies(),
)

save_page(
    title="О реализации",
    header="О чем все это",
    paragraphs={"Времена дня":times,"Глаголы":advices,"Ожидания":promises},
    output="about.html",
)
