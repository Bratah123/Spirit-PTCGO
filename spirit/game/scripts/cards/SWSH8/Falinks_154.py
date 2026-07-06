from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc667b80-cf84-5438-9cae-507e45d5e85d",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic", "Falinks"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Cliff Edge Formation",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 160 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)