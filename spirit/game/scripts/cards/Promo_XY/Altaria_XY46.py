"""STUB: effect not implemented — do not guess mechanics.
Altaria (Promo_XY #XY46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="903b9ed1-c952-50cd-bd58-6f4ba05ea94e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=334,
    abilities=[
        Ability(
            title="Clear Humming",
            game_text="Each of your Colorless Pok\u00e9mon has no Weakness.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)