from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import more_poison

card = PokemonCardDef(
    guid="1b3d96e7-5b0f-5b4e-9c89-2413908a0fcd",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantHisuianSneasler.Name",
    display_name="Radiant Hisuian Sneasler",
    searchable_by=["Radiant Hisuian Sneasler", "Basic", "Radiant", "RadiantHisuianSneasler"],
    subtypes=["Basic", "Radiant"],
    collector_number=123,
    set_code="SWSH11",
    rarity=Rarities.RareRadiant,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=903,
    abilities=[
        Ability(
            title="Poison Peak",
            game_text="During Pok\u00e9mon Checkup, put 2 more damage counters on your opponent's Poisoned Pok\u00e9mon.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=more_poison,
        ),
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)