from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e75359b9-ec76-5414-bc7b-2841f4b97fdf",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    display_name="Thwackey",
    searchable_by=["Thwackey", "Stage 1", "Thwackey"],
    subtypes=["Stage 1"],
    collector_number=12,
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
            title="Taunt",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Double Hit",
            game_text="Flip 2 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)