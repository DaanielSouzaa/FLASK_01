from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    listaProdutos = {1: ['Maça', '6,00', 'kg',
                         'https://conteudo.imguol.com.br/c/entretenimento/32/2018/01/18/maca-1516308281068_v2_450x337.jpg'],
                     2: ['Banana', '4,00', 'kg',
                         'https://www.ibahia.com/fileadmin/user_upload/ibahia/2019/outubro/25/banana.jpg?width=1200&enable=upscale'],
                     3: ['Laranja', '12,00', 'kg',
                         'https://www.remedio-caseiro.com/wp-content/uploads/2014/02/20190923-laranjas.jpg'],
                     4: ['Manga', '15,00', 'kg',
                         'https://www.hypeness.com.br/1/2021/03/f9aad0a8-edit_manga_sau%CC%81de_gettyimages-1162661505.jpg'],
                     5: ['Morango', '35,00', 'kg',
                         'https://www.aen.pr.gov.br/modules/galeria/uploads/65329/news_interna_morango_porto_amazonas20120610_0030.jpg'],
                     6: ['Uva', '17,00', 'kg',
                         'https://www.infoescola.com/wp-content/uploads/2010/04/uvas_665365768.jpg'],
                     }


    return render_template('index.html', listaProdutos=listaProdutos)


if __name__ == '__main__':
    app.run()
