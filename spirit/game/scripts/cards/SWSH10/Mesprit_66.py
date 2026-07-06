from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b492025b-05a7-5886-a8e5-1c7b35e60b31",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    display_name="Mesprit",
    searchable_by=["Mesprit", "Basic", "Mesprit"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=481,
    abilities=[
        Ability(
            title="Mental Shroud",
            game_text="If you have Uxie and Azelf in play, each of your Pok\u00e9mon has no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)