"""STUB: effect not implemented — do not guess mechanics.
Honedge (Promo_XY #XY12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be661dc6-3b79-5a00-9338-a4856a058c2a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    display_name="Honedge",
    searchable_by=["Honedge", "Basic", "Honedge"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=679,
    abilities=[
        Attack(
            title="Swords Dance",
            game_text="During your next turn, this Pok\u00e9mon's Slash attack's base damage is 40.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)