from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e9503568-a733-59f3-9f7f-fe4cdd397b39",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonV.Name",
    display_name="Umbreon V",
    searchable_by=["Umbreon V", "Basic", "V", "Single Strike", "UmbreonV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=188,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=197,
    abilities=[
        Attack(
            title="Mean Look",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Moonlight Blade",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)