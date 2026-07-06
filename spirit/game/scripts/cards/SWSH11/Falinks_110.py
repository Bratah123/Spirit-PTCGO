from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d287bd67-a29a-5307-baee-39a1f3f27da7",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic", "Falinks"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Fighting Headbutt",
            game_text="This attack's damage isn't affected by Weakness. If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)