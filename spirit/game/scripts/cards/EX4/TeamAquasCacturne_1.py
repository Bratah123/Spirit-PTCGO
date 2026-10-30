"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Cacturne (EX4 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.ex import may_discard_energy_paralyze
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="1fb57766-4e66-53d8-ab73-2f2db6d17a5d",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCacturne.Name",
    display_name="Team Aqua's Cacturne",
    searchable_by=["Team Aqua's Cacturne", "Stage 1", "TeamAquasCacturne"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCacnea.Name",
    family_id=331,
    abilities=[
        Attack(
            title="Dark Bind",
            game_text="You may discard a Darkness Energy card attached to Team Aqua's Cacturne. If you do, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=may_discard_energy_paralyze(PokemonTypes.DARKNESS),
        ),
        Attack(
            title="Poison Barb",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)