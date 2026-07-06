from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="45ad3075-16d0-5034-9fe7-ca8a81419e83",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FalinksV.Name",
    display_name="Falinks V",
    searchable_by=["Falinks V", "Basic", "V", "FalinksV"],
    subtypes=["Basic", "V"],
    collector_number=185,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Ability(
            title="Iron Defense Formation",
            game_text="All of your Pok\u00e9mon that have \"Falinks\" in their name take 20 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=unimplemented,
        ),
    ],
)