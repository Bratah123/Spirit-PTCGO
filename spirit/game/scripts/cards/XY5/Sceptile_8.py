"""STUB: effect not implemented — do not guess mechanics.
Sceptile (XY5 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d09f31d-0f9a-5144-874a-da8f24b55ef3",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Nurture and Heal",
            game_text="Once during your turn (before your attack), you may attach a Grass Energy card from your hand to 1 of your Pok\u00e9mon. If you do, heal 30 damage from that Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Jungle Edge",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)