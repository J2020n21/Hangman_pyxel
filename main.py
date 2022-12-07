import pyxel
import words
import line
import time

WORD = words.pick_word()
WORD_SUBJECT = words.get_subject()
LIFE=6
SCORE=0
WRONG_ALPHA = []   #wrong guess
GUESSING_STR = ""  #user input letters
DEATH = False
KEYIN = ""          #key input
WORD_COMPLETION = False
TIME = time.time()
GAME_CLEAR = False
END_SCORE = 20     #game clear measure
PLAY_EFFECT=True

class Character:
    def __init__(self):
        self.Cx = 70 #character position
        self.Cy = 50
        self.Exe_x = 100
        self.width = 16
        self.height = 16

    def draw(self):
        global LIFE,SCORE
        pyxel.blt(self.Exe_x, self.Cy, 0, 16, 55, self.width, self.height + 1)
        pyxel.blt(self.Cx, self.Cy, 0, 0, 56, self.width-3, self.height)
        if LIFE >= 5: #get close
            self.Cx = 90
            self.Exe_x = 100
        elif LIFE == 4: #tied up
            pyxel.blt(self.Cx, self.Cy, 0, 32, 55, self.width, self.height +1)
            self.Exe_x = 500
        elif LIFE == 3:
            pyxel.blt(self.Cx, self.Cy, 0, 0, 79, self.width, self.height + 1)
        elif LIFE == 2:
            pyxel.blt(self.Cx, self.Cy, 0, 16, 79, self.width, self.height + 1)
        elif LIFE == 1: #unconscious
            pyxel.blt(self.Cx, self.Cy, 0, 0, 103, self.width, self.height + 1)
        if SCORE >= END_SCORE - 3:
            self.Exe_x = 500
            pyxel.blt(self.Cx, self.Cy, 0, 32, 104, self.width, self.height)

class Graphics: #기타 이미지 그리기+ 주인공->목숨에따라 그림이 바뀜
    def __init__(self): #tilemap
        self.soilder_x = 40
        self.soilder_y = 50
        self.floor_x = 70
        self.floor_y = 70
        self.cloud_x = 20
        self.cloud_y = 25
        self.cloud_x_end =210
        self.l_crowd_x = 0
        self.r_crowd_x = 150
        self.crowd_y = 130
        self.width = 8
        self.height = 8
#관중 16px기준 좌:32,0 혹은 32,16 / 우향우: 48,0
    def draw(self): #바닥, 구름, 병사
        pyxel.blt(self.soilder_x,self.soilder_y, 0, 0, 40, 16, 16)
        pyxel.blt(self.soilder_x -32, self.soilder_y, 0, 0, 40, 16, 16)
        pyxel.blt(self.soilder_x -64, self.soilder_y, 0, 0, 40, 16, 16)
        pyxel.blt(self.soilder_x +90, self.soilder_y, 0, 0, 40, 16, 16)
        pyxel.blt(self.soilder_x + 122, self.soilder_y, 0, 0, 40, 16, 16)
        pyxel.blt(self.soilder_x + 150, self.soilder_y, 0, 0, 40, 16, 16)
        #pyxel.blt(self.floor_x, self.floor_y, 0, 0, 32, self.width, self.height)
        pyxel.blt(self.cloud_x, self.cloud_y, 0, 24, 24, self.width, self.height)
        pyxel.blt(self.cloud_x +50, self.cloud_y -10, 0, 24, 24, self.width, self.height)
        pyxel.blt(self.cloud_x + 120, self.cloud_y +5, 0, 24, 24, self.width, self.height)
    def update_graphic(self):
        self.cloud_x = (self.cloud_x + 0.1)
        if self.cloud_x == self.cloud_x_end:
            self.cloud_x = -120
class Sound: #Shift:off / space: on
    def __init__(self):
        self.x = 180
        self.y = 10
        self.width = 8
        self.height = 8

    def draw(self): #draw: display element on the screen
        if PLAY_EFFECT:
            pyxel.blt(self.x, self.y, 0, 0, 16, self.width, self.height)
        else:
            pyxel.blt(self.x, self.y, 0, 8, 16, self.width, self.height)
    def off(self):
        pass
class Life:
    def __init__(self):
        self.x =0
        self.y =0
        self.x2 = 15
        self.x3 = 30
        self.width = 16
        self.height = 16

    def draw(self): #draw image
        pyxel.text(0,0,f"Life:{LIFE}",pyxel.COLOR_WHITE)

class Score:
    def draw(self):
        global SCORE
        pyxel.text(80, 10, f"score: {SCORE}", pyxel.COLOR_RED)
class Word:
    def pick_new_word(self): #새로운 단어 할당
        global WORD,WORD_SUBJECT
        WORD = words.pick_word()
        WORD_SUBJECT = words.get_subject()
        return WORD

    def draw(self):
        pyxel.text(90,110,f"{WORD}",pyxel.COLOR_WHITE)

    def draw_subject(self): #word의 subject를 쓰는 용도
        global WORD_SUBJECT
        pyxel.text(70, 100, f"SUBJECT:{WORD_SUBJECT}", pyxel.COLOR_WHITE)


class Guessing:
    def __init__(self):
        self.x =70
        self.y = 120
        self.width= 8 #underbar width
        self.WA_width = 10 #WrongAlpha width
        self.draw_alpha_new = ''
    def draw_underBar(self):
        global WORD
        self.underbars = len(WORD)
        for i in range(self.underbars):
            pyxel.text(self.x + (self.width * i ) ,self.y,"_",pyxel.COLOR_YELLOW)

    def check_complete(self): # decide to move to next word or not.
        global GUESSING_STR,SCORE,WORD,WRONG_ALPHA,WORD_COMPLETION,LIFE
        if len(GUESSING_STR) == len(set(WORD)):
            SCORE += 1
            GUESSING_STR = ""
            WRONG_ALPHA = []
            LIFE += 3
            WORD_COMPLETION=True #ready to get a new word


    def draw_alpha(self):#write correct guess
        global GUESSING_STR,WORD,KEYIN
        for i, val in enumerate(WORD):
            if val in GUESSING_STR:
                pyxel.text(self.x + (self.width * i), 115, f"{val}", pyxel.COLOR_GREEN)
            else: # &nbsp
                pyxel.text(self.x + (self.width * i), 115, f" ", pyxel.COLOR_GREEN)
    def update_judge(self):#입력을 받아 추가한다
        global WORD, GUESSING_STR,KEYIN, WRONG_ALPHA,LIFE
        if KEYIN in WORD and KEYIN not in set(GUESSING_STR): #중복방지
            GUESSING_STR += KEYIN.lower()#right guess
            if PLAY_EFFECT:
                pyxel.play(0,1)
        else:
            WRONG_ALPHA += KEYIN.lower()#wrong guess
            LIFE -= 1
            if PLAY_EFFECT:
                pyxel.play(0,0)

    def draw_wrong_alpha(self):
        global WRONG_ALPHA
        for i,val in enumerate(WRONG_ALPHA):
            pyxel.text(30 + (self.WA_width*i ),140,f"{val}",pyxel.COLOR_RED)


    def input_character(self):
        global KEYIN
        for character, key in self.key_dict().items():
            if pyxel.btnp(key):
                KEYIN = character.lower()
                return character
    def key_dict(self):
        return {
            'a': pyxel.KEY_A,
            'b': pyxel.KEY_B,
            'c': pyxel.KEY_C,
            'd': pyxel.KEY_D,
            'e': pyxel.KEY_E,
            'f': pyxel.KEY_F,
            'g': pyxel.KEY_G,
            'h': pyxel.KEY_H,
            'i': pyxel.KEY_I,
            'j': pyxel.KEY_J,
            'k': pyxel.KEY_K,
            'l': pyxel.KEY_L,
            'm': pyxel.KEY_M,
            'n': pyxel.KEY_N,
            'o': pyxel.KEY_O,
            'p': pyxel.KEY_P,
            'q': pyxel.KEY_Q,
            'r': pyxel.KEY_R,
            's': pyxel.KEY_S,
            't': pyxel.KEY_T,
            'u': pyxel.KEY_U,
            'v': pyxel.KEY_V,
            'w': pyxel.KEY_W,
            'x': pyxel.KEY_X,
            'y': pyxel.KEY_Y,
            'z': pyxel.KEY_Z,
        }


class Game:
    def __init__(self):
        ###Game setting
        self.screen_width = 200
        self.screen_height = 160
        pyxel.init(self.screen_width, self.screen_height,title="Hang man", fps=30)
        pyxel.mouse(False)

        #######Load file & Instance
        pyxel.load("file.pyxres")
        self.life = Life()
        self.sound = Sound()
        self.graphic = Graphics()
        self.character = Character()
        self.scr = Score()
        self.word = Word()
        self.guess = Guessing()
        self.end_line = line.Lines() #print comment at the end
        ###Run the game
        pyxel.run(self.update, self.draw)

    def update(self):#update the logic of game.
        #update the guessing for scoring/win condition
        global WORD_COMPLETION,SCORE,PLAY_EFFECT
        if not DEATH:
            self.graphic.update_graphic()
            if self.guess.input_character():
                self.guess.update_judge()
                self.check_death()
                self.check_end()
                self.guess.check_complete()
                if WORD_COMPLETION:
                    self.word.pick_new_word()
                    WORD_COMPLETION= False
                if GAME_CLEAR:
                    self.end_screen()
        else:
            self.death_screen()

        if pyxel.btn(pyxel.KEY_SHIFT): #sound off-shift
            PLAY_EFFECT = False
        if pyxel.btn(pyxel.KEY_SPACE): #sound on-space
            PLAY_EFFECT = True

        if pyxel.btn(pyxel.KEY_ESCAPE): #ESC - exit
            pyxel.quit()

    def draw(self): #draw things
        if not DEATH:
            pyxel.cls(0)
            self.life.draw()
            self.sound.draw()
            self.graphic.draw()
            self.character.draw()
            #self.word.draw() #for debuging, print answer
            self.word.draw_subject()
            self.scr.draw()
            self.guess.draw_underBar()
            self.guess.draw_alpha()
            self.guess.draw_wrong_alpha()
            if GAME_CLEAR:
                self.draw_end_screen()
        else:
            self.draw_death()

    def reset_all(self): #reset initial value
        global SCORE, LIFE, WRONG_ALPHA, GUESSING_STR, DEATH,WORD,WORD_SUBJECT
        WORD = words.pick_word()
        WORD_SUBJECT = words.get_subject()
        SCORE=0
        LIFE=6
        WRONG_ALPHA=[]
        GUESSING_STR=""
        DEATH = False

    def reset_str(self): #after get a score, move to next word
        global WRONG_ALPHA, GUESSING_STR
        WRONG_ALPHA = []
        GUESSING_STR=""

    def check_death(self):
        global LIFE, DEATH
        if LIFE <= 0:
            DEATH = True
            self.death_screen()   # stop game,goto end page

    def death_screen(self):
        self.death = True
        pyxel.stop()

    def draw_death(self):
        global SCORE, DEATH
    #Draw a black screen and notice text.
        pyxel.cls(0)
        pyxel.text(10,50,"GameOver",col=pyxel.COLOR_WHITE)
        pyxel.text(10, 80, f"Score:{SCORE}", col=pyxel.COLOR_WHITE)
        pyxel.text(10, 100, f"The answer was '{WORD}'", col=pyxel.COLOR_WHITE)
        pyxel.text(10, 120, self.end_line.score_evaluation_line(score=SCORE), col=pyxel.COLOR_WHITE)
        pyxel.text(10,140,"[R]estart or [ESC] to quit",pyxel.COLOR_WHITE)
        if pyxel.btn(pyxel.KEY_R):
            self.reset_all()
            DEATH = False

    def check_end(self): #is score is engouh?
        global SCORE,GAME_CLEAR,END_SCORE
        if SCORE >= END_SCORE:
            GAME_CLEAR=True
    def end_screen(self):
        pyxel.stop()
    def draw_end_screen(self):
        pyxel.cls(4)
        pyxel.text(10,50,"Thank you!",col=pyxel.COLOR_WHITE)
        pyxel.text(10, 80, f"You reached score {SCORE}", col=pyxel.COLOR_WHITE)
        pyxel.text(10, 100, "Thank you for playing!", col=pyxel.COLOR_WHITE)

Game()
