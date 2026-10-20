from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import heal_targets
from spirit.game.session.passives import effective_max_hp


def _damaged_bench(board, player_id, stadium=None):
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in bench.children)


POKEMON_CENTER_ABILITY = Ability(
    title="Pok\u00e9mon Center",
    game_text="Once during each player's turn, that player may heal 20 damage from 1 of his or her Benched Pok\u00e9mon.",
    activation=Activations.ONCE_PER_TURN,
    condition=_damaged_bench,
    effect=heal_targets(20, scope="bench_choice"),
)


card = StadiumCardDef(
    guid="2e6782c8-309d-59f9-b567-fae0359eac7a",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    ability=POKEMON_CENTER_ABILITY
)
