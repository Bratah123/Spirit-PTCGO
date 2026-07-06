from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6280135f-4c64-50c3-928b-298210e5fc62",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionV.Name",
    display_name="Drapion V",
    searchable_by=["Drapion V", "Basic", "V", "DrapionV"],
    subtypes=["Basic", "V"],
    collector_number=175,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=452,
    abilities=[
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title="Hazardous Claws",
            game_text="Discard 2 Energy from this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)