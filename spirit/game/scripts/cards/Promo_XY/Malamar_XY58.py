from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot


class _Contrary(Passive):
    """While this Pokemon is Active, the opponent's coin flips during their turn are tails."""
    def forces_coin_tails_during_own_turn(self, player_id, carrier):
        me = carrier_pokemon(carrier)
        return me is not None and is_in_active_spot(me) and player_id != me.owning_player_id


async def _conform(ctx):
    """40; if both hands are the same size, the opponent's Active is Confused."""
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is not None and ctx.hand_size() == ctx.hand_size(ctx.opponent_id):
        await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="6fce7a9d-eb00-54f5-a56f-d6bd85ce42cd",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=687,
    abilities=[
        Ability(
            title="Contrary",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, whenever your opponent flips a coin during his or her turn, treat it as tails.",
            passive=_Contrary(),
        ),
        Attack(
            title="Conform",
            game_text="If you have the same number of cards in your hand as your opponent, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_conform,
        ),
    ],
)