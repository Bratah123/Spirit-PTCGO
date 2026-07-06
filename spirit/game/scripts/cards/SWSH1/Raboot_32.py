from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e295f9a6-2b3b-5a0a-8929-8f832da97ffc",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    display_name="Raboot",
    searchable_by=["Raboot", "Stage 1", "Raboot"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    family_id=813,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Magnum Kick",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)