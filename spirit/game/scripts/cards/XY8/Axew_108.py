from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9281e840-35e4-517f-a70b-89875578e62a",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=610,
    abilities=[
        Attack(
            title="Brat Snack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)