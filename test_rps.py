import rps

import subprocess
import sys


def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True


def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True


def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True


def test_lizard_is_invalid_play():
    assert rps.is_valid_play('lizard') is False


def test_computer_play_is_valid():
    for _ in range(5000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)

def test_computer_plays_randomly():
    plays = [rps.generate_computer_play()
             for _ in range(5000)]
    rocks = plays.count('rock')
    papers = plays.count('paper')
    scissors = plays.count('scissors')
    print(rocks, papers, scissors)
    assert rocks > 200
    assert papers > 200
    assert scissors > 200


def test_paper_beats_rock():
    result = rps.evaluate_game('paper', 'rock')
    assert result == 'human'


def input_faked_rock(prompt):
    print(prompt)
    return 'rock'


def test_full_game(capsys):
    rps.main(input=input_faked_rock)
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out



def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run([sys.executable, 'rps.py'],
                        encoding='utf-8',
                        stdout=subprocess.PIPE,
                        input='dragon\nrock\n',
                        check=True)
    assert cp.stdout.count('rock, paper, or scissors?') == 2











