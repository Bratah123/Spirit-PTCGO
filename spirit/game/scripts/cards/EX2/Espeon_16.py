from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import (
    condition_attack, count_energy, damage_per,
)


card = PokemonCardDef(
    guid="e4025609-689b-5329-883e-956f4522f51c",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Espeon"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="EX2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Energy Crush",
            game_text="Does 20 more damage plus 10 more damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("opponent"), 10, base=20),
        ),
    ],
)
