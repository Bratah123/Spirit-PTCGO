from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import psyburst, reflect_shield


card = PokemonCardDef(
    guid="12f4704d-272a-5fe1-9d6e-c42b0326f141",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningMewtwo.Name",
    display_name="Shining Mewtwo",
    searchable_by=["Shining Mewtwo", "Basic", "ShiningMewtwo"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="NEO4",
    rarity=Rarities.Shining,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Reflect Shield",
            game_text="If an attack does damage to Shining Mewtwo during your opponent's next turn (even if Shining Mewtwo is Knocked Out), flip a coin. If heads, prevent all damage done to Shining Mewtwo from that attack (any other effects of attacks still happen) and do 20 damage to the attacking Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.LIGHTNING: 1},
            effect=reflect_shield,
        ),
        Attack(
            title="Psyburst",
            game_text="Discard a Fire Energy card attached to Shining Mewtwo or this attack does nothing. This attack does 40 damage plus 10 damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="+",
            effect=psyburst,
        ),
    ],
)
