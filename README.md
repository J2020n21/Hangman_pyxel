# Hangman_pyxel
Basic hangman game using python pyxel module 
License: MIT

##playing video:
[Youtube](https://youtu.be/toaOOZVWynA)

게임을 처음 시행하면 다음과 같습니다.
This is the first screen you execute the game.
![firstScene](https://github.com/J2020n21/Hangman_pyxel/blob/main/Screenshots/screenshot_playing1.jpg){: width="300" height="300"}


좌측상단에는 남은 목숨이, 중앙에는 점수가, 우측 상단에는 사운드 on/off상태를 표시합니다.
사운드는 켜진상태로 시작하며, shift로 끄기, on으로 켤 수 있습니다. 틀리거나 맞출때 효과음을 들을 수 있습니다.

Upper left shows how many lives have left, middle shows score, and upper right shows the current status of sound(ON/OFF).
Sound is basically "ON", but you can turn it off with 'SHIFT' and on with 'SPACE BAR'.
The sound effect will play each time user make guess.

![soundOff](https://github.com/J2020n21/Hangman_pyxel/blob/main/Screenshots/screenshot_sound_off.png)
![soundOn](https://github.com/J2020n21/Hangman_pyxel/blob/main/Screenshots/screenshot_sound_on.jpg)



하단에는 해당 단어의 주제가 표시됩니다. [과일/동물/사물/국가/스포츠]

Underneath the graphic, there is the subject of the word. [fruit/animal/thing/nation/sport]


언더바를 표시해 글자수를 나타내고, 키 입력을 통해 맞추면 해당 언더바 위에, 틀리면 하단 공간에 빨간색으로 표기됩니다. 

Under bar represents the total letters. If the user guessed through keyboard input, the letter will be written on the exact location of the underbar(s) if it is correct, or under the blank space in red if it is wrong.
 
 
틀릴때마다 목숨이 1씩 줄어들며 한 단어를 맞추면 목숨이 +3 증가합니다.

Wrong guess makes life minus one, and if guessed a full word add plus three lives.


사망시 화면은 다음과 같으며, 'R'을 누르면 재시작, ESC를 누르면 게임을 종료할 수 있습니다.

Game over is when the lives ran out. 'R' for restart, 'ESC' for exit the game.
![gameOver](https://github.com/J2020n21/Hangman_pyxel/blob/main/Screenshots/screenshot_gameover.png)


점수가 일정 점수이상 다다르면 게임 클리어!

If the user gets certain amount of scores, game clear.
Figure out how far you can go.



##Reference
*https://github.com/kitao/pyxel [Official document]
*https://www.youtube.com/watch?v=Qg16VhEo2Qs [Pyxel tutorial: making snake game]
*https://github.com/gediminasz/games/blob/master/typo/scenes/game.py [The code of snake game that written by lecturer below]
*https://nadocoding.tistory.com/11 [About Logic]
