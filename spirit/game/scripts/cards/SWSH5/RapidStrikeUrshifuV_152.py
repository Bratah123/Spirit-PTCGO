from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2651c173-cb49-5075-97a0-1354342f7f27",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifuV.Name",
    display_name="Rapid Strike Urshifu V",
    searchable_by=["Rapid Strike Urshifu V", "Basic", "V", "Rapid Strike", "RapidStrikeUrshifuV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=152,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=892,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Hundred Furious Blows",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)