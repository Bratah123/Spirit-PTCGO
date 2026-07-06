from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0ea98e7a-b544-5d31-8a46-66f4e6bc5f4d",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    display_name="Steenee",
    searchable_by=["Steenee", "Stage 1", "Steenee"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    family_id=761,
    abilities=[
        Attack(
            title="Captivate",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Smack",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)