from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.pokemon import in_active_spot


async def cursed_body(ctx):
    """If Active and damaged by an opponent's attack, Attacking Pokémon is Confused."""
    pokemon = ctx.source
    if not in_active_spot(ctx.board, ctx.player_id, pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="4a473049-803a-50f5-9c67-71fbb5489724",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent", "Stage 1", "Jellicent"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Ability(
            title="Cursed Body",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Confused.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=cursed_body,
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 20 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.WATER), 20, base=10),
        ),
    ],
)
