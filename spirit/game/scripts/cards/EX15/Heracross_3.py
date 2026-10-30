"""STUB: effect not implemented — do not guess mechanics.
Heracross δ (EX15 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import dig_deep_energy_to_hand, extra_ball_vs_ex, shining_horn_solo_passive


card = PokemonCardDef(
    guid="c12a22c6-da4c-5f2a-8e2e-761b0dbc1ef0",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross δ",
    searchable_by=["Heracross \u03b4", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Ability(
            title="Shining Horn",
            game_text="As long as Heracross is the only Pok\u00e9mon you have in play, your opponent's Basic Pok\u00e9mon can't attack.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=shining_horn_solo_passive(),
        ),
        Attack(
            title="Dig Deep",
            game_text="Search your discard pile for an Energy card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dig_deep_energy_to_hand(),
        ),
        Attack(
            title="Extra Claws",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=extra_ball_vs_ex(30, 20),
        ),
    ],
)