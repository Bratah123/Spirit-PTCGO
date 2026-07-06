from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1988f57-0828-5c4f-801f-1b5e703918e9",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CoalossalV.Name",
    display_name="Coalossal V",
    searchable_by=["Coalossal V", "Basic", "V", "CoalossalV"],
    subtypes=["Basic", "V"],
    collector_number=173,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=839,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)