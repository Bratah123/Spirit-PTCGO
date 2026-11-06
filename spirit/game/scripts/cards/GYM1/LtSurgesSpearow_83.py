from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="e2aafdb7-4534-54fd-8b63-2de0e8d1f734",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesSpearow.Name",
    display_name="Lt. Surge's Spearow",
    searchable_by=["Lt. Surge's Spearow", "Basic", "LtSurgesSpearow"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=21,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Razor Wind",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)
