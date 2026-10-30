from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f2c8f3e1-b78e-56a7-92fb-2f19256c8f93",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    display_name="Natu δ",
    searchable_by=["Natu \u03b4", "Basic", "Natu"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=177,
    abilities=[
        Attack(
            title="Flop",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)