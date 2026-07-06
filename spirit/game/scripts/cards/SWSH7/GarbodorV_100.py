from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="514bed7f-5ea4-5267-9dc8-63f24c7a242f",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarbodorV.Name",
    display_name="Garbodor V",
    searchable_by=["Garbodor V", "Basic", "V", "GarbodorV"],
    subtypes=["Basic", "V"],
    collector_number=100,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=569,
    abilities=[
        Attack(
            title="Trash Stench",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During your opponent's next turn, that Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)