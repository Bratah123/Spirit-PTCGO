from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


def _togedemaru_toge_dash_condition(board, player_id, pokemon):
    for p in board.pokemon_in_play(player_id):
        card_def = def_for(p.archetype_id)
        if card_def and card_def.display_name == "Togedemaru":
            for used_id, _archetype, used_title in board.turn_state.attacks_used_last_turn:
                if used_id == p.entity_id and used_title == "Toge Dash":
                    return True
    return False

card = PokemonCardDef(
    guid="39aa098f-3cab-5aeb-a8e0-99750798b010",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Dede-Short",
            game_text="You can use this attack only if 1 of your Togedemaru used Toge Dash during your last turn. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            condition=_togedemaru_toge_dash_condition,
            effect=condition_attack(SpecialConditions.PARALYZED),
        ),
    ],
)