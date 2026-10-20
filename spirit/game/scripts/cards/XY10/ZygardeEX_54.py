"""STUB: effect not implemented — do not guess mechanics.
Zygarde-EX (XY10 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="02de805e-6912-59f7-87bc-f34be6e7f73a",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeEX.Name",
    display_name="Zygarde-EX",
    searchable_by=["Zygarde-EX", "Basic", "EX", "ZygardeEX"],
    subtypes=["Basic", "EX"],
    collector_number=54,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
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
            effect=heal_attack(30),
        ),
        Attack(
            title="Land's Wrath",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)