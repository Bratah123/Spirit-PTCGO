from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import energy_provides_type


def _shift_gear_condition(board, player_id, pokemon) -> bool:
    pkmn = board.pokemon_in_play(player_id)
    if len(pkmn) < 2:
        return False
    return any(
        energy_provides_type(e, PokemonTypes.METAL.value)
        for p in pkmn for e in board.attached_energies(p)
    )


async def shift_gear(ctx):
    """Move a Metal Energy from 1 of your Pokémon to another (repeatable)."""
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(
        mine, mine,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.METAL.value),
        max_count=1,
        prompt="Choose a Metal Energy to move",
    )


card = PokemonCardDef(
    guid="c4b694a1-3bba-5ee5-a1e0-80d5582db182",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Shift Gear",
            game_text="As often as you like during your turn (before your attack), you may move a Metal Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_shift_gear_condition,
            effect=shift_gear,
        ),
        Attack(
            title="Gear Grind",
            game_text="Flip 2 coins. This attack does 80 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=80),
        ),
    ],
)
