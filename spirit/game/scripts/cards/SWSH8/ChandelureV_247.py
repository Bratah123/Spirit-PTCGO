from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import is_trainer_card


async def poltergeist(ctx):
    """Opponent reveals their hand; 40 damage for each Trainer card found there."""
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id)
    count = sum(1 for c in cards if is_trainer_card(c))
    await ctx.deal_damage(40 * count)


card = PokemonCardDef(
    guid="93b88900-2afa-5180-80dd-291142165c2e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureV.Name",
    display_name="Chandelure V",
    searchable_by=["Chandelure V", "Basic", "V", "ChandelureV"],
    subtypes=["Basic", "V"],
    collector_number=247,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=609,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 40 damage for each Trainer card you find there.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=poltergeist,
        ),
    ],
)