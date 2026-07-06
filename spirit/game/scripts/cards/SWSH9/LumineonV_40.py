from spirit.game.card_effects.pokemon import aqua_return, luminous_sign
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b4ce3a0e-da4d-5478-899a-ec0a364bc59a",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LumineonV.Name",
    display_name="Lumineon V",
    searchable_by=["Lumineon V", "Basic", "V", "LumineonV"],
    subtypes=["Basic", "V"],
    collector_number=40,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=457,
    abilities=[
        Ability(
            title="Luminous Sign",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_PLAY,
            effect=luminous_sign,
        ),
        Attack(
            title="Aqua Return",
            game_text="Shuffle this Pokémon and all attached cards into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=aqua_return,
        ),
    ],
)
