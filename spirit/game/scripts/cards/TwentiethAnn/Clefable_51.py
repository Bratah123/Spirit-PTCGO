"""STUB: effect not implemented — do not guess mechanics.
Clefable (TwentiethAnn #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c6de8f1d-9d99-5a4b-93c6-df105822ee27",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Attack(
            title="Follow Me",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Moonblast",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 30 (before applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)