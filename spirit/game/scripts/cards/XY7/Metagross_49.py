"""STUB: effect not implemented — do not guess mechanics.
Metagross (XY7 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba0642e5-af29-5fb2-b815-7fd2d18df58f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=49,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Magnetic Warp",
            game_text="Once during your turn (before your attack), you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Iron Cannon",
            game_text="You may discard all Metal Energy attached to this Pok\u00e9mon. If you do, this attack does 80 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)