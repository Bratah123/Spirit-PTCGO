from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents


def _dedenne_dede_short_condition(board, player_id, pokemon):
    for p in board.pokemon_in_play(player_id):
        card_def = def_for(p.archetype_id)
        if card_def and card_def.display_name == "Dedenne":
            for used_id, _archetype, used_title in board.turn_state.attacks_used_last_turn:
                if used_id == p.entity_id and used_title == "Dede-Short":
                    return True
    return False


card = PokemonCardDef(
    guid="4dc26794-4408-51fb-85c0-79e1105be434",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic", "Morpeko"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Peko Blaster",
            game_text="You can use this attack only if 1 of your Dedenne used Dede-Short during your last turn. This attack does 60 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            condition=_dedenne_dede_short_condition,
            effect=damage_all_opponents(60),
        ),
    ],
)
