from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1d51a40-c185-53aa-8ce2-031b8aa52e3d",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1", "Simisear"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Flame Blast",
            game_text="Does 20 more damage for each Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)