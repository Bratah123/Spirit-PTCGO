from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="42548660-c292-5bef-8bc4-95ec077385ed",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGoodraV.Name",
    display_name="Hisuian Goodra V",
    searchable_by=["Hisuian Goodra V", "Basic", "V", "HisuianGoodraV"],
    subtypes=["Basic", "V"],
    collector_number=187,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=706,
    abilities=[
        Attack(
            title="Slip-'n'-Trip",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Rolling Shell",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=unimplemented,
        ),
    ],
)