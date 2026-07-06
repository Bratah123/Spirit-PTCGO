from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5edb9814-ca2f-5889-99d4-25c86d6b373c",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragapultVMAX.Name",
    display_name="Dragapult VMAX",
    searchable_by=["Dragapult VMAX", "VMAX", "DragapultVMAX"],
    subtypes=["VMAX"],
    collector_number=197,
    set_code="SWSH2",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DragapultV.Name",
    family_id=887,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Max Phantom",
            game_text="Put 5 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)