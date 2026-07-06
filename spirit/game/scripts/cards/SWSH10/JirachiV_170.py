from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ded4a63a-004b-56c4-9eba-c4086feb7e91",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiV.Name",
    display_name="Jirachi V",
    searchable_by=["Jirachi V", "Basic", "V", "JirachiV"],
    subtypes=["Basic", "V"],
    collector_number=170,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=385,
    abilities=[
        Ability(
            title="Wish Connector",
            game_text="When 1 of your Basic Pok\u00e9mon V is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, you may move a basic Energy card from that Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Hypnostrike",
            game_text="Both Active Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)