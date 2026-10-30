"""STUB: effect not implemented — do not guess mechanics.
Spinda (EX5 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import flail_damage, hula_la

card = PokemonCardDef(
    guid="c4c7518f-55f2-52a6-ae4b-a784afab4bd0",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=["Spinda", "Basic", "Spinda"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Attack(
            title="The Hula-la",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused. If tails, both the Defending Pok\u00e9mon and Spinda are now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=hula_la(),
        ),
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Spinda.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flail_damage(10),
        ),
    ],
)