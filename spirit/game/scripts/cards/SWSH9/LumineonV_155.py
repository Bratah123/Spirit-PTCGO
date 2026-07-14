from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import luminous_sign, aqua_return

card = PokemonCardDef(
    guid="722e8bee-1cca-5b48-b46a-72580883b149",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LumineonV.Name",
    display_name="Lumineon V",
    searchable_by=["Lumineon V", "Basic", "V", "LumineonV"],
    subtypes=["Basic", "V"],
    collector_number=155,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=457,
    abilities=[
        Ability(
            title="Luminous Sign",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_PLAY,
            effect=luminous_sign,
        ),
        Attack(
            title="Aqua Return",
            game_text="Shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=aqua_return,
        ),
    ],
)