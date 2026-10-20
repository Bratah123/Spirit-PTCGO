"""STUB: effect not implemented — do not guess mechanics.
Hoopa (Promo_XY #XY147): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ee7990e-bd66-522b-8364-42941b0e94a7",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name",
    display_name="Hoopa",
    searchable_by=["Hoopa", "Basic", "Hoopa"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Attack(
            title="Hyperspace Punch",
            game_text="This attack does 20 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Portal Strike",
            game_text="This Pok\u00e9mon can't use Portal Strike during your next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)