from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import effective_max_hp


def _is_psychic(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.PSYCHIC.value in types


def life_shaker_condition(board, player_id, pokemon):
    mine = [p for p in board.pokemon_in_play(player_id) if _is_psychic(p)]
    if len(mine) < 2:
        return False
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p) for p in mine)


async def life_shaker(ctx):
    """Move 1 damage counter from 1 of your Psychic Pokemon to another."""
    mine = [p for p in ctx.my_pokemon_in_play() if _is_psychic(p)]
    damaged = [p for p in mine if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose 1 of your Psychic Pokémon to move a damage counter from"
    )
    if source is None:
        return
    targets = [p for p in mine if p is not source]
    if not targets:
        return
    dest = await ctx.choose_pokemon(
        targets, "Choose 1 of your Psychic Pokémon to move the damage counter to"
    )
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=1)


card = PokemonCardDef(
    guid="f34044bd-297a-51b8-8e60-68b859787747",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Life Shaker",
            game_text="As often as you like during your turn, you may move 1 damage counter from 1 of your Psychic Pok\u00e9mon to another of your Psychic Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=life_shaker_condition,
            effect=life_shaker,
        ),
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)