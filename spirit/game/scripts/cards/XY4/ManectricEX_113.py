"""STUB: effect not implemented — do not guess mechanics.
Manectric-EX (XY4 #113): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="20ce886f-a8cb-5ffa-ab0d-60a4c76541bc",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ManectricEX.Name",
    display_name="Manectric-EX",
    searchable_by=["Manectric-EX", "Basic", "EX", "ManectricEX"],
    subtypes=["Basic", "EX"],
    collector_number=113,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=310,
    abilities=[
        Attack(
            title="Overrun",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=snipe_attack(20),
        ),
        Attack(
            title="Assault Laser",
            game_text="If your opponent's Active Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 60 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)