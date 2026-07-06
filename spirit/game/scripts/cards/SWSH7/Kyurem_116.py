from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f309371-5702-5f03-9019-fe2863ce729d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name",
    display_name="Kyurem",
    searchable_by=["Kyurem", "Basic", "Kyurem"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=646,
    abilities=[
        Attack(
            title="Extreme Freeze",
            game_text="Discard any amount of Water Energy from your Pok\u00e9mon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.METAL: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)