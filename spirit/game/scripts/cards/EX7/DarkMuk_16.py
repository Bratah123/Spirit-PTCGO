from spirit.game.card_effects.ex import slimy_water_retreat, sticky_goo_retreat_passive
"""STUB: effect not implemented — do not guess mechanics.
Dark Muk (EX7 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    passive=sticky_goo_retreat_passive(),
    guid="04be4fe2-3e14-5bf5-bc0d-20ae2780a7c0",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMuk.Name",
    display_name="Dark Muk",
    searchable_by=["Dark Muk", "Stage 1", "DarkMuk"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Sticky Goo",
            game_text="As long as Dark Muk is your Active Pok\u00e9mon, your opponent pays ColorlessColorless more to retreat his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Slimy Water",
            game_text="Does 10 damage times the number of Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost (after applying effects to the Retreat Cost).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=slimy_water_retreat(),
        ),
        Attack(
            title="Acidic Poison",
            game_text="The Defending Pok\u00e9mon is now Burned and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.POISONED),
        ),
    ],
)