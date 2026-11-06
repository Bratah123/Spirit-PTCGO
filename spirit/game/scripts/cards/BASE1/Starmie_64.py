from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import (
    has_typed_basic_energy, recover_discarding_energy,
)


card = PokemonCardDef(
    guid="f86d55d6-0653-5c9d-a7e9-e60b6b92d21a",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="BASE1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard 1 Water Energy card attached to Starmie in order to use this attack. Remove all damage counters from Starmie.",
            cost={PokemonTypes.WATER: 2},
            condition=has_typed_basic_energy(PokemonTypes.WATER),
            effect=recover_discarding_energy(PokemonTypes.WATER),
        ),
        Attack(
            title="Star Freeze",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
