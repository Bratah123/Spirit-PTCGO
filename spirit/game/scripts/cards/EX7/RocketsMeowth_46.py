from spirit.game.card_effects.ex import snatch_and_run, miraculous_comeback
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Meowth (EX7 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca8a7ef9-b765-5990-9b30-d8e28c6953e1",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsMeowth.Name",
    display_name="Rocket's Meowth",
    searchable_by=["Rocket's Meowth", "Basic", "RocketsMeowth"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Snatch and Run",
            game_text="Search your deck for a Pok\u00e9mon Tool card or Rocket's Secret Machine card, show it to your opponent, and put it into your hand. If you do, you may switch Rocket's Meowth with 1 of your Benched Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=snatch_and_run(),
        ),
        Attack(
            title="Miraculous Comeback",
            game_text="Flip a coin for each Pok\u00e9mon in play (both yours and your opponent's). This attack does 10 damage times the number of heads. Rocket's Meowth does 10 damage times the number of tails to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=miraculous_comeback(),
        ),
    ],
)