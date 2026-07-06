from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ec75e675-4b6b-561b-a798-22c8d4f04c13",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegielekiV.Name",
    display_name="Regieleki V",
    searchable_by=["Regieleki V", "Basic", "V", "RegielekiV"],
    subtypes=["Basic", "V"],
    collector_number=57,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=894,
    abilities=[
        Attack(
            title="Switching Bolt",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Wall",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)