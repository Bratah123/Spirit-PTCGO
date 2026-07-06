from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3bc3272f-5a2b-530b-8f3a-39fcb19f13a7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    display_name="Stufful",
    searchable_by=["Stufful", "Basic", "Stufful"],
    subtypes=["Basic"],
    collector_number=150,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=759,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)