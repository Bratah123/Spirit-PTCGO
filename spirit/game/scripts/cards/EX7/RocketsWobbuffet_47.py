"""STUB: effect not implemented — do not guess mechanics.
Rocket's Wobbuffet (EX7 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import amnesia, dark_aid


card = PokemonCardDef(
    guid="2aa3a067-2984-56bf-b4df-62e66c630e92",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsWobbuffet.Name",
    display_name="Rocket's Wobbuffet",
    searchable_by=["Rocket's Wobbuffet", "Basic", "RocketsWobbuffet"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Attack(
            title="Dark Aid",
            game_text="Search your discard pile for Pok\u00e9mon Tool cards and Rocket's Secret Machine cards. You may show either 1 Pok\u00e9mon Tool card or Rocket's Secret Machine card to your opponent and put it into your hand, or show a combination of 3 Pok\u00e9mon Tool cards or Rocket's Secret Machine cards to your opponent and shuffle them into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dark_aid(),
        ),
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=amnesia,
        ),
    ],
)