from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.session.effects import is_special_energy


async def _metallic_sound(ctx):
    """Discard all Special Energy from each Pokemon (both players')."""
    picks = []
    for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if p.owning_player_id != ctx.player_id and ctx.effects_blocked(p):
            continue
        picks.extend(e for e in ctx.attached_energies(p) if is_special_energy(e))
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="c4cc6609-9849-5bee-9e5f-42c0f74f96f9",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=227,
    abilities=[
        Attack(
            title="Metallic Sound",
            game_text="Discard all Special Energy from each Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_metallic_sound,
        ),
        Attack(
            title="Aerial Ace",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)