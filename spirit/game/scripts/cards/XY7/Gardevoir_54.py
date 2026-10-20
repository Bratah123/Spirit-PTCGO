from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import effective_max_hp
from spirit.game.card_effects.attacks_common import snipe_attack


def _bright_condition(board, player_id, pokemon=None):
    return any(effective_max_hp(board, p) > p.get_attribute(AttrID.HP, 0)
               for p in board.pokemon_in_play(player_id))


async def _bright_heal(ctx):
    """Heal 20 damage from each of your Pokemon."""
    for p in ctx.my_pokemon_in_play():
        await ctx.heal(20, p)


card = PokemonCardDef(
    guid="af29d6f6-194b-5c5b-93d3-a69530aab29c",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=54,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Bright Heal",
            game_text="Once during your turn (before your attack), you may heal 20 damage from each of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_bright_condition,
            effect=_bright_heal,
        ),
        Attack(
            title="Telekinesis",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(50, pool='any', apply_modifiers=False),
        ),
    ],
)