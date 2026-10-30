from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="68d047ab-2efe-5c66-a5ca-f013acf604d2",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey",
    searchable_by=["Pidgey", "Basic", "Pidgey"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=16,
    abilities=[
        Attack(
            title="Corner",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)