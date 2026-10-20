"""STUB: effect not implemented — do not guess mechanics.
Shaymin-EX (Promo_XY #XY148): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db7627e5-ae1d-538b-9867-899fae093bdb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name",
    display_name="Shaymin-EX",
    searchable_by=["Shaymin-EX", "Basic", "EX", "ShayminEX"],
    subtypes=["Basic", "EX"],
    collector_number=148,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Ability(
            title="Aroma of Gratitude",
            game_text="Once during your turn (before your attack), you may heal 20 damage from each of your Benched Basic Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Floral Gain",
            game_text="Heal 20 damage and remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)