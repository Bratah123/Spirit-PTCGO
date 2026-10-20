"""STUB: effect not implemented — do not guess mechanics.
Simisear (XY8 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per


card = PokemonCardDef(
    guid="cb9f855c-bdb4-5dd0-86fb-4482054a9df4",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1", "Simisear"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Water Fling",
            game_text="Put 3 Water Energy from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hand Fling",
            game_text="This attack does 10 damage times the number of cards in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=damage_per(lambda ctx: len(ctx.hand()), 10),
        ),
    ],
)