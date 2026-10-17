"""STUB: effect not implemented — do not guess mechanics.
Snorlax (XY2 #80): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a9d82a14-800f-5f02-9e78-f969af42cdfa",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Stir and Snooze",
            game_text="If this Pok\u00e9mon is Asleep, flip 2 coins instead of 1 between turns. If either of them is tails, this Pok\u00e9mon is still Asleep.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sleepy Press",
            game_text="Heal 20 damage from this Pok\u00e9mon. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)