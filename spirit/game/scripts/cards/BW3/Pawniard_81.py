from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d1e054e-a201-5311-bb47-64ef4531ecf4",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    display_name="Pawniard",
    searchable_by=["Pawniard", "Basic", "Pawniard"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="BW3",
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