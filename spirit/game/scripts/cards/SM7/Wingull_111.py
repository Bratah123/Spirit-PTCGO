from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="faca3a5a-92e8-5817-9529-fcddba67fe13",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    display_name="Wingull",
    searchable_by=["Wingull", "Basic", "Wingull"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=278,
    abilities=[
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)