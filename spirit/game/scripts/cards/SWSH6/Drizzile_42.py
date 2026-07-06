from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf8b735e-71a0-509a-b08d-b5b844863d7b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    display_name="Drizzile",
    searchable_by=["Drizzile", "Stage 1", "Rapid Strike", "Drizzile"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=42,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    family_id=816,
    abilities=[
        Attack(
            title="Bounce",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)