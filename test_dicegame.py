import unittest
from main import Die, DiceGame

class TestDiceGame(unittest.TestCase):

    def test_die_roll_bounds(self):
        die = Die()
        for _ in range(100):
            roll = die.roll()
            self.assertTrue(1 <= roll <= 6)
        
    def test_evalulate_win(self):
        game = DiceGame()   
        self.assertEqual(game.evalulate.roll(7), "Win")
        self.assertEqual(game.evalulate.roll(11), "Win")

    def test_evalulate_lose(self):
        game = DiceGame()   
        self.assertEqual(game.evalulate.roll(2), "lose")
        self.assertEqual(game.evalulate.roll(3), "lose")
        self.assertEqual(game.evalulate.roll(12), "lose")

    def test_evalulate_roll_again(self):
        game = DiceGame()
        for total in (4, 5, 6, 8, 9, 10):
            self.assertEqual(game.evalulate.roll(total), "Roll Again")

    def test_play_round_structure(self):
        game = DiceGame()
        result = game.play_round()
        self.assertIn("die1", result)
        self.assertIn("die2", result)
        self.assertIn("total", result)
        self.assertIn("result", result)

    def test_die_custom_sides(self):
        die = Die(sides=10)
        for _ in range(100):
            roll = die.roll()
            self.assertTrue(1 <= roll <= 10)
    
    def test_total_sum_validity(self):
        game = DiceGame()
        result = game.play_round()
        total = result["total"]
        self.assertEqual(total, result["die1"] + result["die2"])

    def test_result_consistency(self):
        game = DiceGame()
        for total in range(2, 13):
            result = game.evalulate_roll(total)
            self.assertIn(result, ["Win", "Lose", "Roll Again"])
    
    
if __name__ == "__main__":   
    unittest.main()