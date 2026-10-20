from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="40dd4c62-7880-5ce7-95a0-171d9ad4e08e",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    display_name="Machop",
    searchable_by=["Machop", "Basic", "Machop"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=66,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)