from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb70d3b6-aa5d-581f-96c5-5b1c7fff0eb9",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=351,
    abilities=[
        Ability(
            title="Weather Reading",
            game_text="If you have 8 or more Stadium cards in your discard pile, ignore all Energy in this Pok\u00e9mon's attack costs.",
            effect=unimplemented,
        ),
        Attack(
            title="Weather Force",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=unimplemented,
        ),
    ],
)