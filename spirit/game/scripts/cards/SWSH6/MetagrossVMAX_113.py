from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7cf01536-fbc5-54ed-af1f-6872961eb578",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossVMAX.Name",
    display_name="Metagross VMAX",
    searchable_by=["Metagross VMAX", "VMAX", "Rapid Strike", "MetagrossVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=113,
    set_code="SWSH6",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossV.Name",
    family_id=376,
    abilities=[
        Attack(
            title="Zap Traction",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Max Rush",
            game_text="During your next turn, this Pok\u00e9mon's Max Rush attack does 150 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)