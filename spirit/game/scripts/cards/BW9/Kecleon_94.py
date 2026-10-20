from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="525953ca-598a-5dfb-abee-966acf3dd4ea",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic", "Kecleon"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Color Change",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, this Pok\u00e9mon is the same type as the your opponent's Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Imittack",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. If this Pok\u00e9mon has the necessary Energy to use that attack, use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)