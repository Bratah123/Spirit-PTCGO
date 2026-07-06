from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="40f96e02-b834-5e06-9de1-9e625c108cd8",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaV.Name",
    display_name="Origin Forme Palkia V",
    searchable_by=["Origin Forme Palkia V", "Basic", "V", "OriginFormePalkiaV"],
    subtypes=["Basic", "V"],
    collector_number=167,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Attack(
            title="Rule the Region",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Break",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)