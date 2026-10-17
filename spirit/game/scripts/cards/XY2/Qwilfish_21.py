"""STUB: effect not implemented — do not guess mechanics.
Qwilfish (XY2 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d373731-726e-51cd-828b-15427d8dd7b8",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name",
    display_name="Qwilfish",
    searchable_by=["Qwilfish", "Basic", "Qwilfish"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=211,
    abilities=[
        Ability(
            title="Counterattack Quills",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)