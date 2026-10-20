from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0ebd0e3f-f164-5d44-885b-ffe0751c8edb",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    display_name="Pawniard",
    searchable_by=["Pawniard", "Basic", "Pawniard"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=624,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Cut",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)