"""STUB: effect not implemented — do not guess mechanics.
Steelix ex (EX10 #109): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.card_effects.ex import metal_charge_self_counter, poison_immunity_passive, mudslide_snipe

card = PokemonCardDef(
    guid="f12505da-6a31-5d55-be47-3e16c810debc",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelixex.Name",
    display_name="Steelix ex",
    searchable_by=["Steelix ex", "Stage 1", "ex", "Steelixex"],
    subtypes=["Stage 1", "ex"],
    collector_number=109,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=5,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Ability(
            title="Poison Resistance",
            game_text="Steelix ex can't be Poisoned.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=condition_immunity_passive(SpecialConditions.POISONED),
        ),
        Attack(
            title="Metal Charge",
            game_text="Put 1 damage counter on Steelix ex.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=metal_charge_self_counter(1),
        ),
        Attack(
            title="Mudslide",
            game_text="Discard 2 Fighting Energy attached to Steelix ex and choose 1 of your opponent's Pok\u00e9mon. This attack does 100 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            effect=mudslide_snipe(100, PokemonTypes.FIGHTING, 2),
        ),
    ],
)