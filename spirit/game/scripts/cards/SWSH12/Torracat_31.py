from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5770fc4-fedb-5dd0-a636-31505b2bf992",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    display_name="Torracat",
    searchable_by=["Torracat", "Stage 1", "Torracat"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Gritty Claws",
            game_text="During your opponent's next turn, if this Pok\u00e9mon has full HP and would be Knocked Out by damage from an attack, it is not Knocked Out, and its remaining HP becomes 10.",
            cost={PokemonTypes.FIRE: 2},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
        ),
    ],
)