from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="edf3398f-8777-5e83-a7a1-6261b49f092e",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonVMAX.Name",
    display_name="Flareon VMAX",
    searchable_by=["Flareon VMAX", "VMAX", "Single Strike", "FlareonVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=18,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonV.Name",
    family_id=136,
    abilities=[
        Attack(
            title="Max Detonate",
            game_text="Discard the top 5 cards of your deck. This attack does 100 damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)