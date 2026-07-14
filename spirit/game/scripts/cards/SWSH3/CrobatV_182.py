from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import dark_asset

card = PokemonCardDef(
    guid="a9034837-b287-56e7-a621-c2db77d7c62e",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatV.Name",
    display_name="Crobat V",
    searchable_by=["Crobat V", "Basic", "V", "CrobatV"],
    subtypes=["Basic", "V"],
    collector_number=182,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
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