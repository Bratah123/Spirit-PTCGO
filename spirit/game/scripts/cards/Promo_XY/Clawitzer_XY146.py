"""STUB: effect not implemented — do not guess mechanics.
Clawitzer (Promo_XY #XY146): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="14575688-ec8e-552f-a5a1-f281e87a5798",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    display_name="Clawitzer",
    searchable_by=["Clawitzer", "Stage 1", "Clawitzer"],
    subtypes=["Stage 1"],
    collector_number=146,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    family_id=693,
    abilities=[
        Ability(
            title="Mega Boost",
            game_text="Once during your turn (before your attack), you may attach a Special Energy card from your hand to 1 of your Mega Evolution Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)