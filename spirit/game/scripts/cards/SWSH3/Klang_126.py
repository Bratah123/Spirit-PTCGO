from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8a5c09e9-0d53-55eb-b73d-d3e29ea22f2e",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    display_name="Klang",
    searchable_by=["Klang", "Stage 1", "Klang"],
    subtypes=["Stage 1"],
    collector_number=126,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Call for Backup",
            game_text="Search your deck for a Metal Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)