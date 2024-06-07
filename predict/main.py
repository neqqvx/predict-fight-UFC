from flask import Flask, render_template
from flask import request
app = Flask(__name__)




@app.route('/fight14', methods=['GET', 'POST'])
def fight14():
    if request.method == 'POST':
        

#вин стрик
        pantoja_winss = 29
        erceg_winss = 7



#луз
        pantoja_lose = 6
        erceg_lose = 1


#счет
        pantoja_wins = 35 + 29 + 6
        erceg_wins = 9 + 7 + 1


#общий
        total_fights = pantoja_wins + erceg_wins

        pantoja_chance = (pantoja_wins / total_fights) * 100
        erceg_chance = (erceg_wins / total_fights) * 100

        return render_template('fight14.html', pantoja_wins=pantoja_wins, erceg_wins=erceg_wins, pantoja_chance=pantoja_chance, erceg_chance=erceg_chance, pantoja_winss=pantoja_winss, erceg_winss=erceg_winss, pantoja_lose=pantoja_lose, erceg_lose=erceg_lose)

    return render_template('fight14.html')















@app.route('/fight13', methods=['GET', 'POST'])
def fight13():
    if request.method == 'POST':
        
        zhoze_winss = 31
        martinz_winss = 18



        zhoze_wins = 39 + 31 + 8
        martinz_wins = 22 + 18 + 4

      
      
        zhoze_lose = 8
        martinz_lose = 4


        total_fights = zhoze_wins + martinz_wins

        zhoze_chance = (zhoze_wins / total_fights) * 100
        martinz_chance = (martinz_wins / total_fights) * 100

        return render_template('fight13.html', zhoze_wins=zhoze_wins, martinz_wins=martinz_wins, zhoze_chance=zhoze_chance, martinz_chance=martinz_chance, zhoze_lose=zhoze_lose, martinz_lose=martinz_lose, zhoze_winss=zhoze_winss, martinz_winss=martinz_winss)

    return render_template('fight13.html')






@app.route('/fight12', methods=['GET', 'POST'])
def fight12():
    if request.method == 'POST':
        
        antony_winss = 36
        vitor_winss = 14

        antony_lose = 19
        vitor_lose = 0

        antony_wins = 55 - 19
        vitor_wins = 14 + 14 - 0

      
      
        


        total_fights = antony_wins + vitor_wins

        antony_chance = (antony_wins / total_fights) * 100
        vitor_chance = (vitor_wins / total_fights) * 100

        return render_template('fight12.html', antony_wins=antony_wins, vitor_wins=vitor_wins, antony_chance=antony_chance, vitor_chance=vitor_chance, antony_lose=antony_lose, vitor_lose=vitor_lose, antony_winss=antony_winss, vitor_winss=vitor_winss)

    return render_template('fight12.html')










@app.route('/fight10', methods=['GET', 'POST'])
def fight10():
    if request.method == 'POST':
        
        paul_winss = 17
        caio_winss = 15

        paul_lose = 7
        caio_lose = 1

        paul_wins = 25 + 17 - 1
        caio_wins = 17 + 15 - 1

      
      
        


        total_fights = paul_wins + caio_wins

        paul_chance = (paul_wins / total_fights) * 100
        caio_chance = (caio_wins / total_fights) * 100

        return render_template('fight10.html', paul_wins=paul_wins, caio_wins=caio_wins, paul_chance=paul_chance, caio_chance=caio_chance, paul_lose=paul_lose, caio_lose=caio_lose, paul_winss=paul_winss, caio_winss=caio_winss)

    return render_template('fight10.html')












@app.route('/ufc', methods=['GET', 'POST'])
def ufc():
    return render_template('ufc.html')











# Главная страница с информацией о бойцах и предиктами
@app.route('/')
def index():
    return render_template('index.html')





@app.route('/about')
def about():
  return render_template('about.html')



@app.route('/aboute')
def aboute():
  return render_template('aboute.html')


@app.route('/aboutes')
def aboutes():
  return render_template('aboutes.html')





if __name__ == '__main__':
    app.run(debug=True)
