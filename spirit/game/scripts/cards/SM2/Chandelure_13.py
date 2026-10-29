from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import AttrID
from spirit.game.data_utils import Activations


from spirit.game.models.board import PokemonEntity
from spirit.game.session.passives import effective_max_hp


def shady_move_condition(board, player_id, pokemon=None):
    for pid in board.player_ids:
        for p in board.pokemon_in_play(pid):
            if isinstance(p, PokemonEntity) and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p):
                return True
    return False


async def shady_move(ctx):
    """Move 1 damage counter from 1 Pokémon to another Pokémon."""
    pool = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    damaged = [p for p in pool if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    src = await ctx.choose_pokemon(damaged, "Choose a Pokémon to move a damage counter from")
    if src is None:
        return
    dests = [p for p in pool if p is not src]
    if not dests:
        return
    dest = await ctx.choose_pokemon(dests, "Choose a Pokémon to move the damage counter to")
    if dest is None:
        return
    await ctx.move_damage_counters(src, dest, max_count=1)


card = PokemonCardDef(
    guid="5172b7b5-9594-54c8-82d6-630375f9fb44",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Shady Move",
            game_text="Once during your turn (before your attack), you may move 1 damage counter from 1 Pok\u00e9mon to another Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN, condition=shady_move_condition,
            effect=shady_move,
        ),
        Attack(
            title="Super Singe",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)