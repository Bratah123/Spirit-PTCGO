from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b31dc2af-fccd-5164-9169-c5efeafdc013",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    display_name="Solosis",
    searchable_by=["Solosis", "Basic", "Solosis"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=577,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)