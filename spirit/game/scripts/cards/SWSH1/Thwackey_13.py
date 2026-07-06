from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9509e516-3340-54d5-9bc2-fe553be702bb",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    display_name="Thwackey",
    searchable_by=["Thwackey", "Stage 1", "Thwackey"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    family_id=810,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)