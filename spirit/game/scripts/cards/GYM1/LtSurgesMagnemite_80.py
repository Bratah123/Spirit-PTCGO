from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="0bbb653a-c0d5-597f-93af-a55b56a94c00",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesMagnemite.Name",
    display_name="Lt. Surge's Magnemite",
    searchable_by=["Lt. Surge's Magnemite", "Basic", "LtSurgesMagnemite"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Attack(
            title="Thundershock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
