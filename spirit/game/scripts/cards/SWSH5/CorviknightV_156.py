from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5d16d2f-5590-5396-8988-6c5e12f2ac6a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CorviknightV.Name",
    display_name="Corviknight V",
    searchable_by=["Corviknight V", "Basic", "V", "CorviknightV"],
    subtypes=["Basic", "V"],
    collector_number=156,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=823,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Sky Hurricane",
            game_text="During your next turn, this Pok\u00e9mon can't use Sky Hurricane.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
    ],
)