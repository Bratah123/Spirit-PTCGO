from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import effective_max_hp


def _victory_kiss_condition(board, player_id, pokemon=None):
    active = board.active_pokemon(player_id)
    return (pokemon is not None and active is not None and pokemon is not active
            and effective_max_hp(board, active) > active.get_attribute(AttrID.HP, 0))


async def _victory_kiss(ctx):
    """If this Pokemon is on your Bench, heal 10 damage from your Active."""
    if ctx.my_active() is not None:
        await ctx.heal(10, ctx.my_active())


card = PokemonCardDef(
    guid="f22c959e-8838-5686-91b2-d04bebe8b037",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Ability(
            title="Victory Kiss",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may heal 10 damage from your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_victory_kiss_condition,
            effect=_victory_kiss,
        ),
        Attack(
            title="Hug",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)