from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import messenger


card = PokemonCardDef(
    guid="0509799c-387f-55f7-8db7-f85f464d4cd2",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasPidgey.Name",
    display_name="Koga's Pidgey",
    searchable_by=["Koga's Pidgey", "Basic", "KogasPidgey"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=16,
    abilities=[
        Attack(
            title="Messenger",
            game_text="Put Koga's Pidgey and all cards attached to it on top of your deck. Then search your deck for any Basic Pok\u00e9mon or Evolution card not named Koga's Pidgey. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=messenger(),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
