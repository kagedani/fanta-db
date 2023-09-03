from src.data.PlayersStats import PlayersStats


def from_download_to_players_stats(sql_records, season):
    players_stats_list = []
    for record in sql_records:
        ps = PlayersStats(id=record.get("Id"),
                          season=season,
                          role=record.get("R"),
                          mantra_role=record.get("Rm"),
                          name=record.get("Nome"),
                          team=record.get("Squadra"),
                          number_of_game_with_vote=record.get("Pv"),
                          average_vote=record.get("Mv"),
                          average_fanta_vote= record.get("Mf") if season <= "2122" else record.get("Fm"),
                          goal_made=record.get("Gf"),
                          goal_taken=record.get("Gs"),
                          penalty_saved=record.get("Rp"),
                          penalty_kicked=record.get("Rc"),
                          penalty_made=record.get("R+"),
                          penalty_missed=record.get("R-"),
                          assist=record.get("Ass"),
                          yellow_card=record.get("Amm"),
                          red_card=record.get("Esp"),
                          autogol=record.get("Au"))
        players_stats_list.append(ps)
    return players_stats_list
