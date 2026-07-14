from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


def _cavern_tackle_condition(board, player_id, pokemon):
    for p in board.pokemon_in_play(player_id):
        for used_id, _archetype, used_title in board.turn_state.attacks_used_last_turn:
            if used_id == p.entity_id and used_title == "Cavern Tackle":
                return False
    return True


card = PokemonCardDef(
    guid="b92d18c5-1b20-534e-95fc-738e6bfc4b8e",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terrakion.Name",
    display_name="Terrakion",
    searchable_by=["Terrakion", "Basic", "Terrakion"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=639,
    abilities=[
        Attack(
            title="Cavern Tackle",
            game_text="During your opponent's next turn, prevent all damage from attacks done to this Pok\u00e9mon. If 1 of your Pok\u00e9mon used Cavern Tackle during your last turn, this attack can't be used.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            condition=_cavern_tackle_condition,
            effect=protect_next_turn(prevent=True),
        ),
    ],
)