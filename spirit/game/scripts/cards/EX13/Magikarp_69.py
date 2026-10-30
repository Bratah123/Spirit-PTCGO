from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcc1f08d-5e83-56e8-8b6d-0106811625be",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp δ",
    searchable_by=["Magikarp \u03b4", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Splash",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)