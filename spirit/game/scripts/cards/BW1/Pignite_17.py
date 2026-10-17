from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe8febd6-84e2-5f73-b138-ec073ce023b4",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    display_name="Pignite",
    searchable_by=["Pignite", "Stage 1", "Pignite"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    family_id=498,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)