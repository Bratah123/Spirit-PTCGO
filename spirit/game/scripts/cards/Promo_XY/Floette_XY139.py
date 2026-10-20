"""STUB: effect not implemented — do not guess mechanics.
Floette (Promo_XY #XY139): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5fd52bfd-e398-5360-974a-069512cc18af",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    display_name="Floette",
    searchable_by=["Floette", "Stage 1", "Floette"],
    subtypes=["Stage 1"],
    collector_number=139,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flabebe.Name",
    family_id=670,
    abilities=[
        Attack(
            title="Aromatherapy",
            game_text="Heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 20 more damage and heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)