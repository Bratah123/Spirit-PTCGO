from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="602991ff-f83d-5337-87fe-b052b22b85fb",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=147,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Hurricane Blender",
            game_text="Move any amount of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=170,
            effect=unimplemented,
        ),
    ],
)