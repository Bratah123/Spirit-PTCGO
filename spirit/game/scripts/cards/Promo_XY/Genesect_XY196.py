"""STUB: effect not implemented — do not guess mechanics.
Genesect (Promo_XY #XY196): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="580b4c35-d908-5000-9e95-eac8e390bfd5",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect", "Basic", "Genesect"],
    subtypes=["Basic"],
    collector_number=196,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=649,
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Destructor Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)