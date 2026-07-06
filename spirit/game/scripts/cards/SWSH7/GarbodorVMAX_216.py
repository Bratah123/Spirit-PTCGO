from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0db6edab-04f5-57ce-adfa-ce90e8778b25",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarbodorVMAX.Name",
    display_name="Garbodor VMAX",
    searchable_by=["Garbodor VMAX", "VMAX", "GarbodorVMAX"],
    subtypes=["VMAX"],
    collector_number=216,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GarbodorV.Name",
    family_id=569,
    abilities=[
        Ability(
            title="Rubbish Collecting",
            game_text="This Pok\u00e9mon may have up to 2 Pok\u00e9mon Tools attached to it. If it loses this Ability, discard Pok\u00e9mon Tools from it until only 1 remains.",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Malodor",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During your opponent's next turn, that Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)