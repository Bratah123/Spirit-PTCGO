"""STUB: effect not implemented — do not guess mechanics.
Altaria (EX8 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import safeguard_ex_passive



async def double_wing_attack(ctx):
    """Does 20 damage to each Defending Pokémon (no printed damage)."""
    await ctx.deal_damage(20)


card = PokemonCardDef(
    guid="79dcf993-5186-5988-ac9c-b7496a57aee7",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to Altaria by your opponent's Pok\u00e9mon-ex.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=safeguard_ex_passive(),
        ),
        Attack(
            title="Double Wing Attack",
            game_text="Does 20 Damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=double_wing_attack,
        ),
        Attack(
            title="Dive",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)