"""STUB: effect not implemented — do not guess mechanics.
Meloetta (Promo_XY #XY193): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1e74244-e058-5369-a34b-5d87f97e8170",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta", "Basic", "Meloetta"],
    subtypes=["Basic"],
    collector_number=193,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=648,
    abilities=[
        Attack(
            title="Soprano Wave",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Entrancing Melody",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)