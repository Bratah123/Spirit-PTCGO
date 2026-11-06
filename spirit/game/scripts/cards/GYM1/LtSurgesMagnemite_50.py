from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import removal_pulse


card = PokemonCardDef(
    guid="3cb66ba4-70ca-5666-8e03-be11b7c4f2e6",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesMagnemite.Name",
    display_name="Lt. Surge's Magnemite",
    searchable_by=["Lt. Surge's Magnemite", "Basic", "LtSurgesMagnemite"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Attack(
            title="Removal Pulse",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, flip a coin. If heads, choose 1 of those Energy cards and discard it.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=removal_pulse,
        ),
        Attack(
            title="Confusion Pulse",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
