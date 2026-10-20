from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2bda0c14-c242-5123-a3e6-7d71092ec9c2",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewEX.Name",
    display_name="Mew-EX",
    searchable_by=["Mew-EX", "Basic", "EX", "MewEX"],
    subtypes=["Basic", "EX"],
    collector_number=139,
    set_code="BW11",
    rarity=Rarities.RareUltra,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Versatile",
            game_text="This Pok\u00e9mon can use the attacks of any Pok\u00e9mon in play (both yours and your opponent's). (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Replace",
            game_text="Move as many Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)