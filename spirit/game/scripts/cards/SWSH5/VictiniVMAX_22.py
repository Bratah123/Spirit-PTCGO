from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8fe4abce-cc29-5fc3-a8fa-74321eb2742e",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniVMAX.Name",
    display_name="Victini VMAX",
    searchable_by=["Victini VMAX", "VMAX", "VictiniVMAX"],
    subtypes=["VMAX"],
    collector_number=22,
    set_code="SWSH5",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniV.Name",
    family_id=494,
    abilities=[
        Attack(
            title="Spreading Flames",
            game_text="Attach up to 3 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Max Victory",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 120 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)