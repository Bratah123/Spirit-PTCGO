from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3ecf5444-4195-5527-b633-eed9b6578756",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    display_name="Rufflet",
    searchable_by=["Rufflet", "Basic", "Rufflet"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=627,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)