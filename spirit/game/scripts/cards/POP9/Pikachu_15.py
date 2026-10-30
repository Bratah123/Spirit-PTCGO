"""Pikachu (POP9 #15)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import charm_reduce_defender_next, numb_if_evolved


card = PokemonCardDef(
    guid="7ae03ddb-26f0-54be-90ef-c7f585013e88",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="POP9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=charm_reduce_defender_next(20)
        ),
        Attack(
            title="Numb",
            game_text="If Pikachu evolved from Pichu during this turn, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=numb_if_evolved(SpecialConditions.PARALYZED)
        ),
    ]
)