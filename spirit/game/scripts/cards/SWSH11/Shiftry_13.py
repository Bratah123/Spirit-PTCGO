from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e1e3b13c-790e-500a-b26e-e72d8bd3af1a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Fan Tornado",
            game_text="You may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Tearing Gust",
            game_text="Put this Pok\u00e9mon and all attached cards in the Lost Zone.",
            cost={PokemonTypes.GRASS: 1},
            damage=210,
            effect=unimplemented,
        ),
    ],
)