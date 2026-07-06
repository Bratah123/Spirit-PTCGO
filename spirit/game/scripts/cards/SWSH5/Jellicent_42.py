from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ddec2db-fb71-55e3-bf8f-30bf4d005a49",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent", "Stage 1", "Jellicent"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Attack(
            title="Sediment Sink",
            game_text="This attack does 10 damage for each Water Energy card in your discard pile.",
            cost={PokemonTypes.WATER: 2},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)