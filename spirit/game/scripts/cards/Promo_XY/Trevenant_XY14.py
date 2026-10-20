"""STUB: effect not implemented — do not guess mechanics.
Trevenant (Promo_XY #XY14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a57343f-48a0-58bf-a049-ba60158b7c83",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1", "Trevenant"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=709,
    abilities=[
        Attack(
            title="Eerie Wave",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wood Hammer",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)