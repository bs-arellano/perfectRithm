var config = {
    type: Phaser.AUTO,
    parent: 'game_canvas',
    width: 800,
    height: 600,
    backgroundColor: '#303030',
    scene: {
        preload: preload,
        create: create,
        update: update,
    }
};

var game = new Phaser.Game(config);

function preload() {
    this.sound.pauseOnBlur = false;
    this.load.image('board', '../static/src/img/background.png');
    this.load.image('up', '../static/src/img/up.png');
    this.load.image('upNote', '../static/src/img/upNote.png');
    this.load.image('down', '../static/src/img/down.png');
    this.load.image('downNote', '../static/src/img/downNote.png');
    this.load.image('left', '../static/src/img/left.png');
    this.load.image('leftNote', '../static/src/img/leftNote.png');
    this.load.image('right', '../static/src/img/right.png');
    this.load.image('rightNote', '../static/src/img/rightNote.png');
    this.load.image('play', '../static/src/img/play.png');
    this.load.audio('song', '../static/' + song);
    this.load.audio('hit', '../static/src/audio/hit.mp3');
    this.load.json('notas', '../static/' + notes);
}

var back;
var music;
var notas;
var jugar_btn;
var score = 0;
var acc = 100;
//UP
var up_key;
var up_img;
//DOWN
var down_key;
var down_img;
//LEFT
var left_key;
var left_img;
//RIGHT
var right_key;
var right_img;

var pause_key;
var playing;

var contexto

function create() {
    contexto = this
    //Background
    back = this.add.image(400, 300, 'board').setScale(0.6, 0.6);
    back.visible = false;
    //Music
    music = this.sound.add('song');
    music.volume = 0.1;
    hit = this.sound.add('hit');
    //Play button
    jugar_btn = this.add.image(400, 300, 'play').setScale(0.5, 0.5);
    jugar_btn.setInteractive();
    jugar_btn.on('pointerdown', playLevel);
    //Controls
    //UP 400,40
    up_key = this.input.keyboard.addKey('W');
    up_img = this.add.image(400, 300, 'up').setScale(0.6, 0.6);
    up_img.visible = false;
    //DOWN 400,555
    down_key = this.input.keyboard.addKey('S');
    down_img = this.add.image(400, 300, 'down').setScale(0.6, 0.6);
    down_img.visible = false;
    //LEFT 140,300
    left_key = this.input.keyboard.addKey('A');
    left_img = this.add.image(400, 300, 'left').setScale(0.6, 0.6);
    left_img.visible = false;
    //RIGHT 660,300
    right_key = this.input.keyboard.addKey('D');
    right_img = this.add.image(400, 300, 'right').setScale(0.6, 0.6);
    right_img.visible = false;
    //PAUSE
    pause_key = this.input.keyboard.addKey('SPACE')
    notas = this.cache.json.get('notas');
}

var notasActivadas = []

function update() {
    if (playing) {
        if (notasActivadas.length > 0 & music.seek == 0) {
            stopGame()
        }
        //Display notes
        notas.Notes.forEach(nota => {
            if (nota[0] - (0.2) <= music.seek + 0.1 & music.seek - 0.1 <= nota[0] - (0.2) & notasActivadas.includes(nota) == false) {
                switch (nota[1]) {
                    case 'up':
                        console.log('up ' + music.seek)
                        moveUp(up_nt());
                        break;
                    case 'down':
                        console.log('down ' + music.seek)
                        moveDown(down_nt());
                        break;
                    case 'left':
                        console.log('left ' + music.seek)
                        moveLeft(left_nt());
                        break;
                    case 'right':
                        console.log('right ' + music.seek)
                        moveRight(right_nt());
                        break;
                }
                notasActivadas.push(nota);
            }
        });
        //UP
        if (Phaser.Input.Keyboard.JustDown(up_key)) {
            up_img.visible = true;
            hit.play();
            notasActivadas.forEach(nota => {
                if (nota[1] == 'up' & nota[0] < music.seek + 0.2 & nota[0] > music.seek - 0.2) {
                    score += 300
                }
            });
        }
        else if (Phaser.Input.Keyboard.JustUp(up_key)) {
            up_img.visible = false;
        }
        //DOWN
        else if (Phaser.Input.Keyboard.JustDown(down_key)) {
            down_img.visible = true;
            hit.play();
            notasActivadas.forEach(nota => {
                if (nota[1] == 'down' & nota[0] < music.seek + 0.2 & nota[0] > music.seek - 0.2) {
                    score += 300
                }
            });
        }
        else if (Phaser.Input.Keyboard.JustUp(down_key)) {
            down_img.visible = false;
        }
        //LEFT
        else if (Phaser.Input.Keyboard.JustDown(left_key)) {
            left_img.visible = true;
            hit.play();
            notasActivadas.forEach(nota => {
                if (nota[1] == 'left' & nota[0] < music.seek + 0.2 & nota[0] > music.seek - 0.2) {
                    score += 300
                }
            });
        }
        else if (Phaser.Input.Keyboard.JustUp(left_key)) {
            left_img.visible = false;
        }
        //RIGHT
        else if (Phaser.Input.Keyboard.JustDown(right_key)) {
            right_img.visible = true;
            hit.play();
            notasActivadas.forEach(nota => {
                if (nota[1] == 'right' & nota[0] < music.seek + 0.2 & nota[0] > music.seek - 0.2) {
                    score += 300
                }
            });
        }
        else if (Phaser.Input.Keyboard.JustUp(right_key)) {
            right_img.visible = false;
        }
    }
    //PAUSE
    if (Phaser.Input.Keyboard.JustDown(pause_key)) {
        if (playing) {
            music.pause();
            playing = false;
            console.log('pause');
        } else {
            music.resume();
            playing = true;
            console.log('resume');
        }
    }
    //UPDATE SCORE
    acc = 0
    if (notasActivadas.length > 1) {
        acc = (score / (notasActivadas.length) / 3).toFixed(2);
    }
    document.getElementById("score").innerHTML = "Puntuacion: " + score + " Presicion: " + acc + "%";
}

//START LEVEL
function playLevel() {
    jugar_btn.destroy();
    back.visible = true;
    playing = true;
    music.play();
    console.log('start');
}

var vel = 3

//Animate up note
function moveUp(img) {
    img.visible = true;
    setTimeout(function () {
        img.y -= vel
        if (img.y > -20) {
            moveUp(img)
        } else {
            img.destroy();
            console.log('up finish ' + music.seek)
            img.y = 300
        }
    }, 1)
}
//Animate down note
function moveDown(img) {
    img.visible = true;
    setTimeout(function () {
        img.y += vel
        if (img.y < 620) {
            moveDown(img)
        } else {
            img.destroy()
            console.log('down finish ' + music.seek)
            img.y = 300
        }
    }, 1)
}
//Animate left note
function moveLeft(img) {
    img.visible = true;
    setTimeout(function () {
        img.x -= vel
        if (img.x > -20) {
            moveLeft(img)
        } else {
            img.destroy();
            console.log('left finish ' + music.seek)
            img.x = 400
        }
    }, 1)
}

//Animate right note
function moveRight(img) {
    img.visible = true;
    setTimeout(function () {
        img.x += vel
        if (img.x < 720) {
            moveRight(img)
        } else {
            img.destroy();
            console.log('right finish ' + music.seek)
            img.x = 400
        }
    }, 1)
}

function up_nt() {
    return contexto.add.image(400, 300, 'upNote').setScale(0.8, 0.8);
}
function down_nt() {
    return contexto.add.image(400, 300, 'downNote').setScale(0.8, 0.8);
}
function left_nt() {
    return contexto.add.image(400, 300, 'leftNote').setScale(0.8, 0.8);
}
function right_nt() {
    return contexto.add.image(400, 300, 'rightNote').setScale(0.8, 0.8);
}

//GAME OVER
function stopGame(){
    game.destroy()
    window.location.replace("/newReg?song="+song_id+"&score="+score+"&acc="+acc);
}