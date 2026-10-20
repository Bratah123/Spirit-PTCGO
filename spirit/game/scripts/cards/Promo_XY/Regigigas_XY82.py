"""STUB: effect not implemented — do not guess mechanics.
Regigigas (Promo_XY #XY82): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="69c1fa80-da82-5ed7-a73d-2bbe8abfc850",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Ability(
            title="Earthen Awakening",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon, heal 20 damage from it.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gigas Punch",
            game_text="Flip 2 coins. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)