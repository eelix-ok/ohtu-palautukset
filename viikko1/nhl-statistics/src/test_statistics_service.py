import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  # 4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),  # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89),  # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_palauttaa_pelaajan_kun_nimi_loytyy(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")

    def test_search_palauttaa_none_kun_nimea_ei_loydy(self):
        player = self.stats.search("Selanne")

        self.assertIsNone(player)

    def test_team_palauttaa_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")

        names = [player.name for player in players]
        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_palauttaa_tyhjan_listan_kun_joukkuetta_ei_ole(self):
        players = self.stats.team("TOR")

        self.assertEqual(players, [])

    def test_top_palauttaa_pyydetyn_maaran_pelaajia(self):
        players = self.stats.top(3)

        self.assertEqual(len(players), 3)

    def test_top_palauttaa_pelaajat_pistejarjestyksessa(self):
        players = self.stats.top(3)

        names = [player.name for player in players]
        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])
