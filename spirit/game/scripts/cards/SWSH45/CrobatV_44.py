from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.pokemon import dark_asset, condition_attack

card = PokemonCardDef(
    guid="1954b5d0-43c6-5813-90b6-53abf8af87fd",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatV.Name",
    display_name="Crobat V",
    searchable_by=["Crobat V", "Basic", "V", "CrobatV"],
    subtypes=["Basic", "V"],
    collector_number=44,
    set_code="SWSH45",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=169,
    abilities=[
        Ability(
            title="Dark Asset",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may draw cards until you have 6 cards in your hand. You can't use more than 1 Dark Asset Ability each turn.",
            trigger=Triggers.ON_PLAY,
            shared_once_per_turn="Dark Asset",
            effect=dark_asset,
        ),
        Attack(
            title="Venomous Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
