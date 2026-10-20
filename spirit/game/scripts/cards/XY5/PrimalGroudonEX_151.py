"""STUB: effect not implemented — do not guess mechanics.
Primal Groudon-EX (XY5 #151): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait

card = PokemonCardDef(
    guid="05023339-cfc8-5d71-8e56-9acdb78039ba",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PrimalGroudonEX.Name",
    display_name="Primal Groudon-EX",
    searchable_by=["Primal Groudon-EX", "MEGA", "EX", "PrimalGroudonEX"],
    subtypes=["MEGA", "EX"],
    collector_number=151,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GroudonEX.Name",
    family_id=383,
    abilities=[
        ancient_trait('Ω Barrier'),
        Attack(
            title="Gaia Volcano",
            game_text="If there is any Stadium card in play, this attack does 100 more damage. Discard that Stadium card.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)