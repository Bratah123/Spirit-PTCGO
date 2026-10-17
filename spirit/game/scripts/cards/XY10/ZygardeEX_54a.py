"""STUB: effect not implemented — do not guess mechanics.
Zygarde-EX (XY10 #54a): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6090233c-8db4-5937-bf2c-874d50aa7c86",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeEX.Name",
    display_name="Zygarde-EX",
    searchable_by=["Zygarde-EX", "Basic", "EX", "ZygardeEX"],
    subtypes=["Basic", "EX"],
    collector_number=54,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Land's Pulse",
            game_text="If there is any Stadium card in play, this attack does 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cell Storm",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Land's Wrath",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)