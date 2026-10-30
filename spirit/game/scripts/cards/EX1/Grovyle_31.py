from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack, swift_attack


card = PokemonCardDef(
    guid="48cbca45-cd87-5e74-8549-8c2eaceca6cc",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    display_name="Grovyle",
    searchable_by=["Grovyle", "Stage 1", "Grovyle"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    family_id=252,
    abilities=[
        Attack(
            title="Poison Breath",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=swift_attack(),
        ),
    ],
)
