"""STUB: effect not implemented — do not guess mechanics.
Silcoon (EX8 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import advanced_armor_vs_evolved


card = PokemonCardDef(
    guid="9b2cf73c-152a-5e2b-bea6-8148530f54d7",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    display_name="Silcoon",
    searchable_by=["Silcoon", "Stage 1", "Silcoon"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Advanced Armor",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to Silcoon by your opponent's Evolved Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=advanced_armor_vs_evolved(),
        ),
    ],
)